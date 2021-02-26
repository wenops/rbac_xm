import json


from django.core.exceptions import ImproperlyConfigured
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.http import Http404
from django.shortcuts import HttpResponse



from .mixin import LoginRequiredMixin
from apps.custom import SandboxCreateView,SandboxUpdateView,BreadcrumbMixin

from .models import Menu


class MenuCreateView(SandboxCreateView):
    model = Menu
    fields = '__all__'
    # extra_context = dict(menu_all=Menu.objects.all())

    def get_context_data(self, **kwargs):
        kwargs['menu_all'] = Menu.objects.all()
        return super().get_context_data(**kwargs)


class MenuListView(LoginRequiredMixin,BreadcrumbMixin,ListView):
    model = Menu
    context_object_name = 'menu_all'
    #ListView中属性template_name_suffix = '_list'

class MenuUpdateView(SandboxUpdateView):
    model = Menu #定义了视图中要显示的模型为Menu，效果等同于queryset = Menu.objects.all()
    fields = '__all__'
    template_name_suffix = '_update'#自动生成模板名称时使用的后缀，默认是'_form'，第12节就是使用的默认值，这里设置为'_update'，所以在创建模板时，必须命名为：'menu_update.html'
    # success_url = '/system/rbac/menu' #添加成功后的跳转页面
    # extra_context = dict(menu_all=Menu.objects.all())

    # def get_object(self,queryset=None):
    #     if queryset is None:
    #         queryset = self.get_queryset()
    #     if 'id' in self.request.GET and self.request.GET['id']:
    #         queryset = queryset.filter(id=int(self.request.GET['id']))
    #     elif 'id' in self.request.POST and self.request.POST['id']:
    #         queryset = queryset.filter(id=int(self.request.POST['id']))
    #     else:
    #         raise AttributeError("Generic detail view %s must be called with id. "
    #                              % self.__class__.__name__)
    #
    #     try:
    #         obj = queryset.get()
    #     except queryset.model.DoesNotExist:
    #         raise Http404("No %(verbose_name)s found matching the query" %
    #                       {'verbose_name': queryset.model._meta.verbose_name})
    #
    #     return obj
    #
    # def post(self,request,*args,**kwargs):
    #
    #     self.object = self.get_object()
    #     res = dict(result=False)
    #     form = self.get_form()
    #     if form.is_valid():
    #         form.save()
    #         res['result'] = True
    #     return HttpResponse(json.dumps(res),content_type='application/json').
    def get_context_data(self, **kwargs):
        kwargs['menu_all'] = Menu.objects.all()
        return super().get_context_data(**kwargs)






