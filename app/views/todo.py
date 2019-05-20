from rest_framework import viewsets
from django.shortcuts import render
from app.models.category import Category
from app.models.user import User
from app.models.order import Order
from app.models.todo import Todo

import json


def index(request):
    data_dict = dict()

    # temporary const
    user_id = 1
    qs_user = User.get_user(user_id)


    # get default category
    qs_category = Category.get_category_by_user_id(qs_user.id)

    # get order
    qs_order = Order.get_order_by_user_id_and_category_id(qs_user.id, qs_category.id)
    order_arr = []
    if qs_order:
        order = json.loads(qs_order.order_json)
        order_arr = order.get('order', [])

    todo_list = Todo.get_todos_by_order(order_arr)
    done_list = Todo.get_todos_by_user_id_and_category_id(qs_user.id, qs_category.id).filter(completed=1).order_by('udate')

    data_dict['user'] = qs_user
    data_dict['category'] = qs_category
    data_dict['order'] = qs_order
    data_dict['todo_list'] = todo_list
    data_dict['done_list'] = done_list



    # todo:
    # 1. 해당 사용자의 id를 받아서
    # 2. 해당 사용자의 카테고리도 받고
    # 3. 그 카테고리에 해당하는 모든 todolist를 받는데
    # 4. 이미 done이면 -> donelist
    # 5. 아직 todo이면 -> todolist
    # 6. order에서 순서 불러와서 그 순서대로 배치할 것

    return render(request, 'todo/list.html', data_dict)
