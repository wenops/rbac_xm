import json

from django.views.generic import CreateView
from django.shortcuts import HttpResponse

from .mixin import LoginRequiredMixin
from .models import Menu


class MenuCreateView(LoginRequiredMixin,CreateView):
    '''
    model 指定了模型 Menu
    fields 设置为all 将Menu模型所有字段都映射到ModelForm
    success_url 定义数据添加成功后跳转到的页面
    get_template_names(self)：获取模板信息，如果没有指定template_name，则会根据规则推断出模板为："system/menu_form.html"，其中system来自模型的应用程序名称，menu是Memu模型的名称小写，_form是从template_name_suffix属性中获取的，当然我们也可以通过这个属性指定自己想要的名称，需要注意的是，在创建模板的时候一定要符合这个规则。
    form_class：使用自定义form作为要实例化的form类，使用form_class时候，fields放在form类中定义，不可再放到视图中定义
    get_form_class: 检索要实例化的表单类。 如果提供form_class，那么将使用该类。 否则，将使用与queryset或model关联的模型实例化ModelForm，上面代码中是通过Menu模型实例化的ModelForm
    '''
    model = Menu
    fields = '__all__'
    success_url = '/system/rbac/menu/create'

    def post(self,request,*args,**kwargs):
        res = dict(result=False)
        form = self.get_form()
        if form.is_valid():
            form.save()
            res['result'] = True
        return HttpResponse(json.dumps(res),content_type='application/json')
