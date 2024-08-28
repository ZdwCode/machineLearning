"""使用相关矩阵检查是否存在较高相关性的特征，如果存在，则删除其中的一个"""

import pandas as pd
import numpy as np

# 创建一个矩阵
features = np.array([[1,1,1],
                     [2,2,0],
                     [3,3,1],
                     [4,4,0],
                     [5,5,1],
                     [6,6,0],
                     [7,7,1],
                     [8,7,0],
                     [9,8,1],])

# 将特征矩阵转化为dataframe
dataframe = pd.DataFrame(features)

# 创建相关矩阵
corr_matrix = dataframe.corr().abs()
print(corr_matrix)

# 选择相关矩阵的上三角矩阵
upper = corr_matrix.where(np)