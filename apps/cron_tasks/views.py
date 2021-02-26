from django.shortcuts import render
from django.views.generic import View,TemplateView
# Create your views here.

class Cron_TaskView(TemplateView):
    template_name = 'cron_tasks/cron_task_index.html'