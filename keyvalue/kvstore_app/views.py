from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse

from .models import KeyValueStore
from django.utils import timezone
import json

from datetime import timedelta

def insert_key(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        key = data['key']
        value = data['value']
        ttl_duration  = timedelta(seconds = 30)
        expires_at = timezone.now() + ttl_duration
        try:
            KeyValueStore.objects.update_or_create(key = key, value = value, expires_at = expires_at)
            return JsonResponse({'message': 'Key inserted successfully'}, status = 201)
        except:
            return JsonResponse({'message': 'Key insertion unsuccessful'}, status = 400)

def get_key(request):
    if request.method == 'GET':
        key = request.GET.get('key')
        try:
            key_value = KeyValueStore.objects.get(key = key)
            if key_value.is_expired():
                return JsonResponse({'message': 'Key has expired'}, status = 400)
            else:
                return JsonResponse({'value': key_value.value}, status = 200)
        except:
            return JsonResponse({'message': 'Key not found'}, status = 404)

def delete_key(request):
    key = request.GET.get('key')
    try:
        key_value = KeyValueStore.objects.get(key = key)
        key_value.delete()
        return JsonResponse({'message': 'Key deleted successfully'}, status = 200)
    except:
        return JsonResponse({'message': 'Key not found'}, status = 404)
    