from django.core import serializers
import json

def jsonResponse(data):
    return json.dumps(data)


def getSearializedData(object):
    return serializers.serialize('json',object)
