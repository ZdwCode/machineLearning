import unicodedata
import sys

# 创建文本
text_data = ['Hi!!!!! I, Love ,This. Song....',
             '10000% Agree! !!!#Love IT',
             'Right?!!!?']

# 创建一个标点字典
punctuation = dict.fromkeys(i for i in range(sys.maxunicode)
              if unicodedata.category(chr(i)).startswith('P')) # 是标点的字符全部取出来,fromkeys(key,[,values]) values 默认为none
print(punctuation)
# 移除每个字符串中的标点
result = [string.translate(punctuation) for string in text_data]
print(result)