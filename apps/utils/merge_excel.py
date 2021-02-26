

import pandas as pd
import openpyxl


file1 = 'G:\\常用保存文件\\tmp\\暂估数据-2019年1.16版本V2.xlsx'#sheet  暂估明细
file2 = 'G:\\常用保存文件\\tmp\\1-12月发票明细表-兴森销售.xlsx'#sheet  1-6月
file3 = 'G:\\常用保存文件\\tmp\\1-12月发票明细表-科技.xlsx'#sheet  1-12明细表
file4 = 'G:\\常用保存文件\\tmp\\1-12月发票明细表-股份.xlsx'#sheet  ＯＭＳ明细
file5 = 'G:\\常用保存文件\\tmp\\暂估收入明细-12月.xlsx'#sheet  明细表

res_total = pd.read_excel(file1,engine='openpyxl',sheet_name='暂估明细',
                          usecols=['账套','客户代码','客户名称',
                          '应收账期','是否军品','发货单号','订单编号','生产型号',
                          '统计单价（统计）','发货数量（统计）','不含税销售金额（折人民币）',
                          '暂估应收','月份'])

#
res_xs = pd.read_excel(file2,engine='openpyxl',sheet_name='1-6月',
                       usecols=['帐套名称','来源单据编号','生产型号','增值税额','开票金额(含税)']).drop_duplicates(
                        subset=['帐套名称','来源单据编号','生产型号','增值税额','开票金额(含税)'],keep='last')

res_kj = pd.read_excel(file3,engine='openpyxl',sheet_name='1-12明细表',
                       usecols=['帐套名称','来源单据编号','生产型号','增值税额','开票金额(含税)']).drop_duplicates(
                        subset=['帐套名称','来源单据编号','生产型号','增值税额','开票金额(含税)'],keep='last')

res_gf = pd.read_excel(file4,engine='openpyxl',sheet_name='gf',
                       usecols=['帐套名称','来源单据编号','生产型号','增值税额','开票金额(含税)']).drop_duplicates(
                        subset=['帐套名称','来源单据编号','生产型号','增值税额','开票金额(含税)'],keep='last')
res_mx = pd.read_excel(file5,engine='openpyxl',sheet_name='明细表',
                       usecols=['帐套名称','发货单号','生产型号','已签收未开票不含税(人民币)']).drop_duplicates(
                        subset=['帐套名称','发货单号','生产型号','已签收未开票不含税(人民币)'],keep='last')
#pd.merge(left=n,right=s,on="number",how="left")

# res_left = pd.merge(left=res_total,right=res_gf,
#                     left_on=['发货单号','生产型号'],
#                     right_on=['来源单据编号','生产型号'],
#                     how="left",suffixes=('_x','_y'),
#                     indicator=True)
#
# res_left.to_csv('total_gf.csv',index=False)
lst = [res_xs,res_kj,res_gf,res_mx]
res_hj = pd.concat(lst)
res_hj.to_csv('res_hj.csv')