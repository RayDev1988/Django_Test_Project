from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage
from django.db import models

from django_site.settings import UPLOAD_DIR


class User(AbstractUser):
    approved = models.BooleanField(default=False)

    def is_approved(self):
        return self.approved

    def save(self, *args, **kwargs):
        super(User, self).save()
        Profile.objects.get_or_create(user=self)


class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M'
        FEMALE = 'F'
        COUPLE = 'C'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.jpg',
        verbose_name='Profile Image',
        max_length=255,
        storage=FileSystemStorage(location=UPLOAD_DIR))
    verification_image = models.ImageField(
        default=None,
        verbose_name='Verification Image',
        max_length=255,
        storage=FileSystemStorage(location=UPLOAD_DIR))
    his_age = models.CharField(max_length=2, null=True)
    her_age = models.CharField(max_length=2, null=True)
    bio = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=2, null=True)
    zip = models.CharField(max_length=5, null=True)
    interests = models.TextField(null=True)
    kik = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.MALE)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        return super(Profile, self).save(*args, **kwargs)


class Friend(models.Model):
    wait = "Wait"
    accept = "Accept"
    block = "Block"
    new_accept = "New_Accept"

    STATE_CHOICES = {
        (accept, "Accept"),
        (wait, "Wait"),
        (block, "Block"),
        (new_accept, "New_Accept")
    }

    sender_id = models.IntegerField()
    recipient_id = models.IntegerField()
    sender_firstName = models.CharField(max_length=35, default='')
    sender_lastName = models.CharField(max_length=35, default='')
    sender_image = models.ImageField(default='default.jpg')
    recipient_firstName = models.CharField(max_length=35, default='')
    recipient_lastName = models.CharField(max_length=35, default='')
    recipient_image = models.ImageField(default='default.jpg')
    state = models.CharField(max_length=35, choices=STATE_CHOICES, default=wait)

    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return '%s %s' % (self.sender_id, self.recipient_id)

    def save(self, *args, **kwargs):
        super(Friend, self).save(*args, **kwargs)


class VerificationCode(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    created_at = models.IntegerField()
    valid_until = models.IntegerField()
    phone = models.TextField(blank=True)
    phone_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'verification_code'
        verbose_name = 'Verification Code'
        verbose_name_plural = 'Verification Codes'
        get_latest_by = "created_at"
