import datetime
from django.shortcuts import HttpResponse
from hotel_system.models import Hotel
from datetime import datetime,timedelta
import calendar
from django.template import loader
from django.shortcuts import redirect
import logging

logger = logging.getLogger('hotel_logger')

def index (request):

    logger.error('Homepage')
    Date = datetime.now().date()
    month = Date.strftime('%h')
    year_present = Date.strftime('%Y')
    Calendar = Hotel.objects.filter(month=month, year=year_present)
    display_month = Hotel.objects.values('month_year').distinct()
    template = loader.get_template('hotel_system/main.html')
    context = {

        'Calendar': Calendar,
        'display_month': display_month,
        'month_ch': month,
    }
    return HttpResponse(template.render(context, request))



def dbupdate(request):
    logger.error('Db populate')
    Hotel.objects.all().delete()
    Date = datetime.now().date() - timedelta(days=1)
    if Date.day > 25:
        Date += datetime.timedelta(7)
    Date = Date.replace(day=1)
    year = int(Date.strftime('%Y')) + 1
    month_int = datetime.now().month
    b = calendar.monthrange(year, month_int)
    value = 366 + b[1]
    for i in range(1, value):
        day = Date.strftime("%A")
        month = Date.strftime('%h')
        year = Date.strftime('%Y')
        month_year = month + '-' + year
        print(Date, day, month, year)
        insert_data = Hotel(id=i, year=year, month_year=month_year, date=Date, day=day, month=month, avail_single=10,
                            price_single=1000, avail_double=5, price_double=2000)
        insert_data.save()
        EndDate = Date + timedelta(days=1)
        Date = EndDate

    return redirect(index)

def values (request):
    room = request.POST['room_type']
    from_date = request.POST['from']
    to_date =  request.POST['to']
    days = list(request.POST.getlist('filter[]'))
    price = request.POST['price']
    avail = request.POST['avail']



    if room == 'Double_Room':
        logger.error('User selected Double room')
        Hotel.objects.filter(date__range=(from_date, to_date), day__in=days).update(price_double = price , avail_double = avail)
        logger.error('Db update for double Room')
        return redirect(index)

    else :
        Hotel.objects.filter(date__range=(from_date, to_date), day__in=days).update(price_single=price,avail_single=avail)
        logger.error('Db update for single Room')
        return redirect(index)

def month (request):

    month_raw=request.POST['month']
    month_compare=month_raw
    Calendar = Hotel.objects.filter(month_year=month_raw)
    display_month=Hotel.objects.values('month_year').distinct()
    template = loader.get_template('hotel_system/main.html')
    context = {
        'Calendar': Calendar,
        'display_month':display_month,
        'month_compare':month_compare,
    }
    logger.error('User changed a month for calender view')
    return HttpResponse(template.render(context, request))


def content (request):

    innerhtml = request.POST.get('name')
    idelement = request.POST.get('new')
    headers = request.POST.get('heads')

    if (headers == 'price_single'):
        Hotel.objects.filter(id = idelement).update(price_single = innerhtml)
        logger.error('User edited single room price from calender')

    elif (headers == 'avail_single'):
        logger.error('User edited single room availability from calender')
        Hotel.objects.filter(id=idelement).update(avail_single=innerhtml)

    elif (headers == 'price_double'):
        logger.error('User edited double room price from calender')
        Hotel.objects.filter(id=idelement).update(price_double=innerhtml)

    elif (headers == 'avail_double'):
        logger.error('User edited double room availability from calender')
        Hotel.objects.filter(id=idelement).update(avail_double=innerhtml)

    return HttpResponse(idelement,headers)

