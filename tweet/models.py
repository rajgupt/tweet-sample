from django.db import models
from django.utils import timezone
import datetime



# Create your models here.

##
# user handle just like twitter handle3
class handle(models.Model):
    value = models.TextField(max_length=100, unique=True)

    def __str__(self):
        return self.value
    
    
# simple tweet message to hold the message and its publish datetime
class message(models.Model):
    author = models.ForeignKey(handle)
    value = models.TextField(max_length=256)
    pub_date = models.DateTimeField('date published', auto_now_add='True')

    def __str__(self):
        return self.value
    def is_recent(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 1))
