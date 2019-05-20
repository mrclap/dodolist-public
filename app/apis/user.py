from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from app.models.user import User