# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 19:56:35 2022

@author: hp
"""

import numpy as np
import pandas as pd

#df1 = pd.read_excel(r'C:\Users\Satish S\Desktop\python flask\Data set Template\Final data.xlsx')

df=df1
df.columns=['nm','gr','ug','ugsp','irt','ski','cgp','cert','certc','wrk','job','mas']

df.fillna('', inplace=True)
del df['nm']

i=0
while 1195 >i:
 m_to_b=df.ug[i]
 if m_to_b.startswith('M') ==True:
       df.ug[i] = m_to_b.replace(m_to_b[0], 'B')
        
 i=i+1  
 
df

df.loc[df['ugsp'] == 'C,c++, java', 'ugsp'] = 'computer science Engineering'
df.loc[df['ugsp'] == 'Science,Maths, Engineering subject', 'ugsp'] = 'Engineering'
df.loc[df['ugsp'] == 'Structural Engineeeing', 'ugsp'] = 'civil engineering'
df.loc[df['ugsp'] ==  'High pressure die casting ', 'ugsp'] = 'Mechanical engineering'

df.loc[df['ugsp'] == 'Electrical Machines', 'ugsp'] = 'celectrical Engineering'
df.loc[df['ugsp'] == 'ManagementÃŠ', 'ugsp'] = 'Management'
df.loc[df['ugsp'] == 'Principal of programming language with C, MS Office Management Tools, Computer Organization, Mathematics, English.', 'ugsp'] = 'computer science engineering'
df.loc[df['ugsp'] == 'Electronics & Telecom.', 'ugsp'] = 'Electrical and Electronics engineering'

df.loc[df['ugsp'] == 'Mechanical ', 'ugsp'] = 'Mechanical Engineering'
df.loc[df['ugsp'] == 'Structural analysis ', 'ugsp'] = 'civil Engineering'
df.loc[df['ugsp'] == 'Transportation Engineering', 'ugsp'] = 'civil engineering'
df.loc[df['ugsp'] =='B.E complete', 'ugsp'] = 'engineering'

df.loc[df['ugsp'] =='Computer ( Languages like  .. C, C++ ,  Java,  C# ) ', 'ugsp'] = 'computer science Engineering'
df.loc[df['ugsp'] =='Java Programming & Website Designing' , 'ugsp'] = 'computer science Engineering'
df.loc[df['ugsp'] == 'Programing language', 'ugsp'] = 'computer science engineering'
df.loc[df['ugsp'] == 'C, C++, Java, SQL, MySQL, Unix, HTML, Mathematics, Statistics', 'ugsp'] = 'computer science engineering'

df.loc[df['ugsp'] == 'Cse', 'ugsp'] = 'computer science Engineering'
df.loc[df['ugsp'] == 'Building material and construction ', 'ugsp'] = 'civil Engineering'
df.loc[df['ugsp'] == 'MathematicsÃŠ', 'ugsp'] = 'mathematics'
df.loc[df['ugsp'] == 'CSIT', 'ugsp'] = 'computer science engineering'

df.loc[df['ugsp'] ==  'Java ', 'ugsp'] = 'computer science Engineering'
df.loc[df['ugsp'] == 'Engineering graphics', 'ugsp'] = 'civil Engineering'
df.loc[df['ugsp'] == 'B.E.\xa0', 'ugsp'] = 'engineering'
df.loc[df['ugsp'] == 'Oops', 'ugsp'] = 'computer science engineering'

df.loc[df['ugsp'] ==   'NAthing ', 'ugsp'] = 'na'
df.loc[df['ugsp'] == 'Graphics', 'ugsp'] = 'civil Engineering'
df.loc[df['ugsp'] ==  'C, C++, java, SQL, MYSql, Unix, Html, Mathematics, Statistics', 'ugsp'] = 'computer science engineering'
df.loc[df['ugsp'] ==  'Coding', 'ugsp'] = 'computer science engineering'

df.loc[df['ugsp'] ==  'C language', 'ugsp'] = 'computer science Engineering'
df.loc[df['ugsp'] =='C++', 'ugsp'] = 'computer science Engineering'
df.loc[df['ugsp'] == 'Coding ', 'ugsp'] = 'computer science engineering'
df.loc[df['ugsp'] == 'Java', 'ugsp'] = 'computer science engineering'

df.loc[df['ugsp'] ==   'Structure ', 'ugsp'] = 'civil Engineering'
df.loc[df['ugsp'] == 'Mechanical Machines ', 'ugsp'] = 'mechanical Engineering'
df.loc[df['ugsp'] == 'Software engineering, java programming, web development ', 'ugsp'] = 'computer science engineering'
df.loc[df['ugsp'] == 'Mechania', 'ugsp'] = 'mechanical engineering'


bool_series = pd.isnull(df["ugsp"]) 
bool_series.sum()

df4=df.iloc[:,[1,2,3,4,9,10]] 
df3=df4.copy()

dfj=df.loc[df.wrk =='Yes'].iloc[:,[1,2,3,4,9]]
#dfj.to_csv(r'C:\Users\Satish S\Desktop\python flask\Data set Template\df_job_data_set_for_imputy.csv')
#dfj = pd.read_excel(r'C:\Users\Satish S\Desktop\python flask\Data set Template\df_job_data_set_for_impute_to.xlsx')
dfjcopy=dfj.iloc[:,[2,3,4,5,9]]
dfj.rename(columns = {'Unnamed: 0':'index'}, inplace = True)
dfj.set_index(['index'], inplace = True)
dfj=dfj.iloc[:,[1,2,3,4,8]]

dfm=df.loc[(df.wrk =='No') & (df['mas'] !="" )].iloc[:,[1,2,3,4,10]]
#dfm.to_csv(r'C:\Users\Satish S\Desktop\python flask\Data set Template\df_mast_data_set_for_imputy.csv')
#dfm=pd.read_csv(r"C:\Users\Satish S\Desktop\python flask\Data set Template\df_mast_data_set_for_imputy_to.csv", encoding= 'unicode_escape')
dfmcopy=dfm.iloc[:,[2,3,4,5,9]]
dfm.rename(columns = {'Unnamed: 0':'index'}, inplace = True)
dfm.set_index(['index'], inplace = True)
dfm=dfm.iloc[:,[1,2,3,4,8]]

dfs=df.loc[(df.wrk =='No') & (df.mas =="" )].iloc[:,[1,2,3,4]]

# Model Building

def rec(which,d,topN):

    #which='j'
    global df3
    df3 = df3.append(dict(d),ignore_index = True)
    print('hi')
    dfs=df3.iloc[[-1],[0,1,2,3]]
    df3['factors'] = df3[['ug', 'ugsp', 'irt', 'ski']].agg('-'.join, axis=1)
    # Removing punctuations
    df_f=df3.factors
    df_f.replace("[^a-zA-Z]"," ",regex=True, inplace=True)
    df_f = df_f.to_frame()
    df_f.columns=['factors']
    
    from sklearn.feature_extraction.text import TfidfVectorizer #term frequencey- inverse document frequncy is a numerical statistic that is intended to reflect how important a word is to document in a collecion or corpus
    df_f["factors"].isnull().sum() 
    tfidf = TfidfVectorizer(stop_words = "english")    # taking stop words from tfid vectorizer 
    tfidf_matrix = tfidf.fit_transform(df_f["factors"])   #Transform a count matrix to a normalized tf or tf-idf representation
    tfidf_matrix_df=pd.DataFrame.sparse.from_spmatrix(tfidf_matrix)
    df_final=tfidf_matrix_df
    
    lst_j=[]
    for i in df_final.index:
        for j in dfj.index:
            if i==j:
                lst_j.append(j)
            else:
                continue   
    
    lst_m=[]
    for i in df_final.index:
        for j in dfm.index:
            if i==j:
                lst_m.append(j)
            else:
                continue 
            
    lst_s=[]
    for i in df_final.index:
        for j in dfs.index:
            if i==j:
                lst_s.append(j)
            else:
                continue 
    
    df_final_j=df_final.loc[lst_j,:]
    df_final_m=df_final.loc[lst_m,:]
    df_final_s=df_final.loc[lst_s,:]
    df_final_s.iloc[[-1],:]
    
    if str(which)=='j' or str(which)=='J':
        y=df_final_j
    else:
        y=df_final_m
    
    from sklearn.metrics.pairwise import sigmoid_kernel
    #sigmoid computation
    sig_sim_matrix=sigmoid_kernel(df_final_s.iloc[[-1],:],y)
    df_sig_sim_matrix = pd.DataFrame(sig_sim_matrix)
    sig_scores = list(enumerate(sig_sim_matrix[0]))
    sig_scores

    
    if which=='j' or which=='J':     
        # Sorting the sig_similarity scores based on scores 
        sig_scores = sorted(sig_scores, key=lambda x:x[1], reverse = True)
    
        # Get the scores of top N most similar job 
        #sig_scores_N = sig_scores[0: topN+1]
    
        # Getting the job index 
        s_idx  =  [i[0] for i in sig_scores]
        s_scores =  [i[1] for i in sig_scores]
    
        # Similar job and scores
        s_similar_show = pd.DataFrame(columns=["job", "Score"])
        s_similar_show["job"] = dfjcopy.loc[s_idx, "job"]
        s_similar_show["Score"] = s_scores
        s_similar_show=s_similar_show.loc[(s_similar_show.job !='')]
        s_similar_show=s_similar_show.drop_duplicates(subset='job', keep="first")
        s_similar_show_N=s_similar_show.iloc[0:topN+1,:]
        s_similar_show_N.reset_index(inplace = True)
        ca = s_similar_show_N['job'].values.tolist()
    
        # s_similar_show.drop(["index"], axis=1, inplace=True)
        #print (s_similar_show_N)
        #return (s_similar_show_N)
        result = []
        for sublist in ca:
            for item in sublist:
                result.append(item)
        # print(career_unique.iloc[1:, :])
        return ca

    
    else:
        # Sorting the sig_similarity scores based on scores 
        sig_scores = sorted(sig_scores, key=lambda x:x[1], reverse = True)
    
        # Get the scores of top N most similar job 
        #sig_scores_N = sig_scores[0: topN+1]
    
        # Getting the masters index 
        s_idx  =  [i[0] for i in sig_scores]
        s_scores =  [i[1] for i in sig_scores]
    
        # Similar masters and scores
        s_similar_show = pd.DataFrame(columns=["mas", "Score"])
        s_similar_show["mas"] = dfmcopy.loc[s_idx, "mas"]
        s_similar_show["Score"] = s_scores
        s_similar_show=s_similar_show.loc[(s_similar_show.mas !='')]
        s_similar_show=s_similar_show.drop_duplicates(subset='mas', keep="first")
        s_similar_show_N=s_similar_show.iloc[0:topN+1,:]
        s_similar_show_N.reset_index(inplace = True)
        ca = s_similar_show_N['mas'].values.tolist()

        result = []
        for sublist in ca:
            for item in sublist:
                result.append(item)
        # print(career_unique.iloc[1:, :])
        return ca


# iterating the columns
#for col in df.columns:
#print("enter your details:  ")
#nm=input("Enter the name:  ")
#d['gr']=input("Enter the gender:  ")
#d['ug']=input("Enter the UG:  ")
#d['ugsp']=input("Enter the UG specialization:  ")
#d['irt']=input("Enter the interests:  ")
#d['ski']=input("Enter the skills :  ")
#d['cgp']=float(input("Enter the cgpa/percentage:  "))
#d['cert']=input("Did you do any certification courses additionally? :  ")
#d['certc']=input("If yes, please specify your certificate course title:  ")
#d['wrk']='No'
#d['job']=" "
#d['mas']=" "

#which=str(input("Would you be interested in a job or higher education?(if job plz input 'j' or if higher education, plz input 'h'):"))
#if str(which)=='j' or str(which)=='J':
#    topN=int(input("Enter the No.of Jobs to be recommended:  "))
#else:
#    topN=int(input("Enter the No.of Higher studies to be recommended:  "))

#recommendations=rec(d,topN)
#recommendations
