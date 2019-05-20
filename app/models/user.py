from django.db import models


class User(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)
    pw = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    cdate = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    udate = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'user'

    @staticmethod
    def get_user(id):
        return User.objects.filter(id=id).first()




