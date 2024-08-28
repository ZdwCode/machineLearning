"""使用字符串处理方法：strip replace split来处理文本"""

text_data = ["   this is a test. You know! ",
             "Live Or Die. This is a question",
             "     Today Is The night.  "]

strip_whitespace = [string.strip() for string in text_data]
print(strip_whitespace)
# 删除句点
remove_periods = [string.replace(".","") for string in strip_whitespace]
print(remove_periods)

# 创建一个自定义转换方法
def capitalizer(string:str)->str:
    return string.upper()

result = [capitalizer(string) for string in remove_periods]
print(result)