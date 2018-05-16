import datetime
from django.shortcuts import HttpResponse
from hotel_system.models import Hotel
from datetime import datetime,timedelta
import calendar
from django.template import loader
from django.shortcuts import redirect

def index (request):

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

    return HttpResponse('Success')

def values (request):

    room = request.POST['room_type']
    from_date = request.POST['from']
    to_date =  request.POST['to']
    days = list(request.POST.getlist('filter[]'))
    price = request.POST['price']
    avail = request.POST['avail']


    # answer = Hotel.objects.filter(date__range=(from_date,to_date) , day__in=days)

    if room == 'Double_Room':

        Hotel.objects.filter(date__range=(from_date, to_date), day__in=days).update(price_double = price , avail_double = avail)
        return redirect(index)

    else :

        Hotel.objects.filter(date__range=(from_date, to_date), day__in=days).update(price_single=price,avail_single=avail)
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
    return HttpResponse(template.render(context, request))


def content (request):

    innerhtml = request.POST.get('name')
    idelement = request.POST.get('new')
    headers = request.POST.get('heads')

    if (headers == 'price_single'):

        Hotel.objects.filter(id = idelement).update(price_single = innerhtml)

    elif (headers == 'avail_single'):

        Hotel.objects.filter(id=idelement).update(avail_single=innerhtml)

    elif (headers == 'price_double'):

        Hotel.objects.filter(id=idelement).update(price_double=innerhtml)

    elif (headers == 'avail_double'):

        Hotel.objects.filter(id=idelement).update(avail_double=innerhtml)

    return HttpResponse(idelement,headers)

