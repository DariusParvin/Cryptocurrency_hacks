#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:32:58 2019

@author: dariuscognac
"""
import pandas as pd
import numpy as np

df1 = pd.read_csv('Batch_3487043_batch_results.csv')
df2 = pd.read_csv('Batch_3487321_batch_results.csv')

    
dfNew = pd.DataFrame()

# Loop through exchanges
for company in df1["Input.urlName"]:
    
    year1 = df1["Answer.foundYear"][df1["Input.urlName"]==company].values[0]
    year2 = df2["Answer.foundYear"][df2["Input.urlName"]==company].values[0]
    
    link1 = df1["Answer.link"][df1["Input.urlName"]==company].values[0]
    link2 = df2["Answer.link"][df2["Input.urlName"]==company].values[0]
    
    confidence1 = df1["Answer.confidence.1"][df1["Input.urlName"]==company].values[0]
    confidence2 = df2["Answer.confidence.1"][df2["Input.urlName"]==company].values[0]
    totConfidence = int(confidence1) + int(confidence2)
    
    yearsAgree = int(year1==year2)
    
    dfNew = dfNew.append({'company':company, 'yearsAgree':yearsAgree, 
                      'yearFounded1':year1, 'yearFounded2':year2,
                      'confidence':totConfidence,
                      'link1':link1, 'link2':link2}, ignore_index=True)   

# Rearrange Columns, sort and save CSV    
cols = dfNew.columns.tolist()
rearrange = [0,6,1,4,5,2,3]
new_column_order = [cols[i] for i in rearrange]
dfNew = dfNew[new_column_order]

dfNew = dfNew.sort_values(by=['yearsAgree','confidence','company'], ascending=False)

dfNew.to_csv('MTurkProcessedData.csv', index=False)
