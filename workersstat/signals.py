from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from .models import Screenshot

@receiver(pre_delete, sender=Screenshot)
def screenshot_model_delete(sender, instance, **kwargs):
  if instance.screenshot.name:
    instance.screenshot.delete(False)

