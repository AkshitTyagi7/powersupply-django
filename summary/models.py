from django.db import models
from summary.function import transform_data
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# Create your models here.
class Summary(models.Model):
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        super(Summary, self).save(*args, **kwargs)
        summaryData= Summary.objects.all().values()
        print(summaryData)
        data= transform_data( list(summaryData))
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'summary',
            {
                'type': 'summary_message',
                'data': data
            }
        )

class DiscomDrawl(models.Model):
    id=models.AutoField(primary_key=True)
    discom=models.CharField(max_length=200)
    schedule=models.IntegerField()
    drawl=models.IntegerField()
    OD=models.IntegerField()

    def __str__(self):
        return str(self.discom) 
    def save(self, *args, **kwargs):
        super(DiscomDrawl, self).save(*args, **kwargs)
        discomDrawlData= DiscomDrawl.objects.all().values()
        print(discomDrawlData)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'summary',
            {
                'type': 'summary_message',
                'data': list(discomDrawlData)
            }
        )
    
class DelhiGeneration(models.Model):
    id=models.AutoField(primary_key=True)
    GENCO=models.CharField(max_length=200)
    schedule=models.IntegerField()
    actual=models.IntegerField()
    UI=models.IntegerField()
    def __str__(self):
        return self.GENCO
    def save(self, *args, **kwargs):
        super(DelhiGeneration, self).save(*args, **kwargs)
        delhiGenerationData= DelhiGeneration.objects.all().values()
        print(delhiGenerationData)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'summary',
            {
                'type': 'summary_message',
                'data': list(delhiGenerationData)
            }
        )

class StateDrawl(models.Model):
    id=models.AutoField(primary_key=True)
    state=models.CharField(max_length=200)
    schedule=models.IntegerField()
    drawl=models.IntegerField()
    OD=models.IntegerField()

    def __str__(self):
        return self.state
    def save(self, *args, **kwargs):
        super(StateDrawl, self).save(*args, **kwargs)
        stateDrawlData= StateDrawl.objects.all().values()
        print(stateDrawlData)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'summary',
            {
                'type': 'summary_message',
                'data': list(stateDrawlData)
            }
        )
    
