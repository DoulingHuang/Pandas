import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# plot 的方法種類:
# 'bar', 'hist', 'box', 'kde', 'area', 'scatter', 'hexbin', 'pie'

# DataFrame
data = pd.DataFrame(np.random.randn(1000,4),
                    index=np.arange(1000),
                    columns=list("ABCD"))
data = data.cumsum()
print(data.head(5))  # 印出前五個數據

#使用Scatter
ax = data.plot.scatter(x='A',y='B', color='Red',label='Class 1')  # 取 A 欄位 B 欄位
data.plot.scatter(x='A', y='C', color='Green', label='Class 2', ax=ax) # 取 A 欄位 C 欄位

plt.show()