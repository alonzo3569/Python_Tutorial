## Numpy array index

* 二維index :
```python
A = np.arange(3,15).reshape((3,4))
"""
array([[ 3,  4,  5,  6]
       [ 7,  8,  9, 10]
       [11, 12, 13, 14]])
"""
         
print(A[2])         
# [11 12 13 14]

print(A[1][1])      # 8
print(A[1, 1])      # 8

print(A[1, 1:3])    # [8 9]
print(A[2,:])       # 列2所有元素 [11, 12, 13, 14]
print(A[:,1])       # 行1所有元素 [4, 8, 12]

```

* 利用for迴圈:
```python
# 逐列疊代
for row in A:
    print(row)

# 透過轉置實現逐行疊代
for column in A.T:
    print(column)

# 若想在2維矩陣逐"元素"疊代,可利用flat
# flat 可將多維矩陣轉換為1維
# flat 為一generator 返回物件 <numpy.flatiter object>
# flatten 返回一為矩陣

print(A.flat)      # <numpy.flatiter object at 0x101a2d000>
print(A.flatten()) # [ 3,  4,  5,  6,.....14]
for item in A.flat
    print(item)
```
