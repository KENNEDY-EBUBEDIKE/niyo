import json
from channels.generic.websocket import AsyncWebsocketConsumer


class TasksConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

        self.group_name = 'tasks'

    async def connect(self):
        print("CONNECTING...")
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        print("CONNECTED")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)

        event = {
            "type": "task_message",
            "message": text_data_json,
        }

        await self.channel_layer.group_send(self.group_name, event)

    # Receive message from room group
    async def task_message(self, event):
        message = event["message"]
        # Send to WebSocket
        await self.send(text_data=json.dumps(message))

