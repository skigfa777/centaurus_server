import os
from django.db import models
from django.conf import settings
from datetime import date



class Session(models.Model):
  domain = models.CharField(max_length=200, null=True, blank=True)
  machine = models.CharField(max_length=200, null=True, blank=True)
  ip = models.CharField(max_length=100, null=True, blank=True)
  user = models.CharField(max_length=200, null=True, blank=True)
  start_activity = models.DateTimeField("start activity", null=True, blank=True)
  last_activity = models.DateTimeField("last activity", null=True, blank=True)
  get_screenshots = models.BooleanField(default=False, 
    verbose_name="Получить скриншот рабочего стола (обновите эту страницу ~ через 30 сек после сохранения правки)")

  class Meta:
    verbose_name = 'Сессия/сотрудник'
    verbose_name_plural = 'Сессии сотрудников'


def get_upload_path(instance, filename):
  session_id = instance.session_id
  today = date.today()
  path = f'screenshots/{instance.session_id}/{today}/'
  # if not os.path.exists(path):
  #   os.makedirs(path)
  return os.path.join(path, filename)

class Screenshot(models.Model):
  session = models.ForeignKey(Session, related_name='screenshots', on_delete=models.CASCADE)
  screenshot = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
  created = models.DateTimeField("created", null=True, blank=True)

  def ImageFieldFile(self):
    return self.screenshot

