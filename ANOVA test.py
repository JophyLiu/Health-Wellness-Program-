# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 13:22:56 2018

@author: Intern
"""

#ANALYST FOR QUESTION ONE
df_2015['year']=2015
df_2016['year']=2016
df_2017['year']=2017
df_2018['year']=2018

df1=df_2015[['year','feeling satisfied']]
df2=df_2016[['year','feeling satisfied']]
df3=df_2017[['year','feeling satisfied']]
df3=df3.dropna()
df4=df_2018[['year','feeling satisfied']]


frames = [df1,df2,df3,df4]
result = pd.concat(frames)
result=result.dropna()
year_s=result.groupby(['year']).mean()

import matplotlib.pyplot as plt
#mean
year_s.plot(figsize=(8,6),
            title='The score trends of participants feeling satisfied for retrest experience',
            xticks =np.arange(2015, 2019, step=1)
            )

#satisfied rate:
a1=(df1[df1['feeling satisfied']==[4,5]].count())/(df1.count())

#anova to test different between group
from scipy import stats

F, p = stats.f_oneway(df1['feeling satisfied'], df2['feeling satisfied'], df3['feeling satisfied'],df4['feeling satisfied'])
print("the p_value of anova is "+str(p)+" which acutually mean there are no different between each year")
