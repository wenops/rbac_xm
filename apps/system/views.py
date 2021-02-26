from django.shortcuts import render
from django.views.generic.base import View,TemplateView


from .mixin import LoginRequiredMixin
from custom import BreadcrumbMixin


class SystemView(LoginRequiredMixin,BreadcrumbMixin,TemplateView):

    template_name = 'system/system_index.html'

