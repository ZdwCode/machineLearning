import pandas as pd

dataframe = pd.read_csv('titanic.csv')
print(dataframe.head(5))

# 创建数据帧
dataframe = pd.DataFrame()
dataframe['name'] = ['jack','alice']
dataframe['age'] = [12,20]
dataframe['Driver'] = [True,False]
# 创建一行
new_person = pd.Series(['john',18,True],index=['name','age','Driver'])
dataframe = dataframe.append(new_person,ignore_index=True)
print(dataframe)

# 3.2 描述数据
dataframe = pd.read_csv('titanic.csv')
# 查看数据维度
print('查看数据维度：',dataframe.shape)
print('查看数据描述:',dataframe.describe())

# 3.3 浏览数据帧
dataframe = pd.read_csv('titanic.csv')
# iloc[行，列] 就是按照索引开选择数据 前提是索引必须存在
print(dataframe.iloc[0:2,:])#
# 如果索引不是数值而是标签时 loc比较常用 并且loc不一定非要存在
print(dataframe.loc[0:2,'PassengerId':'Pclass'])

# 3.4 利用条件语句来选择行
# 筛选出Pclass等于3的行
print(dataframe[dataframe['Pclass'] == 3])
print(dataframe[(dataframe['Pclass'] == 3)&(dataframe['Embarked'] == 'S')])
# 3.5 替换值
# dataframe = dataframe['Sex'].replace('female','Woman')
# print(dataframe)

# 3.6 重命名列 rename 传入的是重命名的字典 字典可以传递多个键值对
dataframe = dataframe.rename(columns={'Pclass':'Passernger Class','Sex':'Gender'})
print(dataframe.head(3))

# 3.7 计算最小值 最大值...
#(略)

# 3.8 查找唯一值 unique
print(dataframe['Gender'].unique())
print(dataframe['Gender'].value_counts())

# 3.9 处理缺失值 NaN not a number
print(dataframe[dataframe['Age'].isnull()])
# 用NaN来替换 需要导入numpy
import numpy as np
# dataframe['Gender'] = dataframe['Gender'].replace('male',np.nan)
# print(dataframe['Gender'])
# 3.10 删除一列drop
dataframe.drop('Age',axis=1)
# 可用数组传入多个列
dataframe.drop(['Age'],axis=1)

# 3.11 删除一行的方法 也可以使用drop方法将axis设为0
# 使用判断语句 挑选出一下不要的就行了
#dataframe = dataframe[dataframe['Gender'] == 'male'] # 相当于删除了某些行
print(dataframe)
# 使用drop按索引删除
dataframe = dataframe.drop([0, 4], axis=0)
print(dataframe)


# 3.12 删除重复行
#print(dataframe.drop_duplicates()) # 注意 drop_duplicates()只会删除完全一样的行
# 使用好在使用subset参数就能实现：删除某一列有重复的值
#print(dataframe.drop_duplicates(subset=["Gender"]))

# 3.13 根据 值 对行 分组
print(dataframe.groupby("Gender")['Age'].mean())
# 3.14 按照时间段对 行 进行分组
# 首先创建日期范围
# time_index = pd.date_range('2/6/2023', periods=10000)
# dataframe = pd.DataFrame(index=time_index)
# dataframe['Sale_Amount'] = np.random.randint(1,10,10000)
# print(dataframe)
# 按照两周求均值
# print(dataframe.resample('2w').mean())
# print(dataframe.resample('M',label='left').count())
# 3.15 遍历一个列的数据
# 就是个for循环
# 3.16 对某一列的所有元素应用某个函数
# 定义一个函数
def uppercase(x):
    return x.upper()

print(dataframe['Name'].apply(uppercase)[0:2])

# 2.18连接concatenate 和合并merge数据帧

