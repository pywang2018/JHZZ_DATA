'''
circ_mv.py
描述：从tushare上抓取总资本，需安装tushare包
'''

import tushare as ts
import pandas as pd
import numpy as np
import datetime
ts.set_token('7e67081f05f2a9ea58ca60da55f6cb5f62fadd112bf0581d35c9def0')
pro=ts.pro_api()
TradingDay=pro.trade_cal(start_date='20090909',end_date='20190909',is_open='1')['cal_date']         #获取交易日期，可更改start_date，end_date更改日期
days=len(TradingDay)
OutCap=pd.DataFrame(TradingDay)
code=list(pro.daily_basic(ts_code='',trade_date='20190909',fileds='total_mv')['ts_code'])           #获取该交易日所有股票代码



for i in code:
    s = pd.DataFrame(pro.daily_basic(ts_code=i,start_date='20090909',end_date='20190909'))
    s=s[['trade_date', 'total_mv']]                                                                  #获取两列，第一列为日期，第二列为流通资本
    s.columns=['trade_date',i]                                                                       #将总资本列名改为股票代码
    OutCap=OutCap.merge(s,left_on='cal_date',right_on='trade_date',how='outer')
    OutCap=OutCap.drop(['trade_date'],axis=1)
    #print(OutCap)

OutCap.to_excel('total_mv.xlsx')                                                                      #导出至excel文件





