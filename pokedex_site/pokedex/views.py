import json

from django.http import HttpResponse
from .models import Pokemon


def index(request):
    result_set = Pokemon.objects.values('code', 'name', 'description').all()
    data = json.dumps(list(result_set))
    return HttpResponse(data, content_type='application/json')
