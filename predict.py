#!/usr/bin/python
#-*-coding: utf-8 -*-
######
import pickle
import pandas as pd
import numpy as np

modFile = './models/loan_predict_2020_08_31.p'
model = pickle.load(open(modFile,'rb'))
def predict(gender,	married, dependents,	education,	self_employed,	applicantIncome,	coapplicantIncome,	loanAmount,	loan_amount_term,	credit_history,	property_area):
  pd_columns_head = ['Loan_ID',	'Gender', 'Married', 'Dependents', 'Education',	'Self_Employed', 'ApplicantIncome',	'CoapplicantIncome',	'LoanAmount',	'Loan_Amount_Term',	'Credit_History', 'Property_Area', 'Loan_Status']
  pd_df = pd.DataFrame([
      ['Test', gender,	married, dependents,	education,	self_employed,	applicantIncome,	coapplicantIncome,	loanAmount,	loan_amount_term,	credit_history,	property_area, 'Y']
  ], columns = pd_columns_head)
 
  print("create data frame success")
  print(pd_df)
  pd_clean_df  = clean_data(pd_df)

  print("clean data success")
  print(pd_clean_df)
  
  if pd_clean_df['ApplicantIncome']+pd_clean_df['CoapplicantIncome'] == 0:
      pd_clean_df['DebtRatio'] = pd_clean_df['LoanAmount']
  else:
      pd_clean_df['DebtRatio'] = pd_clean_df['LoanAmount']/(pd_clean_df['ApplicantIncome']+pd_clean_df['CoapplicantIncome'])

  pd_feat, pd_temp = extract_feature(pd_clean_df)
  print("extract feature success")
  print(pd_feat)
  
  # sorting data

  Gender_0 = 0
  Gender_1 = 0
  if pd_feat['Gender'][0] == 0:
    Gender_0 = 1
  else:
    Gender_1 = 1

  Married_0 = 0
  Married_1 = 0
  if pd_feat['Married'][0] == 0:
    Married_0 = 1
  else:
    Married_1 = 1

  Dependents_0 = 0
  Dependents_1 = 0
  Dependents_2 = 0
  Dependents_3 = 0
  if pd_feat['Dependents'][0] <= 0:
    Dependents_0 = 1
  elif pd_feat['Dependents'][0] == 1:
    Dependents_1 = 1
  elif pd_feat['Dependents'][0] == 2:
    Dependents_2 = 1
  else:
    Dependents_3 = 1

  Education_0 = 0
  Education_1 = 0
  if pd_feat['Education'][0] == 0:
    Education_0 = 1
  else:
    Education_1 = 1

  Self_Employed_0 = 0
  Self_Employed_1 = 0
  if pd_feat['Self_Employed'][0] == 0:
    Self_Employed_0 = 1
  else:
    Self_Employed_1 = 1

  Credit_History_0 = 0
  Credit_History_1 = 0
  if pd_feat['Credit_History'][0] == 0:
    Credit_History_0 = 1
  else:
    Credit_History_1 = 1

  Property_Area_0 = 0
  Property_Area_1 = 0
  Property_Area_2 = 0
  if pd_feat['Property_Area'][0] == 0:
    Property_Area_0 = 1
  elif pd_feat['Property_Area'][0] == 1:
    Property_Area_1 = 1
  elif pd_feat['Property_Area'][0] == 2:
    Property_Area_2 = 1

  ApplicantIncome_GROUP_2000_3999 = 0
  ApplicantIncome_GROUP_4000_5999 = 0
  ApplicantIncome_GROUP_6000_up = 0
  ApplicantIncome_GROUP_Below_2000 = 0
  if pd_feat['ApplicantIncome'][0] < 2000:
    ApplicantIncome_GROUP_Below_2000 = 1
  elif pd_feat['ApplicantIncome'][0] >= 2000 and pd_feat['ApplicantIncome'][0] < 4000:
    ApplicantIncome_GROUP_2000_3999 = 1
  elif pd_feat['ApplicantIncome'][0] >= 4000 and pd_feat['ApplicantIncome'][0] < 6000:
    ApplicantIncome_GROUP_4000_5999 = 1
  elif pd_feat['ApplicantIncome'][0] >= 6000:
    ApplicantIncome_GROUP_6000_up = 1

  CoapplicantIncome_GROUP_2000_3999 = 0
  CoapplicantIncome_GROUP_4000_5999 = 0
  CoapplicantIncome_GROUP_6000_up = 0
  CoapplicantIncome_GROUP_Below_2000 = 0
  if pd_feat['CoapplicantIncome'][0] < 2000:
    CoapplicantIncome_GROUP_Below_2000 = 1
  elif pd_feat['CoapplicantIncome'][0] >= 2000 and pd_feat['CoapplicantIncome'][0] < 4000:
    CoapplicantIncome_GROUP_2000_3999 = 1
  elif pd_feat['CoapplicantIncome'][0] >= 4000 and pd_feat['CoapplicantIncome'][0] < 6000:
    CoapplicantIncome_GROUP_4000_5999 = 1
  elif pd_feat['CoapplicantIncome'][0] >= 6000:
    CoapplicantIncome_GROUP_6000_up = 1

  LoanAmount_GROUP_200_399 = 0
  LoanAmount_GROUP_400_599 = 0 
  LoanAmount_GROUP_600_up = 0
  LoanAmount_GROUP_Below_200 = 0
  if pd_feat['LoanAmount'][0] < 200:
    LoanAmount_GROUP_Below_200 = 1
  elif pd_feat['LoanAmount'][0] >= 200 and pd_feat['LoanAmount'][0] < 400:
    LoanAmount_GROUP_200_399 = 1
  elif pd_feat['LoanAmount'][0] >= 400 and pd_feat['LoanAmount'][0] < 600:
    LoanAmount_GROUP_400_599 = 1
  elif pd_feat['LoanAmount'][0] >= 600:
    LoanAmount_GROUP_600_up = 1

  Loan_Amount_Term_GROUP_200_399 = 0
  Loan_Amount_Term_GROUP_400_599 = 0
  Loan_Amount_Term_GROUP_Below_200 = 0
  # Loan_Amount_Term_GROUP_600_up = 0
  if pd_feat['Loan_Amount_Term'][0] < 200:
    Loan_Amount_Term_GROUP_Below_200 = 1
  elif pd_feat['Loan_Amount_Term'][0] >= 200 and pd_feat['Loan_Amount_Term'][0] < 400:
    Loan_Amount_Term_GROUP_200_399 = 1
  elif pd_feat['Loan_Amount_Term'][0] >= 400 and pd_feat['Loan_Amount_Term'][0] < 600:
    Loan_Amount_Term_GROUP_400_599 = 1
  # elif pd_feat['Loan_Amount_Term'][0] >= 600:
    # Loan_Amount_Term_GROUP_600_up = 1 // TODO train model to use 600 up

  # order_args = ['DebtRatio', 'Gender_0.0', 'Gender_1.0', 'Married_0.0',
  #      'Married_1.0', 'Dependents_0.0', 'Dependents_1.0',
  #      'Dependents_2.0', 'Dependents_3.0', 'Education_0', 'Education_1',
  #      'Self_Employed_0.0', 'Self_Employed_1.0', 'Credit_History_0.0',
  #      'Credit_History_1.0', 'Property_Area_0', 'Property_Area_1',
  #      'Property_Area_2', 'ApplicantIncome_GROUP_2000_3999',
  #      'ApplicantIncome_GROUP_4000_5999', 'ApplicantIncome_GROUP_6000_up',
  #      'ApplicantIncome_GROUP_Below_2000',
  #      'CoapplicantIncome_GROUP_2000_3999',
  #      'CoapplicantIncome_GROUP_4000_5999',
  #      'CoapplicantIncome_GROUP_6000_up',
  #      'CoapplicantIncome_GROUP_Below_2000', 'LoanAmount_GROUP_200_399',
  #      'LoanAmount_GROUP_400_599', 'LoanAmount_GROUP_600_up',
  #      'LoanAmount_GROUP_Below_200', 'Loan_Amount_Term_GROUP_200_399',
  #      'Loan_Amount_Term_GROUP_400_599',
  #      'Loan_Amount_Term_GROUP_Below_200']
  sorted_df = pd.DataFrame([[
    pd_feat['DebtRatio'][0],
    Gender_0,
    Gender_1,
    Married_0,
    Married_1,
    Dependents_0,
    Dependents_1,
    Dependents_2,
    Dependents_3,
    Education_0,
    Education_1,
    Self_Employed_0,
    Self_Employed_1,
    Credit_History_0,
    Credit_History_1,
    Property_Area_0,
    Property_Area_1,
    Property_Area_2,
    ApplicantIncome_GROUP_2000_3999,
    ApplicantIncome_GROUP_4000_5999,
    ApplicantIncome_GROUP_6000_up,
    ApplicantIncome_GROUP_Below_2000,
    CoapplicantIncome_GROUP_2000_3999,
    CoapplicantIncome_GROUP_4000_5999,
    CoapplicantIncome_GROUP_6000_up,
    CoapplicantIncome_GROUP_Below_2000,
    LoanAmount_GROUP_200_399,
    LoanAmount_GROUP_400_599, 
    LoanAmount_GROUP_600_up,
    LoanAmount_GROUP_Below_200,
    Loan_Amount_Term_GROUP_200_399,
    Loan_Amount_Term_GROUP_400_599,
    Loan_Amount_Term_GROUP_Below_200,
  ]])
  # predict by model

  result = model.predict(sorted_df)[0]
  if result == 1:
    result = "Approve"
  else:
    result = "Reject"

  return {"result": result}


