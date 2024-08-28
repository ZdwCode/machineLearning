"""使用NLTK的stopwords删除很常见但包含信息量很少的单词"""
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
string = 'The science of today is the technology of tomorrow!'
# 使用文本分词器
result = word_tokenize(string)

stop_words = stopwords.words('english')
result_without_stopwords = [word for word in result if word not in stop_words]
print(result_without_stopwords)
stop_words_english = stopwords.words('english')
stop_words_chinese = stopwords.words('chinese')
print(len(stop_words_english),stop_words_english)
print(len(stop_words_chinese),stop_words_chinese)