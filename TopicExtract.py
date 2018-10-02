import numpy as np
import pandas as pd
import gc
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
from DataPreProcess import dataProcessForLDA

MODEL_PATH='./resource/mallet-2.0.6/bin/mallet'
filePath = ""
data = pd.read_csv(filePath)
result = dataProcessForLDA(data)
id2word,corpus = result.get("id2word")


topic_count = 20
ldamallet = gensim.models.wrappers.LdaMallet(MODEL_PATH, corpus, topic_count, id2word)

'''
:return topic_index: topic_index, text_index
'''
def TextTopic(ldaModel = ldamallet,corpus = corpus,texts = data):
    th = ldamallet[corpus]
    texts_topic = [sorted(row, key=lambda x:x[1], reverse=True) for row in th]
    # topic_index, text_index
    texts_topic = [f[0] for f in texts_topic]
    texts_topic = pd.DataFrame(texts_topic)
    texts_topic.columns = ["topic_index", "text_index"]
    texts_topic.text_index = texts_topic.index
    return texts_topic

'''
:return topic_index, time_interval, list(text_index), count

'''
def TopicTimeInvervalCount(data, texts_topic, interval):
    texts_topic['time'] = data['time']
    topic_time_count = texts_topic.set_index(pd.DatetimeIndex[texts_topic['time']])
    topic_time_interval = topic_time_count.groupby(["topic_index", pd.Grouper(freq= interval)],as_index=False).agg({'text_index':list})
    topic_time_interval['count'] = topic_time_interval['text_index'].apply(len)
    return topic_time_interval

'''
import ast
>>> df = pd.read_clipboard(header=None, quotechar='"', sep=',', 
...                   converters={1:ast.literal_eval})
use this way to load information from csv file
'''




def TopicIdKeyword():
    return (ldamallet.show_topics(formatted=False))