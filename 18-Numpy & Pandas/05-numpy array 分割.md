## Numpy array 分割

* split :

```python
import numpy as np
A = np.arange(12).reshape((3, 4))
print(A)
"""
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
"""

# 縱向
print(np.split(A, 2, axis=1)) # axis = 1 縱向切割; 2:分成2組
"""
[array([[0, 1],
        [4, 5],
        [8, 9]]), 
 array([[ 2,  3],
        [ 6,  7],
        [10, 11]])]
"""

# 橫向
print(np.split(A, 3, axis=0)) # axis = 0 橫向切割; 3:分成3組

"""
[array([[0, 1, 2, 3]]),
 array([[4, 5, 6, 7]]),
 array([[ 8,  9, 10, 11]])]
"""
```
* split 無法進行不等量分割，會error
```python
# 沿用上述array A
print(np.split(A, 3, axis=1))

# ValueError: array split does not result in an equal division
```

* array_split : 不等量分割
```python
print(np.array_split(A, 3, axis=1)) # 縱向切割; 3:分成3組
"""
[array([[0, 1],
        [4, 5],
        [8, 9]]), 
 array([[ 2],
        [ 6],
        [10]]),
 array([[ 3],
        [ 7],
        [11]])]
"""
```


* vsplit & hsplit : 功能與split相同
```python
print(np.vsplit(A, 3)) 
#等于 print(np.split(A, 3, axis=0))
# 注意: vertical 是切"橫向"
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]


print(np.hsplit(A, 2)) 
#等于 print(np.split(A, 2, axis=1))
# 注意: horizontal 是切"縱向"
"""
[array([[0, 1],
       [4, 5],
       [8, 9]]),
 array([[ 2,  3],
        [ 6,  7],
        [10, 11]])]
"""
```