from django.db import models
import json

class DataPiece(models.Model):
  data = models.JSONField()

  def __str__(self):
    return json.dumps(self.data)