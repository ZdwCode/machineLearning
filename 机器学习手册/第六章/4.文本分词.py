"""使用自然语言工具集NLTk"""
from nltk.tokenize import word_tokenize,sent_tokenize
# import nltk
# nltk.download('punkt')
string = 'The science of today is the technology of tomorrow!'
# 使用文本分词器
result = word_tokenize(string)
print(result)

# 还可以分句子
string = 'The science of today is the technology of tomorrow!I love you,baby. Thank you!'
# 使用文本分词器
result = sent_tokenize(string)
print(result)
