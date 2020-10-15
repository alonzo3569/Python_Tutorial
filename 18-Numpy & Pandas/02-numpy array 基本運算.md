## Numpy array 基本運算

* 加減乘除、次方 :
```python
import numpy as np
a=np.array([10,20,30,40])   # array([10, 20, 30, 40])
b=np.arange(4)              # array([0, 1, 2, 3])

c=a-b  
# array([10, 19, 28, 37])

c=a+b  
# array([10, 21, 32, 43])

c=a*b  
# array([  0,  20,  60, 120])

c=b**2  
# array([0, 1, 4, 9])

```

* np method : use on np object
  * sin()
  ```python
  c=10*np.sin(a)  
  # array([-5.44021111,  9.12945251, -9.88031624,  7.4511316 ])
  ```
  * sum(), min(), max()
  ```python
  import numpy as np
  a=np.random.random((2,4))
  print(a)
  # array([[ 0.94692159,  0.20821798,  0.35339414,  0.2805278 ],
  #        [ 0.04836775,  0.04023552,  0.44091941,  0.21665268]])
  
  # 整個矩陣各個元素總和、最大值、最小值
  np.sum(a)   # 4.4043622002745959
  np.min(a)   # 0.23651223533671784
  np.max(a)   # 0.90438450240606416

  print("a =",a)
  # a = [[ 0.23651224  0.41900661  0.84869417  0.46456022]
  #      [ 0.60771087  0.9043845   0.36603285  0.55746074]]
  
  # 分列行計算總和、最大值、最小值
  print("sum =",np.sum(a,axis=1))     #  axis=0 : 行元素相加 (default) 
  # sum = [ 1.96877324  2.43558896]   #  axis=1 : 列元素相加

  print("min =",np.min(a,axis=0))
  # min = [ 0.23651224  0.41900661  0.36603285  0.46456022]

  print("max =",np.max(a,axis=1))
  # max = [ 0.84869417  0.9043845 ]
  ```


* 搭配print()進行邏輯判斷 :
```python
print(b<3)  
# array([ True,  True,  True, False], dtype=bool)
```


* 標準矩陣乘法 : Numpy中的矩阵乘法分为两种
1. 对应元素相乘 (a*b)
2. 标准的矩阵乘法运算，即对应行乘对应列得到相应元素 (dot)

```python
a=np.array([[1,1],[0,1]])
b=np.arange(4).reshape((2,2))
c_dot = np.dot(a,b)
# array([[2, 4],
#       [2, 3]])

#除此之外还有另外的一种关于dot的表示方法，即：
c_dot_2 = a.dot(b)
# array([[2, 4],
#       [2, 3]])
```

* 返回矩阵中最小元素和最大元素的index
```python
import numpy as np
A = np.arange(2,14).reshape((3,4)) 

# array([[ 2, 3, 4, 5]
#        [ 6, 7, 8, 9]
#        [10,11,12,13]])
         
print(np.argmin(A))    # 0
print(np.argmax(A))    # 11
```
* 平均數、中位數
```python
# 平均數
print(np.mean(A))                # 7.5
print(np.mean(A, axis=0))        # axis=0 : 行元素相加 (default); 1 : 列元素
print(A.mean())                  # 7.5
# 中位數
print(A.median())                # 7.5
```

* 累積總和函式
```python
print(np.cumsum(A)) 

# [2 5 9 14 20 27 35 44 54 65 77 90]
```

* 每一行中后一项与前一项之差
```python
# A = array([[ 2, 3, 4, 5]
#            [ 6, 7, 8, 9]
#            [10,11,12,13]])

print(np.diff(A)) 
   
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]
```

* 返回矩陣中非零值的index，輸出為列index與行index矩陣
```python
print(np.nonzero(A))    

# (array([0,0,0,0,1,1,1,1,2,2,2,2]),array([0,1,2,3,0,1,2,3,0,1,2,3]))
```

* 排序 (逐列排序)
```python
import numpy as np
A = np.arange(14,2, -1).reshape((3,4)) 

# array([[14, 13, 12, 11],
#       [10,  9,  8,  7],
#       [ 6,  5,  4,  3]])

print(np.sort(A))    

# array([[11,12,13,14]
#        [ 7, 8, 9,10]
#        [ 3, 4, 5, 6]])
```

* 矩陣轉置
```python
print(np.transpose(A))    
print(A.T)

# array([[14,10, 6]
#        [13, 9, 5]
#        [12, 8, 4]
#        [11, 7, 3]])
# array([[14,10, 6]
#        [13, 9, 5]
#        [12, 8, 4]
#        [11, 7, 3]])
```

* Clipping : clip(Array,Array_min,Array_max)
```python
print(A)
# array([[14,13,12,11]
#        [10, 9, 8, 7]
#        [ 6, 5, 4, 3]])

print(np.clip(A,5,9))    
# array([[ 9, 9, 9, 9]
#        [ 9, 9, 8, 7]
#        [ 6, 5, 5, 5]])
```




