import pandas as pd
import numpy as np

#讀取檔案
data = pd.read_csv('student.csv')
print(data)
#存檔
data.to_pickle('student.pickle')

#concat 設定 axis=0 為直向合併
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
res = pd.concat([df1,df2,df3],axis=0)
print(res)

#ignore_index = True 可以忽略合併時舊的 index 欄位，改採用自動產生的 index
res = pd.concat([df1,df2,df3],axis=0, ignore_index=True)
print(res)

#concat 的 join 屬性有兩種模式 inner, outer(預設)
res = pd.concat([df1,df2])               # 這兩行程式是全等的
res = pd.concat([df1,df2], join='outer') # 這兩行程式是全等的
print(res)
res = pd.concat([df1,df2], join='inner', ignore_index=True)
print(res)

#concat 的 join_axes 功能，用於水平合併時可指定 index
res = pd.concat([df1,df2],axis=1, join_axes=[df1.index]) #設定左右合併 axis=1, join_axes 設定成按照 df1 的 index 來進行合併
print(res)

# 使用 DataFrame append 來合併資料，新增資料
# append 預設是往下加
res = df1.append(df2, ignore_index=True)
print(res)

# append 多個
df3 = pd.DataFrame(np.ones((3,4))*3, columns=['a','b','c','d'])
res = df1.append([df2,df3], ignore_index=True)
print(res)

# 直接 append 一組資料
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res = df1.append(s1, ignore_index=True)
print(res)

