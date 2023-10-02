
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from summary.function import transform_data

from summary.models import DelhiGeneration, DiscomDrawl, StateDrawl, Summary
from asgiref.sync import sync_to_async


class SummaryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'summary'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        """ Send message to WebSocket """
        data=await self.get_summary()
        await self.send(text_data=json.dumps({'data':data}))
    
    @sync_to_async
    def get_summary(self):
        summaryData= Summary.objects.all().values()
        print(summaryData)
        data= transform_data( list(summaryData))
        return {
            'type':'All',
            'summary':data,
            'discomDrawl':list(DiscomDrawl.objects.all().values()),
            'delhiGeneration':list(DelhiGeneration.objects.all().values()),
            'stateDrawl':list(StateDrawl.objects.all().values())
            
        }
    
    """ Receive message from WebSocket and print to console """
    async def receive(self, text_data):
        print(text_data)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'summary_message',
                'message': text_data
            }
        )
    

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def summary_message(self, event):
        data=await self.get_summary()
        await self.send(text_data=json.dumps({'data':data}))