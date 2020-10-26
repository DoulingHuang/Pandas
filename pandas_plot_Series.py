import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# plot data

# Series 線性數據
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum() # 做累加
data.plot()
plt.show()