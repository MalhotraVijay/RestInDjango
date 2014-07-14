from django.shortcuts import render

from django.http import HttpResponse
from baseutil import base
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
    if request.method == "GET":
        dictData = {'name':'john',
                    'age':'33'}
        jsonResponse = base.jsonResponse(dictData)
        print jsonResponse
        response = HttpResponse()
        response.write(jsonResponse)
        response['Access-Control-Allow-Origin'] = "http://localhost"
        return response
