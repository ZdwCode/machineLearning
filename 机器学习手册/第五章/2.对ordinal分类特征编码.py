import pandas as pd

# 使用pandas的replace方法传入一个字典，简单替换掉内容
dataframe = pd.DataFrame({"Score": ["Low", "Low", "Medium", "Medium", "High"]})

scale_mapper = {"Low": 1,
                "Medium": 2,
                "High": 3}

dataframe_result = dataframe["Score"].replace(scale_mapper)
print(dataframe_result)

dataframe = pd.DataFrame({"Score":["Low","Low","Medium","High","Barely More Than Medium"]})

scale_mapper = {"Low": 1,
                "Medium": 2,
                "Barely More Than Medium": 2.1,
                "High": 3}
dataframe_map = dataframe['Score'].replace(scale_mapper)
print(dataframe_map)
print()