from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class LocationConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "_location"
        self.room_group_name = "_location_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': '1'}))

    def receive(self, text_data):
        print(text_data)
        pass

    def disconnect(self, *args, **kwargs):
        print("[ DISCONNECTED ]")
        pass

    def send_loc(self, event):
        print("SEND LOC")
        self.send(text_data=event.get('value'))