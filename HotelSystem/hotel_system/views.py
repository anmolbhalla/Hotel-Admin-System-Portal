from django.shortcuts import render
import datetime
from datetime import timedelta
from django.shortcuts import HttpResponse

from hotel_system.models import Hotel

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