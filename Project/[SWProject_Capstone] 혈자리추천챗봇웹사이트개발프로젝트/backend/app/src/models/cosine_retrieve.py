import pandas as pd
import numpy as np
import pymysql
import json

from janome.tokenizer import Tokenizer
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

def connect_sql():

    connection = pymysql.connect(
        host = 'localhost' ,
        user = 'root' ,
        password = 'snskdhkskK123!' ,
        database = 'project_DB'
    )

    query = 'SELECT * FROM ORIG_MRDN_TB'
    df = pd.read_sql(query , connection)

    connection.close()

    return df

def calc_cosine(prompt):
    prompt = [prompt]
    data = connect_sql()
    tokenizer = Tokenizer()
    tokenized_data = [[token.surface for token in tokenizer.tokenize(sentence)] for sentence in prompt]
    w2v_model = Word2Vec(sentences = tokenized_data , vector_size = 100 , window = 5 , min_count = 1 ,
                         workers = 4)
    
    sentence_embeddings = [
        sum([w2v_model.wv[word] for word in sentence if word in w2v_model.wv]) / len(sentence)
        for sentence in tokenized_data
    ]

    similarity_scores = []
    for idx in range(data.shape[0]):
        similarity_score = cosine_similarity(sentence_embeddings , [json.loads(data.loc[idx , 'EMBEDDED_INFORMATION'])])
        similarity_scores.append((idx , similarity_score))
    return similarity_scores

def vector_retrieve(usr_input):
    TOP_K = 4
    similarity_data = calc_cosine(usr_input)
    sorted_similarity_data = sorted(similarity_data, reverse = True , key = lambda x : x[1][0][0])
    return sorted_similarity_data[:4] # 상위 4개를 반환한다.