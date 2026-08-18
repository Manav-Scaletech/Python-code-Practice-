from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    room_group_name = "chat_room"

    async def connect(self):
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        await self.accept()
        await self.send(text_data="Connected to chat room")

    async def receive(self, text_data=None, bytes_data=None):
        message = text_data or ""
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": message,
            }
        )

    async def chat_message(self, event):
        await self.send(
            text_data=event["message"]
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )
