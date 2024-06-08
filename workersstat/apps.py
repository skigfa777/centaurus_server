from django.apps import AppConfig
from django.core.signals import request_finished



class WorkersstatConfig(AppConfig):
  default_auto_field = 'django.db.models.BigAutoField'
  name = 'workersstat'
  verbose_name = 'Мониторинг активности'

  def ready(self):
    from . import signals

