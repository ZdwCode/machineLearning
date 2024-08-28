from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize,sent_tokenize
# import nltk
# nltk.download('punkt')
string = 'The science of today is the technology of tomorrow!'
# 使用文本分词器
result = word_tokenize(string)
# 创建词干转换器
porter = PorterStemmer()
result_porter = [porter.stem(word) for word in result]
print(result_porter)