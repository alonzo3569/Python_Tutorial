## Pandas & matplotlib

* Pandas Series plot :
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 随机生成1000个数据
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
 
# 为了方便观看效果, 我们累加这个数据
ans = data.cumsum()

# ans 為一 pandas object，可直接.plot()後用matplotlib的method .show()顯示
type(ans)
# > <class 'pandas.core.series.Series'>

# pandas 数据可以直接观看其可视化形式
ans.plot()

plt.show()
```


* Pandas Dataframe plot :
```python
data = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),   # 列 index
    columns=list("ABCD")     # 行 index
    )
ans = data.cumsum()
ans.plot()
plt.show()
```

* Scatter plot using dataframe :
```python
ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
# label : legend (圖例名稱)

# 将之下这个 data 画在上一个 ax 上面
data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)
# ax(scatter 參數) = ax(上一行的物件)
# ax : 將這一條線也畫到某個物件內，效果類似 hold on
plt.show()
```