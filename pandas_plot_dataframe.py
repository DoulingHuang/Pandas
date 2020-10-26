import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DataFrame
data = pd.DataFrame(np.random.randn(1000,4),
                    index=np.arange(1000),
                    columns=list("ABCD"))
data = data.cumsum()
print(data.head(5))  # 印出前五個數據

data.plot()
plt.show()