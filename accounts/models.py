# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# # 
# # 
# class Profile(models.Model):
#     '''
#     This model extends the default django user model to
#     add an extra field to know whether a user is vip or not
#     '''
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     vip = models.BooleanField(default=False, blank=False)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     '''
#     This signal automatically creates a Profile object and assigns a 1 to 1
#     relationship to the User when a new User object is created
#     '''
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()