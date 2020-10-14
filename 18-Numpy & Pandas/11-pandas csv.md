## Pandas csv I/O

* Read csv file :
```python
import pandas as pd #加载模块

#读取csv
data = pd.read_csv('student.csv')

#打印出data
print(data) 
# 讀入後會自動加入在"列index"(從0開始編號)

```

* Output : 將矩陣存成 pickle 檔(pickle 用於記錄已經序列化的物件)
```python
data.to_pickle('student.pickle')
```