def extract_feature(df):
  feat = df.copy().dropna()

  label = feat['Loan_Status']
  feat = feat.drop(['Loan_Status',], axis=1)
  return feat, label

def clean_data(df):
  clean_df = df.copy()
  clean_df = clean_df.drop('Loan_ID', axis=1)

  gender_map = {'Male': 0, 'Female': 1}
  marry_map = {'Yes': 1, 'No': 0}
  dependent_map = {'0': 0, '1': 1, '2': 2,'3+': 3}
  education_map = {'Graduate': 1, 'Not Graduate': 0}
  selfemp_map = {'Yes': 1, 'No': 0}
  area_map = {'Rural': 0,'Urban': 1,'Semiurban': 2}
  status_map = {'Y': 1,'N': 0}
  for i in range(0,1):
    clean_df.iloc[:,i] = clean_df.iloc[:,i].map(gender_map)
  for i in range(1,2):
    clean_df.iloc[:,i] = clean_df.iloc[:,i].map(marry_map)
  for i in range(2,3):
    clean_df.iloc[:,i] = clean_df.iloc[:,i].map(dependent_map)
  for i in range(3,4):
    clean_df.iloc[:,i] = clean_df.iloc[:,i].map(education_map)
  for i in range(4,5):
    clean_df.iloc[:,i] = clean_df.iloc[:,i].map(selfemp_map)
  for i in range(10,11):
    clean_df.iloc[:,i] = clean_df.iloc[:,i].map(area_map)
  for i in range(11,12):
    clean_df.iloc[:,i] = clean_df.iloc[:,i].map(status_map)

#drop row contain NaN
  clean_df.dropna(subset = ['Gender'], inplace=True )
  clean_df.dropna(subset = ['Self_Employed'], inplace=True)

#change blank to NaN and drop row
  clean_df['LoanAmount'].replace('', np.nan, inplace = True)
  clean_df.dropna(subset = ['LoanAmount'], inplace=True)
  clean_df['Loan_Amount_Term'].replace('', np.nan, inplace = True)
  clean_df.dropna(subset = ['Loan_Amount_Term'], inplace=True)
  clean_df['Credit_History'].replace('', np.nan, inplace = True)
  clean_df.dropna(subset = ['Credit_History'], inplace=True)

  return clean_df
