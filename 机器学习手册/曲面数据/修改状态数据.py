import pandas as pd

data = pd.read_excel(r'G:\mogodar_case\case39\i_copy.xlsx', header=None)
print(data.shape)
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if data.iloc[i,j] == 1:
            pass
        elif data.iloc[i,j] == 2:
            pass
        elif data.iloc[i,j] == 11:
            data.iloc[i,j] = 3
        elif data.iloc[i,j] == 12:
            data.iloc[i,j] = 3
        elif data.iloc[i,j] == 20:
            data.iloc[i,j] = 4
        elif data.iloc[i,j] == 30:
            data.iloc[i,j] = 5
        elif data.iloc[i,j] == 40:
            data.iloc[i,j] = 6
        elif data.iloc[i,j] == 50:
            data.iloc[i,j] = 7
        elif data.iloc[i,j] == 45:
            data.iloc[i,j] = None
        else:
            print(data.iloc[i,j])

data.to_excel('state.xlsx', index=False,columns=None,header=False)