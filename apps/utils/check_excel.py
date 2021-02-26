

import os
from pathlib import Path
import pandas as pd
import re
import openpyxl


def findAll(str):
    for root,ds,fs in os.walk(str):
        for f in fs :
            fullname = os.path.join(root,f)
            yield fullname,f


def replace_space_hans(s):
    res = re.findall('[\da-zA-Z\/_.-]+',str(s))
    return ''.join(res)



excles = findAll('H:\阿里云svn数据治理\GXCW财务管理数据子集\GXCW05教职工个人收入数据类\GXCW0501工资明细子类')
for fullname,filename in excles:

    path  = Path(fullname)
    parent_path = path.parent
    res_data = pd.read_excel(path)
    res_data['值空间'] = res_data['值空间'].apply(lambda x :replace_space_hans(str(x)))
    res_data['值空间'] = res_data['值空间'].apply(lambda x: str(x).replace('nan',''))

    writer = pd.ExcelWriter('H:\导入_tmp\{}'.format(filename))
    res_data.to_excel(writer,index=False)
    writer.save()

