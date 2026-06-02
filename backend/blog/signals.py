from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, Comment

@receiver(post_save, sender=Post)
def add_welcome_comment(sender, instance, created, **kwargs):
    if created:
        Comment.objects.create(
            post=instance,
            text="Welcome! First comment.",
            author="Admin"
        )