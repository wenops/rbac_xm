import json


from django.shortcuts import render,HttpResponse
from django.views.generic.base import  View,TemplateView

from apps.custom import BreadcrumbMixin



from .mixin import LoginRequiredMixin

import pymysql

NAME = "rbac"
USER =  'root'
PASSWORD = "vb7X4HvdGlHdk5Uq"
HOST = "192.168.2.253"
PORT = 3306


class ManagerStu(LoginRequiredMixin,BreadcrumbMixin,TemplateView):

    template_name = 'system/manager_index.html'

class StudentView(LoginRequiredMixin,BreadcrumbMixin,TemplateView):

    template_name = 'system/manager.html'



class StudentListView(LoginRequiredMixin,View):

    def get(self,request):
        conn = pymysql.connect(database=NAME,port=PORT,user=USER,host=HOST,password=PASSWORD)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        sql ='select xh,xm,xb,mz,jg_sf from edu_app_xs_jbxx '
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        conn.close()
        # print(res)
        ret = dict(data=res)
        return HttpResponse(json.dumps(ret),content_type='application/json')


