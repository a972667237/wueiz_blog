#coding:utf-8
from django.shortcuts import render,HttpResponse
import json
from .models import article,tag
import re
# Create your views here.

def index(requests):
    art_list = article.objects.all().order_by('-id')[:4]
    tag_list = tag.objects.all()
    recommond_list = article.objects.filter(recommond=True)
    if(len(article.objects.all())>4):
        next = True
    else:
        next = True
    return render(requests,'blog.html',{'art_list':art_list,'tag_list':tag_list,'recommond_list':recommond_list,'next':next,'pre':False})

def get_article(requests,art_id):
    art = article.objects.get(id=art_id)
    return render(requests,'show.html',{
        'art_title':art.title,'art_date':art.date,'art_author':art.author.all(),'art_tag':art.tag.all(),'art_content':art.content,
        })

def get_tag(requests,t_id):
    art_list = article.objects.filter(tag__id=t_id)
    tag_list = tag.objects.all()
    recommond_list = article.objects.filter(recommond=True)

    return render(requests, 'blog.html', {
        'art_list': art_list, 'tag_list': tag_list, 'recommond_list': recommond_list, 'next': False, 'pre': False
        })

def get_more(requests):
    href = requests.GET.get('href')
    url_id = re.findall(r'[0-9]+',href)[0]
    url_id = int(url_id) - 3
    info = article.objects.filter(id__lt=url_id).order_by('-id')
    my_list = []
    for i in info:
        my_dict = {}
        my_dict['title'] = i.title
        my_dict['author'] = i.author.all()[0].name
        my_dict['content'] = i.article_info + u" <a href='/article/%s' class='article_all' >查看全文</a> " %(str(i.id))
        my_dict['id'] = i.id
        my_dict['dates'] = u'时间：' + i.date.__str__()

        my_list.append(my_dict)
    return HttpResponse(json.dumps(my_list), content_type='application/json')

def get_pre(requests):
    href = requests.GET.get('href')
    url_id = re.findall(r'[0-9]+',href)[0]
    url_id = int(url_id)
    info = article.objects.filter(id__gt=url_id).filter(id__lt=url_id+5).order_by('-id')
    biggest = len(article.objects.all())
    my_list = []
    for i in info:
        my_dict = {}
        my_dict['title'] = i.title
        my_dict['author'] = i.author.all()[0].name
        if (len(i.content) > 110):
            i.content = i.content[:101] + '...'
        my_dict['content'] = i.article_info + u" <a href='/article/%s' class='article_all' >查看全文</a> " % (str(i.id))
        my_dict['biggest'] = biggest
        my_dict['id'] = i.id
        my_dict['dates'] = u'时间：' + i.date.__str__()

        my_list.append(my_dict)
    return HttpResponse(json.dumps(my_list), content_type='application/json')
