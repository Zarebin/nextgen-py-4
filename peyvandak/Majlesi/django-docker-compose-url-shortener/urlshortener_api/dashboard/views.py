from django.http import JsonResponse
from django.shortcuts import render
from api.models import  VisitUrl, Shortener
from django.core import serializers

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})


def pivot_data(request):
    dataset = Shortener.objects.all()
    #dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
