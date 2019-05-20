from django.db import models
from app.models.user import User
from app.models.category import Category

class Todo(models.Model):
    user = models.ForeignKey(on_delete=models.CASCADE, to=User)
    title = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)   # tinyint(-128~127)
    completed = models.IntegerField(blank=True, null=True)  # tinyint(-128~127)
    category = models.ForeignKey(on_delete=models.CASCADE, to=Category)
    cdate = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    udate = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'todo'

    @staticmethod
    def get_todo(id):
        return Todo.objects.filter(id=id).first()

    @staticmethod
    def get_todos(user_id):
        return Todo.objects.filter(user_id=user_id)

    @staticmethod
    def get_todos_by_user_id_and_category_id(user_id, category_id):
        return Todo.objects.filter(user_id=user_id).filter(category_id=category_id)

    @staticmethod
    def get_todos_by_order(order):
        # [1, 3, 5, 2, 7] => 1, 3, 5, 2, 7
        order_str = ', '.join(str(x) for x in order)


        # raw query
        query = "SELECT * FROM todo WHERE completed = 0 "
        if order:
            query += " AND  id in (" + order_str + ") ORDER BY FIELD(id, " + order_str + ")"

        print(query)
        return Todo.objects.raw(query)
