from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltxt = request.GET['fulltxt']
    data=fulltxt.split()
    data_dic = {}
    for i in data:
        if i in data_dic:data_dic[i]+=1
        else:data_dic[i]=1
    data_dic = dict(sorted(data_dic.items(), key=lambda item: item[1]))
    return render(request, 'count.html', {'fulltxt':fulltxt, 'countt':len(data), 'data_dic':data_dic.items()})