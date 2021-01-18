import pandas as pd

df = pd.read_csv('credit.csv')

df = df[['BALANCE', 'PURCHASES', 'ONEOFF_PURCHASES', 'CREDIT_LIMIT',	'PAYMENTS',	'MINIMUM_PAYMENTS']]

df.to_excel('data_credit.xlsx')