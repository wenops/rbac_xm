import requests
import json

url = """http://wxpusher.zjiecode.com/api/send/message"""
appToken = "AT_dQHJApnfwmpHykKFyri2mcmtUX9hGGLg"

#推送消息测试
content = {}
summary =""
contentType=3
uids=['UID_RWyDL5NLRnVx4yiRQf7YKL2tFuce']

data = {
    "appToken":appToken,
  "content":content,
  "summary":summary,#消息摘要，显示在微信聊天页面或者模版消息卡片上，限制长度100，可以不传，不传默认截取content前面的内容。
  "contentType":contentType,#内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown
  "topicIds":[ #发送目标的topicId，是一个数组！！！，也就是群发，使用uids单发的时候， 可以不传。
      ],
  "uids":uids,#发送目标的UID，是一个数组。注意uids和topicIds可以同时填写，也可以只填写一个。
  "url":"" #原文链接，可选参数
}




tq_res = requests.get("http://www.weather.com.cn/data/sk/101200101.html")

res_xq = json.loads(tq_res.text.encode("raw_unicode_escape").decode("utf-8"))["weatherinfo"]

content = """### 武汉今日天
> 今天:
>    {} ℃
>    {}
""".format(res_xq["temp"],res_xq["WD"])
# print(content)

import urllib
def qingyunke(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(msg))
    html = requests.get(url)
    return html.json()["content"]
msg = '食谱'
print("原话>>", msg)
res = qingyunke(msg)
print("青云客>>", res)

data["content"] = str(res).replace('{br}','')
res = requests.post(url,data=json.dumps(data),headers={'Content-Type':'application/json'})

