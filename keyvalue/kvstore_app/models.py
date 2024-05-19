from django.db import models
import datetime
# Create your models here.

from django.db import models

class KeyValueStore(models.Model):
    key = models.CharField(max_length = 100)
    value = models.JSONField()
    expires_at = models.DateTimeField()

    def __str__(self):
        return self.key
    
    def is_expired(self):
        return datetime.datetime.now(datetime.timezone.utc) > self.expires_at

