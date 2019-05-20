from django.db import models
from app.models.user import User


class Category(models.Model):
    user = models.ForeignKey(on_delete=models.CASCADE, to=User)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)   # tinyint(-128~127)
    cdate = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    udate = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'category'

    @staticmethod
    def get_category(id):
        return Category.objects.filter(id=id).first()

    @staticmethod
    def get_category_by_user_id(user_id):
        return Category.objects.filter(user__id=user_id).filter(is_default=1).first()



