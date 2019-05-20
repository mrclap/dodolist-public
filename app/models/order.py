from django.db import models
from app.models.user import User
from app.models.category import Category

class Order(models.Model):
    user = models.ForeignKey(on_delete=models.CASCADE, to=User)
    category = models.ForeignKey(on_delete=models.CASCADE, to=Category)
    order_json = models.TextField()
    cdate = models.DateTimeField(blank=True, null=True, auto_now=True)

    # don't need udate
    # udate = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'order'

    @staticmethod
    def get_order(id):
        return Order.objects.filter(id=id).first()

    @staticmethod
    def get_order_by_user_id_and_category_id(user_id, category_id):
        return Order.objects.filter(user__id=user_id).filter(category__id=category_id).first()
