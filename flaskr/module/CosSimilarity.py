import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class CosSimilarity():
    def __init__(self, df_dic):
        tmp = []
        self.df = pd.DataFrame(df_dic)
        for a, b, c, d, e in zip(self.df['Price'],self.df['colorpower'],self.df['spread'],self.df['keep'], self.df['moisture']):
            tmp.append([a,b,c,d,e ])
        self.cosine_sim = cosine_similarity(tmp)
        self.indices = pd.Series(self.df.index, index=self.df['Color'])

    def get_recommendations(self, title):
        # 선택한 립스틱의 타이틀로부터 해당되는 인덱스를 받아옴
        idx = self.indices[title]

        # 모든 립스틱에 대해서 해당 립스틱과의 유사도를 구합니다.
        sim_scores = list(enumerate(self.cosine_sim[idx]))

        # 유사도에 따라 립스틱들을 정렬합니다.
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # 가장 유사한 7개의 립스틱을 받아옵니다.
        sim_scores = sim_scores[1:8]

        # 가장 유사한 7개의 립스틱의 인덱스를 받아옵니다.
        lib_indices = [i[0] for i in sim_scores]

        # 가장 유사한 7개의 립스틱의 제목을 리턴합니다.
        return self.df.iloc[lib_indices]
