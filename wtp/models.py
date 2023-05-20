from django.db import models
from user.models import WtpUser

class WtpBook(models.Model):
    book_num = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    book_topic = models.CharField(max_length=45)
    book_author = models.CharField(max_length=45)
    book_plot = models.TextField()
    book_price = models.CharField(max_length=45)
    book_img = models.TextField()

    class Meta:
        managed = True
        db_table = 'wtp_book'


class WtpBookmark(models.Model):
    bookmark_num = models.AutoField(primary_key=True)
    book_num = models.ForeignKey(WtpBook, models.DO_NOTHING, db_column='book_num')
    user_num = models.ForeignKey(WtpUser, models.DO_NOTHING, db_column='user_num')

    class Meta:
        managed = True
        db_table = 'wtp_bookmark'


class WtpEmo(models.Model):
    emo_num = models.AutoField(primary_key=True)
    emo_emotion = models.IntegerField()
    emo_gender = models.IntegerField()
    emo_age = models.IntegerField()
    book_num = models.ForeignKey(WtpBook, models.DO_NOTHING, db_column='book_num')

    class Meta:
        managed = True
        db_table = 'wtp_emo'

