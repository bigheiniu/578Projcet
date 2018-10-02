# calculte similarity of topic
import numpy as np
import gensim
import gensim.corpora as corpora
'''
:topic1 (topic_index, array[(word, word_p)])

'''
def TopicSimilarity(topic1,topic2):
    words1 = dict((word,pro) for word, pro in topic1[1])
    words2 = dict((word,pro) for word, pro in topic2[1])
    sumValue = 0.0
    for word, pro in words1:
        value = np.square(pro)
        value = np.power(value - np.square(words2.get(word, 0.0)), 2)
        sumValue = sumValue + value

    wordOnlyInTopic2 = set(words2.keys()) - set(words1.keys())
    if(len(wordOnlyInTopic2) > 0):
        for word in wordOnlyInTopic2:
            sumValue = sumValue + words2.get(word)
    return sumValue



'''
Use kmeans to cluster topic
'''
def TopicCluster(topicWordPro):# build word_corups for all topic
    word = [[word[0] for word in topic[1]] for topic in topicWordPro]
    id2word = corpora.Dictionary(word)
    token2id = id2word.token2id
    vector_len = len(token2id)
    feature = []
    topicIndex = []
    for topic in topicWordPro:
        topicIndex.append(topic[0])
        wordPro = topic[1]
        vector = np.zeros(vector_len)
        for word,pro in wordPro:
            vector[token2id.get(word)] = pro
        feature.append(vector)

    from sklearn.cluster import KMeans
    features = np.array(feature)
    topicIndex = np.array(feature)
    #manualy set the cluster of
    cluster = len(topicWordPro) / 5
    kmeans = KMeans(n_clusters=5, random_state=0).fit_predict(X=features)
    result = [(group, topic_index) for group, topic_index in zip(kmeans,topicIndex)]


