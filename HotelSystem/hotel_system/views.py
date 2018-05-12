from django.shortcuts import render
import datetime
from datetime import timedelta
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from hotel_system.models import Hotel
from django.core import serializers

def index (request):
    return render(request , 'hotel_system/main.html')


def dbupdate(request):
    Date = datetime.datetime.now().date() - timedelta(days=1)
    for i in range(1, 367):
        EndDate = Date + timedelta(days=1)
        Date = EndDate
        day = Date.strftime("%A")

        insert_data = Hotel(date = EndDate, day = day, avail_single = 10, price_single = 1000, avail_double = 5, price_double = 2000 )
        insert_data.save()


    return HttpResponse('Success')

def values (request):

    room = request.POST['room_type']
    from_date = request.POST['from']
    to_date =  request.POST['to']
    days = list(request.POST.getlist('filter[]'))
    price = request.POST['price']
    avail = request.POST['avail']

    answer = Hotel.objects.filter(day__in=days)
    return HttpResponse(answer)
    # return JsonResponse(serializers.serialize('json',answer),safe=False)
