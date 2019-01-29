from django.shortcuts import render
from booktest.models import *
from datetime import date
# Create your views here.

#查询所有图书并显示
def index(request):
    list = BookInfo.objects.all()
    return render(request, 'booktest/index.html', {'list':list})


#创建新图书
def create(request):
    book = BookInfo()
    book.btitle = '流星蝴蝶剑'
    book.bpub_date = date(1995, 12, 3)
    book.save()
    #转到首页
    return redirect('/')

#逻辑删除指定编号的图书
def delete(request, id):
    book = BookInfo.objects.get(id=int(id))
    book.delete()
    #转到首页
    return redirect('/')

def static_test(request):
    return render(request,'booktest/static_test.html')