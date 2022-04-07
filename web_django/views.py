import os
import json
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.template import loader

def index(request):
    template = loader.get_template('snakes.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)

def input_commands(request):
    cmd = request.GET.get('cmd', None)
    res = {}
    if cmd:
        with open('cmd.json', 'w', encoding='utf-8') as f:
            json.dump({'cmd': cmd}, f)
            res = {'stat': 'cmd_set'}
    else:
        with open('cmd.json', 'w', encoding='utf-8') as f:
            json.dump({'cmd': ''}, f)
            res = {'stat': 'cmd_unset'}
    return JsonResponse(res)

def output_commands(request):
    cmd = {}
    with open('cmd.json', 'r', encoding='utf-8') as f:
        cmd = json.loads(f.read())
        # print(cmd)
    return JsonResponse(cmd)
