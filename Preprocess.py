# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:15:55 2018

@author: Intern
"""

import pandas as pd
import numpy as np 
import numpy as np
from scipy import stats

#extract dataset 
df_2015=pd.read_csv('C:/Users/intern/Downloads/dataset/data_2015.csv')
df_2016=pd.read_csv('C:/Users/intern/Downloads/dataset/data_2016.csv')
df_2017=pd.read_csv('C:/Users/intern/Downloads/dataset/data_2017.csv')
df_2018=pd.read_csv('C:/Users/intern/Downloads/dataset/data_2018.csv')
df=pd.read_csv('C:/Users/intern/Downloads/dataset/data_whole.csv')

df_2015['year']=2015
df_2016['year']=2016
df_2017['year']=2017
df_2018['year']=2018



df1=df_2015[['year', 'feeling satisfied']]
df2=df_2016[['year', 'feeling satisfied']]
df3=df_2017[['year', 'feeling satisfied']]
df4=df_2018[['year', 'feeling satisfied']]
df1=df1.dropna()
df2=df2.dropna()
df3=df3.dropna()
df4=df4.dropna()
frames = [df1,df2,df3,df4]
result = pd.concat(frames)
unsatis=result[result['feeling satisfied']<=3]
year_precentage=unsatis.groupby(['year']).count()/result.groupby(['year']).count()*100
year=year_precentage.merge(year_precentage,how='outer')


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
