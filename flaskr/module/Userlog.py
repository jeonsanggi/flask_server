import pickle
import pandas as pd
import numpy as np
import scipy as sp
import surprise
import warnings

class UserLog():
    def __init__(self):

        warnings.filterwarnings('ignore')
        with open('./LogDic.pickle', 'rb') as f:
            df_to_dict = pickle.load(f)
        # print("----------Let's dictionary----------")
        cos_set = set()
        self.name_list = []
        for user_key in df_to_dict:
            self.name_list.append(user_key)

            for cos_key in df_to_dict[user_key]:
                cos_set.add(cos_key)

        self.cos_list = list(cos_set)

        rating_dic = {
            'Nickname':[],
            'ProductIdx' : [],
            'rating' : []
        }

        for name_key in df_to_dict:
            for cos_key in df_to_dict[name_key]:
                a1 = self.name_list.index(name_key)

                a2 = self.cos_list.index(cos_key)
                a3 = df_to_dict[name_key][cos_key]

                rating_dic['Nickname'].append(a1)
                rating_dic['ProductIdx'].append(a2)
                rating_dic['rating'].append(a3)

        df = pd.DataFrame(rating_dic)

        reader = surprise.Reader(rating_scale=(1,5))

        col_list = ['Nickname','ProductIdx','rating']
        self.data = surprise.Dataset.load_from_df(df[col_list], reader)
        # print("----------Let's training----------")
        trainset = self.data.build_full_trainset()
        option = {'name': 'pearson'}
        self.algo = surprise.KNNBasic(sim_options=option)
        self.algo.fit(trainset)

    def recommand(self, who):
        recommand = list()
        # print("-----name_list in recommand-----:", self.name_list)
        index = self.name_list.index(int(who))
        # print('user_index',index)

        result = self.algo.get_neighbors(index, k=5)
        # print('당신과 유사한 사용자는? : ',result)
        # print('\n')
        #
        # print('당신에게 추천드리는 화장품 : ', '\n')

        for r1 in result:
            max_rating=self.data.df[self.data.df['Nickname']==r1]["rating"].max()
            cos_id=self.data.df[(self.data.df["rating"]==max_rating)&(self.data.df['Nickname']==r1)]["ProductIdx"].values

            for cos_item in cos_id:
                recommand.append(self.cos_list[cos_item])
        return recommand
