## Numpy array 合併

* Vertical stack & Horizontal stack :

```python
import numpy as np
A = np.array([1,1,1])
B = np.array([2,2,2])
         
C = np.vstack((A,B))    # vertical stack
D = np.hstack((A,B))    # horizontal stack
print(C)
"""
[[1,1,1]
 [2,2,2]]
"""
print(C.shape)
# (2,3)
```

* Newaxis : 使非矩陣之物件，產生維度(m*n)

```python
A = np.array([1,1,1]) # A = np.array([[1,1,1]]) 如此宣告shape即為(1,3)
print(A.T)       # 仍為[1,1,1]
print(A.shape)   # (3,)
# 理論上應為(1,3)
# 但輸出卻為(3,)
# 表示A并不是矩阵的属性 需使用newaxis轉換為矩陣

print(A[np.newaxis,:])
# [[1 1 1]]

print(A[np.newaxis,:].shape)
# (1,3)

print(A[:,np.newaxis])
"""
[[1]
[1]
[1]]
"""

print(A[:,np.newaxis].shape)
# (3,1)
```

* Concatenate : 合併多個array
```python
import numpy as np

import numpy as np
A = np.array([1,1,1])[:,np.newaxis] # A.shape => (3,1)
B = np.array([2,2,2])[:,np.newaxis] # B.shape => (3,1)
         

C = np.concatenate((A,B,B,A),axis=0) # 0 : 矩陣縱向合併

print(C)
"""
array([[1],
       [1],
       [1],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2],
       [1],
       [1],
       [1]])
"""

D = np.concatenate((A,B,B,A),axis=1) # 1 : 矩陣橫向合併

print(D)
"""
array([[1, 2, 2, 1],
       [1, 2, 2, 1],
       [1, 2, 2, 1]])
"""
```
