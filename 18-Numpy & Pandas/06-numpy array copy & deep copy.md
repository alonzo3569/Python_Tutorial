## Numpy array Copy & Deep copy

* numpy array 性質 : 使用"="附值
```python
import numpy as np

a = np.arange(4)
# array([0, 1, 2, 3])

b = a
c = a
d = b

# 改變 a[0] 數值
a[0] = 11
print(a)
# array([11,  1,  2,  3])

# 改變 a[0] 數值， 但b,c,d的[0]index數值也都跟著改變
# 代表使用"="附值numpy array，代表的是完全相同的array
b is a  # True
c is a  # True
d is a  # True

# 更改d的值，a、b、c也会改变
d[1:3] = [22, 33]   # array([11, 22, 33,  3])
print(a)            # array([11, 22, 33,  3])
print(b)            # array([11, 22, 33,  3])
print(c)            # array([11, 22, 33,  3])
```  

* numpy array deep copy : copy()
```python
b = a.copy()    # deep copy
print(b)        # array([11, 22, 33,  3])
a[3] = 44
print(a)        # array([11, 22, 33, 44])
print(b)        # array([11, 22, 33,  3])
# 改變 a，b不會跟著改變
```