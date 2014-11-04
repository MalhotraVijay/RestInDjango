from django.shortcuts import render

from django.http import HttpResponse
from baseutil import base,appconfig
from django.contrib.auth.models import User
from django.core import serializers
from django.shortcuts import render_to_response

from django.template import RequestContext


def restGETHandler(request,id):
    ''' Rest handlers'''
    
    # For the GET method
    
    if request.method == "GET":
        # Handle {{user}}/{{id}}  [specific user]
        if id:
            if 0 == int(id):
                users = User.objects.all()
            else:
                users = User.objects.filter(id=id)
            
        return HttpResponse(base.getSearializedData(users))


    # For the POST method 
    if request.method == "POST":
        pass



def landingRestHandler(request):
    return render_to_response('landing_rest.html',context_instance= RequestContext(request))



def corsHandler(request):
    print request
    if request.method == "OPTIONS" or request.method == "GET":
        dictData = {'name':'john',
                    'age':'33'}
        jsonResponse = base.jsonResponse(dictData)
        print jsonResponse
        response = HttpResponse()
        response.write(jsonResponse)
        response['Access-Control-Allow-Origin'] = "http://localhost"
        response['Access-Control-Allow-Headers'] = "X-Requested-With"
        return response


def sendDataToGoogle(request):
    
    if request.method == "OPTIONS" or request.method == "GET":

       
        dataObject = request.GET
    
        totalLength =  request.GET['objLength']
        for i in range(0,int(totalLength)):
            obj = {}
            name = 'dataObject['+str(i)+'][url]'
            obj['index'] = str(i)
            obj['url'] = str(dataObject[name])
            print obj 
            sendFileInfo(obj)
        response = HttpResponse()
        #response.write(jsonResponse)
        response['Access-Control-Allow-Origin'] = "http://localhost"
        response['Access-Control-Allow-Headers'] = "X-Requested-With"
        return response


def sendFileInfo(obj):
    import gdata.spreadsheet.service

    client = gdata.spreadsheet.service.SpreadsheetsService() 
    client.debug = True # feel free to toggle this 
    client.email = appconfig.gappConfig['username'] 
    client.password = appconfig.gappConfig['password']
    client.source = 'some description' 
    client.ProgrammaticLogin()


    spreadsheet_key = '13tu3U-pd6isQQq8VDTv8JOFd4AnJWuhd9APYnCuzgTo'

    worksheet_id = 'od6'

    row = { "id": "1", "title": "second" }

    print 'done'
    client.InsertRow(obj, spreadsheet_key, worksheet_id)





