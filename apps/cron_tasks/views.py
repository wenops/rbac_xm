from django.shortcuts import render
from django.views.generic.base import View,TemplateView
from django.views.generic import ListView

from .models import Cron_Task
from system.mixin import LoginRequiredMixin
# Create your views here.

class Cron_TaskView(TemplateView):
    template_name = 'cron_tasks/cron_task_index.html'

class All_Cron_TaskView(LoginRequiredMixin,ListView):
    model = Cron_Task
    context_object_name = 'cron_task_all'
    # ListView中属性template_name_suffix = '_list'


