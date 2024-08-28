import numpy as np
from scipy import sparse
# 一行向量
vector_row = np.array([1,2,3])
# 一列向量
vector_column = np.array([[1],[2],[3]])
print(vector_row)
print(vector_column)
# 创建一个矩阵
matrix = np.array([[0, 0],
                   [0, 1],
                   [3, 0]])
print(matrix)

# 创建一个压缩的稀疏行
matrix_sparse = sparse.csr_matrix(matrix)
print(matrix_sparse)  # 压缩后只保存矩阵的非零值

matrix_large = np.array([[0,0,0,0,0,0,1,0],
                        [0,0,1,0,0,0,1,0],
                        [0,2,0,3,0,0,1,0]])
print('压缩前的矩阵：',matrix_large)
# 使用crs来压缩
matrix_large_sparse = sparse.csr_matrix(matrix_large)
print('压缩后的矩阵',matrix_large_sparse)

# 1.4 选择元素
# 创建一个行向量
vector = np.array([0,1,2,0,0,0])
# 创建一个矩阵
matrix = np.array([[0,1,2],
                   [2,3,4],
                   [4,5,6]])
print(vector[2],matrix[0,1])
print('选取向量的所有元素(使用切片操作):',vector[:])
print('选取矩阵的所有元素(使用切片操作[:,:]):\n',matrix[0:2,:2])
# 1.5展示一个矩阵的属性
matrix = np.array([[1,2,3,4],
                   [2,3,4,5],
                   [3,4,5,6],
                   [4,5,6,7]])

print('查看矩阵的行和列：',matrix.shape)
print('查看矩阵的数量；',matrix.size)
print('查看矩阵的维度：',matrix.ndim)

# 1.6对矩阵的内容进行批量的运算
# 创建一个函数来准备应用
add_100 = lambda i:i+100
# 创建向量化函数
vectorized_add_100 = np.vectorize(add_100)
# 应用这个向量化函数
matrix = vectorized_add_100(matrix)
print(matrix)
# 1.7 找到最大值和最小值
print('矩阵的最大值:',np.max(matrix))
print('矩阵的最小值：',np.min(matrix))
print('矩阵每一列的最大值:',np.max(matrix,axis=0))
print('矩阵每一行的最小值：',np.min(matrix,axis=1))

# 1.8 计算平均值,方差,标准差
print('均值',np.mean(matrix))
print('方差',np.var(matrix))
print('标准差',np.std(matrix))

# 1.9 矩阵变形 reshape 先平铺再一行一行的摆 必须要求新矩阵和原矩阵的size相同 -1可以不用指定了
matrix = np.array([[1,2,3,4],
                   [2,3,4,5],
                   [3,4,5,6]])
print(matrix.shape)
print(matrix)
matrix = matrix.reshape(4,3)
print(matrix)
# 1.10 转置向量和矩阵 但是转置之后的shape是不变的
matrix = matrix.T
print(matrix)


# 1.11 展开一个矩阵
print('使用flatten展开',matrix.flatten())
print('使用reshape展开',matrix.reshape(1,-1)) # 但是不会改变矩阵的维度

# 1.12 计算矩阵的秩matrix_rank 封装在线性代数方法里
matrix = np.array([[1,1,1],
                   [1,1,10],
                   [1,1,15]
                   ])

print(np.linalg.matrix_rank(matrix))
# 1.13 计算行列式linalg.det()
print(np.linalg.det(matrix))
# 1.14 获取矩阵的对角线元素 offset来做偏移
print(np.diagonal(matrix,offset=1))
# 1.15 计算矩阵的迹
print(matrix.trace())
# 1.16 计算矩阵的特征向量和特征值 使用线性函数eig
matrix = np.array([[1,-1,3],
                   [1,1,6],
                   [3,8,9]])
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(eigenvalues)
print(eigenvectors)

# 1.17 计算点积
vector_a = np.array([1,2,4])
vector_b = np.array([2,3,4])
result = np.dot(vector_a,vector_b)
print(result)

# 1.18 矩阵相加或相减
matrix_a = np.array([[1,1,1],
                     [2,2,2],
                     [3,3,3]])

matrix_b = np.array([[1,1,1],
                     [2,2,2],
                     [3,3,3]])
# 相加
matrix_c = np.add(matrix_a,matrix_b)
# 相减
matrix_d = np.subtract(matrix_a,matrix_b)
print(matrix_c)
print(matrix_d)

# 1.19两个矩阵相乘
matrix_a = np.array([[1,1],[1,2]])
matrix_b = np.array([[1,3],[1,2]])
matrix_c = np.dot(matrix_a,matrix_b)
print(matrix_c)

# 1.20 计算矩阵的逆矩阵
matrix = np.array([[1,4],
                   [2,5]])
if matrix.ndim == matrix.shape[0]:
    # 满秩才有逆矩阵
    print(np.linalg.inv(matrix))

# 1.21 生成随机数
np.random.seed(0)
# 生成0-1的随机数
results = np.random.random(4)
print(results)
# 生成0-11之间的整数
results = np.random.randint(0,11,3)
print(results)
# 从均值是0，标准差是1的正态分布中取三个数
results = np.random.normal(0.0,1.0,3)
print(results)