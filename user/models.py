from django.db import models

# Create your models here.
class WtpUser(models.Model):
    user_id = models.CharField(max_length=45)
    user_password = models.CharField(max_length=128)
    user_email = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'wtp_user'
