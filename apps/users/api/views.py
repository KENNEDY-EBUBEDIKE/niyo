from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.users.models import User
from .serializers import UserSerializer


class UserAPIView(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes_by_action = {
        'users': (IsAuthenticated,),
        'new_user': (AllowAny,),
        'edit_user': (IsAuthenticated,),
        'delete_user': (IsAuthenticated,),
    }

    def get_permissions(self):

        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [IsAuthenticated()]

    @action(detail=False, methods=['get'], url_path='me')
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False, methods=['get'], url_path='user')
    def users(self, request):

        if request.GET.get('user_id'):
            try:
                user = self.queryset.get(id=request.GET.get('user_id'))
                data = self.get_serializer(user).data
            except Exception as e:
                return Response(
                    data={
                        "success": False,
                        "message": e.args[0],
                    },
                    status=status.HTTP_200_OK
                )

        else:
            data = self.get_serializer(self.queryset, many=True).data

        return Response(
            data={
                "success": True,
                "message": "OK",
                "data": data
            },
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['post'], url_path='create')
    def new_user(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            try:
                user = User.objects.create_user(
                    username=request.data['username'],
                    email=request.data['email'],
                    password=request.data['password'],

                )
                user.save()

            except Exception as e:
                return Response(
                    data={
                        "success": False,
                        "error": e.args[0],
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response(
                data={"success": True, "message": "OK"},
                status=status.HTTP_201_CREATED
            )
        return Response(
            data={"success": False, "message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=False, methods=['patch'], url_path='edit')
    def edit_user(self, request):
        """
            Edits a user.
            :param request:
            :return:
        """
        try:
            user = request.user
            serializer = self.get_serializer(instance=user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(
                data={"success": True, "message": "User Data updated successfully"},
                status=status.HTTP_206_PARTIAL_CONTENT
            )
        except Exception as e:
            return Response(
                data={"success": False, "message": e.args[0]},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['delete'], url_path='delete')
    def delete_user(self, request):
        """
            Deletes the User
            :param request:
            :return:
        """
        try:
            user = request.user
            user.delete()
            return Response(
                data={"success": True, "message": "User Deleted successfully"},
                status=status.HTTP_204_NO_CONTENT
            )

        except Exception as e:
            return Response(
                data={"success": False, "message": e.args[0]},
                status=status.HTTP_400_BAD_REQUEST
            )
