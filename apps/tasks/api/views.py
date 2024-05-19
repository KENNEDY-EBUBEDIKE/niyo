from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.tasks.models import Task
from .serializers import TaskSerializer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(
            data={
                "success": True,
                "message": "OK",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            new_task = serializer.save()
            notify_ws_clients(new_task, 'create')
            return Response(
                data={"success": True, "message": "OK"},
                status=status.HTTP_201_CREATED
            )
        return Response(
            data={"success": False, "message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes((IsAuthenticated,))
def task_detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Response(
            data={"success": False, "message": "Task Not Found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(
            data={
                "success": True,
                "message": "OK",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    elif request.method == 'PATCH':
        serializer = TaskSerializer(instance=task, data=request.data, partial=True)
        if serializer.is_valid():
            task = serializer.save()
            notify_ws_clients(task, 'update')
            return Response(
                data={
                    "success": True,
                    "message": "OK",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(
            data={"success": False, "message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        task.delete()
        notify_ws_clients(task, 'delete')
        return Response(
            data={
                "success": True,
                "message": "Task Deleted",
            },
            status=status.HTTP_204_NO_CONTENT
        )


def notify_ws_clients(task, action):
    channel_layer = get_channel_layer()
    task_data = TaskSerializer(task).data
    task_data['action'] = action
    async_to_sync(channel_layer.group_send)(
        "tasks",
        {
            'type': 'task_message',
            'message': task_data
        }
    )
