from .models import Company, Appointment
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Company)
def create_appointment(sender, instance, created, **kwargs):
    if created:
        Appointment.objects.create(user=instance.user, company=instance)