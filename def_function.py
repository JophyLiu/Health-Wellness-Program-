# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 17:24:26 2018

@author: Intern
"""
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

common_question=['feeling satisfied',
                 'most impact for you',
                 'Had you been to a TAPS Retreat before?',
                 'which retreat(s)?',
                 'How likely are you to attend a TAPS Retreat in the future?',
                 'recommend a fellow survivor',
                 'Would you like any further information on the following TAPS Services?',
                 'I am glad I attended this retreat',
                 'remain in contact with other retreat participants',
                 'recommend a retreat to others',
                 'familiar with other resources that TAPS offers?',
                 'share any feedback on your TAPS staff'
                 ]

numerical_question=['feeling satisfied',
                 'How likely are you to attend a TAPS Retreat in the future?',
                 'recommend a fellow survivor',
                 'I am glad I attended this retreat',
                 'emain in contact with other retreat participants'
                 ]

df_2015['year']=2015
df_2016['year']=2016
df_2017['year']=2017
df_2018['year']=2018

df_2017['feeling satisfied']=df_2017['feeling satisfied'].fillna(5)


frames = [df_2015,df_2016,df_2017,df_2018]
result = pd.concat(frames)


for i in numerical_question:
    df1=df_2015[['year', i]]
    df2=df_2016[['year', i]]
    df3=df_2017[['year', i]]
    df4=df_2018[['year', i]]
    df1=df1.dropna()
    df2=df2.dropna()
    df3=df3.dropna()
    df4=df4.dropna()
    frames = [df1,df2,df3,df4]
    result = pd.concat(frames)
    year_s=result.groupby(['year']).mean()
    year_s.plot(figsize=(8,6),
        title='The score trends of participants '+i+' for retrest experience',
        xticks =np.arange(2015, 2019, step=1)
        )
    F, p = stats.f_oneway(df1[i], df2[i], df3[i],df4[i])
    print("the p_value of anova is "+str(p))



#try to find the reason
for i in numerical_question:
    df1=df_2015[['year', i]]
    df2=df_2016[['year', i]]
    df3=df_2017[['year', i]]
    df4=df_2018[['year', i]]
    df1=df1.dropna()
    df2=df2.dropna()
    df3=df3.dropna()
    df4=df4.dropna()
    frames = [df1,df2,df3,df4]
    result = pd.concat(frames)
    unsatis=result[result[i]<=3]
    year_percentage=unsatis.groupby(['year']).count()/result.groupby(['year']).count()*100
    print(year_percentage)

frames = [df_2015,df_2016,df_2017,df_2018]
result = pd.concat(frames)

impact=result[['year','feeling satisfied','most impact for you']]
impact_sat=impact[impact['feeling satisfied']>=4]
impact_unsat=impact[impact['feeling satisfied']<=3]


