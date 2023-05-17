import subprocess

from django.contrib import messages
from django.shortcuts import render
from Warehouse.models import Item
from django.db.models import Count
# Create your views here.
def product_1(request):

    data = {}
    balcony_list = list(Item.objects.values('balcony_num').annotate(value=Count('balcony_num')))
    bedroom_list = list(Item.objects.values('bedroom_num').annotate(value=Count('bedroom_num')))
    hall_list = list(Item.objects.values('hall_num').annotate(value=Count('hall_num')))
    toilet_list = list(Item.objects.values('toilet_num').annotate(value=Count('toilet_num')))
    facing_list =  list(Item.objects.values('facing').annotate(value=Count('facing')))
    floor_height_list =  list(Item.objects.values('floor_height').annotate(value=Count('floor_height')))
    renting_type_list =  list(Item.objects.values('renting_type').annotate(value=Count('renting_type')))
    has_elevator_list = list(Item.objects.values('has_elevator').annotate(value=Count('has_elevator')))
    for item in has_elevator_list:
        if item['has_elevator']== True:
            item['has_elevator']="有"
        else:
            item['has_elevator']="无"
    data['balcony_list'] = balcony_list
    data['bedroom_list'] = bedroom_list
    data['hall_list'] = hall_list
    data['toilet_list'] = toilet_list
    data['facing_list'] = facing_list
    data['floor_height_list'] = floor_height_list
    data['renting_type_list'] = renting_type_list
    data['has_elevator_list'] = has_elevator_list
    refresh = request.POST.get('refresh',1)
    if(refresh!=1):
        messages.success(request, '开始重新爬取数据，请耐心等待！')
        Item.objects.all().delete()
        subprocess.Popen('scrapy crawl maitian')
    return render(request,'product_1.html',data)
def product_2(request):
    data ={}
    area_list = list(Item.objects.values('area','price'))
    floor_list = list(Item.objects.values('floor','price'))
    for item in area_list:
        item['area'] = float(item['area'])
        item['price'] = float(item['price'])
    for item in floor_list:
        item['floor'] = float(item['floor'])
        item['price'] = float(item['price'])
    data['area_list'] = area_list
    data['floor_list'] = floor_list
    refresh = request.POST.get('refresh', 1)
    if (refresh != 1):
        messages.success(request, '开始重新爬取数据，请耐心等待！')
        Item.objects.all().delete()
        subprocess.Popen('scrapy crawl maitian')
    return render(request,'product_2.html',data)
def product_3(request):
    data={}
    area_list = list(Item.objects.values('area'))
    area_dict = []
    for item in area_list:
        area_dict.append(float(item['area']))
    data['area_dict'] = area_dict
    balcony_list = list(Item.objects.values('balcony_num'))
    balcony_dict = []
    for item in balcony_list:
        balcony_dict.append(int(item['balcony_num']))
    data['balcony_dict']=balcony_dict
    bedroom_list = list(Item.objects.values('bedroom_num'))
    bedroom_dict = []
    for item in bedroom_list:
        bedroom_dict.append(int(item['bedroom_num']))
    data['bedroom_dict']= bedroom_dict
    hall_list = list(Item.objects.values('hall_num'))
    hall_dict = []
    for item in hall_list:
        hall_dict.append(int(item['hall_num']))
    data['hall_dict'] = hall_dict
    toilet_list = list(Item.objects.values('toilet_num'))
    toilet_dict = []
    for item in toilet_list:
        toilet_dict.append(int(item['toilet_num']))
    data['toilet_dict'] = toilet_dict
    floor_list = list(Item.objects.values('floor'))
    floor_dict = []
    for item in floor_list:
        floor_dict.append(int(item['floor']))
    data['floor_dict'] = floor_dict
    price_list = list(Item.objects.values('price'))
    price_dict = []
    for item in price_list:
        price_dict.append(float(item['price']/1000))
    data['price_dict'] = price_dict
    refresh = request.POST.get('refresh', 1)
    if (refresh != 1):
        messages.success(request, '开始重新爬取数据，请耐心等待！')
        Item.objects.all().delete()
        subprocess.Popen('scrapy crawl maitian')
    return render(request,'product_3.html',data)
def product_4(request):
    data ={}
    total_num = int(Item.objects.all().count())
    price_0 = float(Item.objects.filter(price__lte=1000).count()) / total_num * 100
    price_1 = float(Item.objects.filter(price__lte=2000).count())/total_num*100
    price_2 = float(Item.objects.filter(price__lte=3000).count())/total_num*100
    price_3 = float(Item.objects.filter(price__lte=4000).count())/total_num*100
    price_4 = float(Item.objects.filter(price__lte=5000).count())/total_num*100
    price_5 = float(Item.objects.filter(price__lte=6000).count())/total_num*100
    price_6 = float(Item.objects.filter(price__lte=7000).count())/total_num*100
    price_7 = float(Item.objects.filter(price__lte=8000).count()) / total_num * 100
    price_8 = float(Item.objects.filter(price__lte=9000).count()) / total_num * 100
    price_9 = float(Item.objects.filter(price__lte=10000).count()) / total_num * 100
    data['price'] = [price_0,price_1,price_2,price_3,price_4,price_5,price_6,price_7,price_8,price_9]
    data['tag'] = ['1000以下','2000以下','3000以下','4000以下','5000以下','6000以下','7000以下','8000以下','9000以下','10000以下']
    refresh = request.POST.get('refresh', 1)
    if (refresh != 1):
        messages.success(request, '开始重新爬取数据，请耐心等待！')
        Item.objects.all().delete()
        subprocess.Popen('scrapy crawl maitian')
    return render(request,'product_4.html',data)
def product_5(request):
    data={}
    tags = list(Item.objects.values('tags'))
    brt = 0
    mashangruzhu=0
    suishikanfang=0
    linjinditie=0
    duwei=0
    duyang=0
    shoucichuzu=0
    xuexiaofujin=0
    for item in tags:
        if '近BRT' in item['tags']:
            brt=brt+1
        if '马上入住' in item['tags']:
            mashangruzhu = mashangruzhu+1
        if '随时看房' in item['tags']:
            suishikanfang = suishikanfang+1
        if '独卫' in item['tags']:
            duwei = duwei+1
        if '独阳'in item['tags']:
            duyang = duyang+1
        if '临近地铁' in item['tags']:
            linjinditie = linjinditie+1
        if '首次出租' in item['tags']:
            shoucichuzu = shoucichuzu+1
        if '学校附近' in item['tags']:
            xuexiaofujin = xuexiaofujin+1
    data['brt']=brt
    data['mashangruzhu']=mashangruzhu
    data['suishikanfang']=suishikanfang
    data['linjinditie']=linjinditie
    data['duwei']=duwei
    data['duyang']=duyang
    data['shoucichuzu']=shoucichuzu
    data['xuexiaofujin']=xuexiaofujin
    refresh = request.POST.get('refresh', 1)
    if (refresh != 1):
        messages.success(request, '开始重新爬取数据，请耐心等待！')
        Item.objects.all().delete()
        subprocess.Popen('scrapy crawl maitian')
    return render(request,'product_5.html',data)