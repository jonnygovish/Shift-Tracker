from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.
class Employee_profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  phonenumber = models.IntegerField(blank=True,null=True)
  position = models.CharField(max_length =30)
  profile_pic = models.ImageField(upload_to = 'prof_pic/', blank =True, null = True)
  date_of_birth = models.DateTimeField(null = True, blank = True)


  @receiver(post_save, sender = User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Employee_profile.objects.create(user=instance)

  @receiver(post_save, sender = User)
  def save_user_profile(sender,instance, **kwargs):
    instance.employee_profile.save()

  def __str__(self):
    return self.user.username


class Shift(models.Model):
  SHIFT =(
    ('Morning shift','Morning Shift'),
    ('Evening shift','Evening Shift'),
    ('Night shift','Night Shift'),
  )
  shift_name = models.CharField(max_length =20, choices = SHIFT, blank=True, null=True)
  employee = models.ForeignKey('Employee_profile', on_delete=models.CASCADE,related_name='shifts', blank = True, null = True)
  DAYS = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thusrday'),
    ('Friday', 'Friday'),
  )
  day_of_the_week = models.CharField(max_length=20, choices=DAYS, blank=True, null=True)
  start_time = models.TimeField()
  end_time = models.TimeField()
  activated = models.BooleanField(verbose_name='Activate', default=False)
  sale_status = models.BooleanField(verbose_name='Activate sale', default=False)


  def __str__(self):
    return self.day_of_the_week

  @classmethod
  def get_shift(cls):
    shifts = cls.objects.all()
    return shifts