from datetime import datetime
import json
import simplejson
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from news import models

def hello(request):
    return HttpResponse("54646546")

def userLogin(request):
    http_bad_response = HttpResponseBadRequest()
    http_bad_response['Content-Type'] = 'text/plain'
    if request.method == 'POST':
        usr = request.POST.get('username')
        pwd = request.POST.get('password')
        user = auth.authenticate(username=usr, password=pwd)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                http_response = HttpResponse()
                http_response['Content-Type'] = 'text/plain'
                http_response.status_code = 200
                http_response.content = 'login successful'
                return http_response

    http_bad_response.status_code = 423
    http_bad_response.content = 'login failed'
    return http_bad_response




@csrf_exempt
def userLogout(request):
    http_bad_response = HttpResponseBadRequest()
    http_bad_response['Content-Type'] = 'text/plain'
    if request.method == 'GET':
        auth.logout(request)
        if request.user.is_authenticated:
            http_bad_response.status_code = 423
            http_bad_response.content = 'logout failed'
            return http_bad_response
        else:
                http_response = HttpResponse()
                http_response['Content-Type'] = 'text/plain'
                http_response.status_code = 200
                http_response.content = 'logout successful'
                return http_response


@csrf_exempt
def poststory(request):
    http_bad_response = HttpResponseBadRequest()
    http_bad_response['Content-Type'] = 'text/plain'


    if request.method =='POST':
        if request.user.is_authenticated:
            req = simplejson.loads(request.body)
            hdl = req['headline']
            cat = req['category']
            reg = req['region']
            det = req['details']

            user = models.Author.objects.get(user=request.user)
            if cat == 'politics' or 'art' or 'technology' or 'trivial':
                if reg == 'UK' or 'European' or 'World':
                    models.Story.objects.create(headline=hdl, category=cat, region=reg, author=user, details=det)
                    http_response = HttpResponse()
                    http_response['Content-Type'] = 'text/plain'
                    http_response.status_code = 201
                    http_response.content = 'CREATED\n'
                    return http_response
                else:
                    http_bad_response.status_code = 503
                    http_bad_response.content = 'Wrong region\n'
                    return http_bad_response
            else:
                http_bad_response.status_code = 503
                http_bad_response.content = 'Wrong category\n'
                return http_bad_response
        else:
            http_bad_response.status_code = 503
            http_bad_response.content = 'Unauthenticated\n'
            return http_bad_response
    else:
        http_bad_response.content = 'Only GET requests are allowed for this resource\n'
        return http_bad_response



@csrf_exempt
def getstories(request):
    http_bad_response = HttpResponseBadRequest()
    http_bad_response['Content-Type'] = 'text/plain'

    if (request.method != 'GET'):
        http_bad_response.content = 'Only GET requests are allowed for this resource\n'
        return http_bad_response

    if request.method == 'GET':
        req = simplejson.loads(request.body)
        cat = req['story_cat']
        reg = req['story_region']
        dato = req['story_date']
        if cat == '*' and reg != '*' and dato != '*':
            dat = datetime.strptime(str(dato), '%d/%m/%Y')
            story_list = models.Story.objects.filter(region=reg, date_gt=dat.datetime_object.strftime('%Y-%m-%d'))
        if reg == '*' and cat != '*' and dato != '*':
            dat = datetime.strptime(str(dato), '%d/%m/%Y')
            story_list = models.Story.objects.filter(category=cat, date_gt=dat.datetime_object.strftime('%Y-%m-%d'))
        if dato == '*' and reg != '*' and cat != '*':
            story_list = models.Story.objects.filter(category=cat, region=reg)
        if dato == '*' and reg == '*' and cat != '*':
            story_list = models.Story.objects.filter(category=cat)
        if dato == '*' and reg != '*' and cat == '*':
            story_list = models.Story.objects.filter(region=reg)
        if dato != '*' and reg == '*' and cat == '*':
            dat = datetime.strptime(str(dato), '%d/%m/%Y')
            story_list = models.Story.objects.filter(date_gt=dat)
        if dato != '*' and reg != '*' and cat != '*':
            dat = datetime.strptime(str(dato), '%d/%m/%Y')
            story_list = models.Story.objects.filter(category=cat, region=reg, date_gt=dat.datetime_object.strftime('%Y-%m-%d'))
        if dato == '*' and reg == '*' and cat == '*':
            story_list = models.Story.objects.all().values('key', 'headline', 'category', 'region', 'author', 'date',
                                                           'details', )



    the_list = []
    for record in story_list:
        item = {'key': record['key'] , 'headline': record['headline'], 'story_cat': record['category'] , 'story_region': record['region'] ,
                'author': record['author'], 'story_date': str(record['date']), 'story_details': record['details']}
        the_list.append(item)

    payload = {'Stories':the_list}

    http_response = HttpResponse(json.dumps(payload))
    http_response['Content-Type']='application/json'
    http_response.status_code = 200
    http_response.reason_phtase = 'OK'
    return http_response


@csrf_exempt
def deletestory(request):
    http_bad_response = HttpResponseBadRequest()
    http_bad_response['Content-Type'] = 'text/plain'

    if (request.method != 'POST'):
        http_bad_response.content = 'Only POST requests are allowed for this resource\n'
        return http_bad_response


    if request.method =='POST':
        if request.user.is_authenticated:
            req = simplejson.loads(request.body)
            ki = req['story_key']

            # if the number of key is larger than the biggest key, we consider it correct.
            # Because the story of the key doesnt exit, which is 'deleted'. :)
            # So loop for counting the number of key is unnecessary. xD!
            models.Story.objects.filter(key=ki).delete()

            http_response = HttpResponse()
            http_response['Content-Type'] = 'text/plain'
            http_response.status_code = 201
            http_response.content = 'CREATED\n'
            return http_response













