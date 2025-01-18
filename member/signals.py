# members/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Member
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_member(sender, instance, **kwargs):
    instance.member.save()
