import pandas as pd
import numpy as np

left = pd.DataFrame({
    'key':['K0','K1','K2','K3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']})

right = pd.DataFrame({
    'key':['K0','K1','K2','K3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']})

# merge by 一個 key
res = pd.merge(left,right, on='key') # 目標，基於 key 把 left 與 right 合併
print(res)

#merge by 多個 key
#inner 模式
# 目標，基於 key1, key2 把 left 與 right 合併
res = pd.merge(left,right, on=['key1','key2'])           # 這兩行效果一樣
res = pd.merge(left,right, on=['key1','key2'],how='inner')  # 這兩行效果一樣
                                                         # 使用 merge 同時合併 by 多個 key 預設為 how='inner' 模式
print(res)

#outer 模式
#使用 merge 同時合併 by 多個 key, how='outer' 模式
res = pd.merge(left,right, on=['key1','key2'],how='outer')
print(res)

#right 模式
# 使用 merge 同時合併 by 多個 key, how='right' 模式
res = pd.merge(left,right, on=['key1','key2'],how='right')
print(res)

#left 模式
# 使用 merge 同時合併 by 多個 key, how='left' 模式
res = pd.merge(left,right, on=['key1','key2'],how='left')
print(res)

#使用 indicator 顯示 merge 的 mode
# 使用 indicator 可以顯示 merge 的方式
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,3], 'col_right':[2,2,2]})
res = pd.merge(df1,df2, on='col1', how='outer',indicator=True)
print(res)

# 設定 indicator 欄位的名字
res = pd.merge(df1,df2, on='col1', how='outer',indicator='indicator_column')
print(res)

#merge 合併時，處理欄位名稱相同衝突，以 suffixes 區別
# 目前 age 欄位是重複的，我們為了要區別 boy 與 girl，必須要在新的合併表格中，為 age 欄位取新的名字
# 使用 suffixes 屬性即可辦到
boys = pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls = pd.DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})
res = pd.merge(boys,girls, on='k', suffixes=['_boy','_girl'], how='outer')
print(res)