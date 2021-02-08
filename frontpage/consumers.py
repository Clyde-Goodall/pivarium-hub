from channels.generic.websocket import AsyncWebsocketConsumer
from pivarium.models import Station, StationData, Sensor
from asgiref.sync import sync_to_async
import json
from channels.consumer import SyncConsumer
from django.http import JsonResponse

#Where all data from each station goes. 
#Registers new station if hex mac addr. isn't found in model, does nothing and continues to submit data otherwise
class StationConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        #self.check_if_exists
        #print(self.scope)

        await self.accept()

    async def disconnect(self, close_code):
        
        pass
    
    #called when data comes in
    async def receive(self, text_data):
        
        text_data = json.loads(text_data)
        response = JsonResponse([text_data], safe=False)
        print(text_data['station_id'])
        await self.check_if_exists(text_data)

        await self.submit_measurement(text_data)

    #station checker
    @sync_to_async
    def check_if_exists(self, data):
        print("Checking incoming data")
        if(len(Station.objects.filter(sid=data['station_id']))  > 0):
            print("familiar station data received")
        else:
            Station(sid=data['station_id'], title="Raspberry Pi", desc="Data channel source").save()
            print("New station added")
        #adds a new entry for a sensor if a new type is added.
        #for client side to know what units and title to give data points.
        if(len(Sensor.objects.filter(sensor_type=data['sensor_type'])) == 0):
            Sensor(sensor_type=data['sensor_type'], unit=data['unit']).save()
            print("New sensor type added")

    #submits to station data mode
    @sync_to_async
    def submit_measurement(self, data):
        StationData(sid=data['station_id'], value=data['data'], timestamp=data['timestamp'], sensor_type=data['sensor_type'])
        print("data tick added")

    # @sync_to_async
    # def send_history(self):
        

#sends chart data over to client. Sends first X amount of entries if it is a fresh connection
#will send new updates at X interval according to client parameters, stored in client setings model,
#agnostic of update interval from pi. Will consider adding "real-time" option, but not the default.
class DataSyncConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        #print(self.scope)

        await self.accept()

    async def disconnect(self, close_code):
        
        pass

