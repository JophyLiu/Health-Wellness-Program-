# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:40:28 2018

@author: Intern
"""
import pandas as pd
import numpy as np

#create the list that want to be extract 
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



common_whole_question=['Did you leave feeling satisfied with your retreat experience?',
'If no, please explain',
'what aspect of the retreat had the most impact for you',
'Had you been to a TAPS Retreat before?',
'If yes, which retreat(s)?',
'How likely are you to attend a TAPS Retreat in the future?',
'How likely are you to recommend a fellow survivor to attend a TAPS Retreat in the future?',
'Would you like any further information on the following TAPS Services?',
'How likely are you to remain in contact with other retreat participants?',
'I would recommend a retreat to others who are in similar circumstances.',
'I am glad I attended this retreat']

useful_question=['Are you familiar with other resources that TAPS offers?',
'following this retreat, do you fell more strongly connected to taps?',
'do you feel better connected to other survivors?',
'Please share any feedback on your TAPS staff']

#basic structure
#extract
#create an empty list
#b=dict([(question, []) for question in common_question])
#create a function to 
def extract_question(df,question):
    a=list(df.columns)
    for t in a:
        if question in t:
            b[question]=b[question]+list(df[t].values)
    return b
        
#for question in common_question:
#    extract_question(survey_2016_0_df,question)

#for question in common_question:
#    extract_question(survey_2016_1_df,question)
    
    
#complete 
# as whole
#2016
b=dict([(question, []) for question in common_question])
#2016
for i in range(10):
    for question in common_question:
        df=pd.read_csv('C:/Users/intern/Downloads/dataset/2016/'+str(i)+'.csv')
        extract_question(df,question)

#2015
for i in range(2):
    for question in common_question:
        df=pd.read_csv('C:/Users/intern/Downloads/dataset/2015/'+str(i)+'.csv')
        extract_question(df,question)
#2017        
for i in range(20):
    for question in common_question:
        df=pd.read_csv('C:/Users/intern/Downloads/dataset/2017/'+str(i)+'.csv')
        extract_question(df,question)
#2018        
for i in range(6):
    for question in common_question:
        df=pd.read_csv('C:/Users/intern/Downloads/dataset/2018/'+str(i)+'.csv')
        extract_question(df,question)

df_whole=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in b.items() ]))


df_whole.to_csv('C:/Users/intern/Downloads/dataset/data_whole.csv')














#seperate as year
        
#2016        
def extract_question_year(df,question):
    a=list(df.columns)
    for t in a:
        if question in t:
            dict_2016[question]=dict_2016[question]+list(df[t].values)
    return dict_2016        
dict_2016=dict([(question, []) for question in common_question])
for i in range(10):
    for question in common_question:
        df=pd.read_csv('C:/Users/intern/Downloads/dataset/2016/'+str(i)+'.csv')
        extract_question_year(df,question)
df_2016=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dict_2016.items() ]))
#df_2016.to_csv('C:/Users/intern/Downloads/dataset/data_2016.csv')
#2015
def extract_question_year(df,question):
    a=list(df.columns)
    for t in a:
        if question in t:
            dict_2015[question]=dict_2015[question]+list(df[t].values)
    return dict_2015         
dict_2015=dict([(question, []) for question in common_question])        
for i in range(2):
    for question in common_question:
        df=pd.read_csv('C:/Users/intern/Downloads/dataset/2015/'+str(i)+'.csv')
        extract_question_year(df,question)
df_2015=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dict_2015.items() ]))
#df_2015.to_csv('C:/Users/intern/Downloads/dataset/data_2015.csv')

#2017 
        
def extract_question_year(df,question):
    a=list(df.columns)
    for t in a:
        if question in t:
            dict_2017[question]=dict_2017[question]+list(df[t].values)
    return dict_2017   
dict_2017=dict([(question, []) for question in common_question])         
for i in range(20):
    for question in common_question:
        df=pd.read_csv('C:/Users/intern/Downloads/dataset/2017/'+str(i)+'.csv')
        extract_question_year(df,question)
df_2017=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dict_2017.items() ]))
#df_2017.to_csv('C:/Users/intern/Downloads/dataset/data_2017.csv')
#2018 
        
def extract_question_year(df,question):
    a=list(df.columns)
    for t in a:
        if question in t:
            dict_2018[question]=dict_2018[question]+list(df[t].values)
    return dict_2018   
dict_2018=dict([(question, []) for question in common_question])          
for i in range(6):
    for question in common_question:
        df=pd.read_csv('C:/Users/intern/Downloads/dataset/2018/'+str(i)+'.csv')
        extract_question_year(df,question)
        
df_2018=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dict_2018.items() ]))
#df_2018.to_csv('C:/Users/intern/Downloads/dataset/data_2018.csv')


