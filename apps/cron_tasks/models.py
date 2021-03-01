from django.db import models

# Create your models here.

#定时任务设置
class Cron_Task(models.Model):

    TASK_TYPE_CHOICES = (
        ('01','shell任务'),
        ('02','sql任务')
    )
    task_name = models.CharField(max_length=255,verbose_name="任务名称")
    task_type = models.CharField(max_length=255,verbose_name="任务类型",choices=TASK_TYPE_CHOICES,default='01')
    task_connent = models.TextField(null=True,blank=True,verbose_name="任务内容")
    task_para = models.CharField(max_length=255,verbose_name="任务参数")
    task_sta = models.CharField(max_length=255,verbose_name="任务状态",default='N')
    is_delete = models.CharField(max_length=255,verbose_name="是否删除",default='N')
    exe_host = models.ForeignKey("Server_Host",on_delete=models.SET_NULL, blank=True, null=True,verbose_name="执行机器")
    task_res = models.TextField(null=True,blank=True,verbose_name="任务结果")

    class Meta:
        verbose_name = "任务"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.task_name

#执行脚本的服务器
class Server_Host(models.Model):

    ip = models.CharField(max_length=255,verbose_name="IP地址")
    host_name = models.CharField(max_length=255,verbose_name="hostname")
    username = models.CharField(max_length=255,verbose_name="用户名")
    password = models.CharField(max_length=255,verbose_name="服务器密码")
    db_port = models.CharField(max_length=255,verbose_name="数据库端口")
    db_usrname = models.CharField(max_length=255,verbose_name="db用户名")
    db_password = models.CharField(max_length=255,verbose_name="db密码")
    db_database = models.CharField(max_length=255,verbose_name="数据库")
    db_schema = models.CharField(max_length=255,verbose_name="数据库模式")
    is_db = models.CharField(max_length=1,verbose_name="是否数据库服务器",default='否')

    class Meta:
        verbose_name = "服务器"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.host_name+self.ip