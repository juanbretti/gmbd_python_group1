#%%
# General usage
import math
import numpy as np
import pandas as pd

# Reporting
from pandas_profiling import ProfileReport

# Preprocessing
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer, SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Modeling
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, f1_score, recall_score, matthews_corrcoef, confusion_matrix, precision_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# https://dateutil.readthedocs.io/en/stable/relativedelta.html
from datetime import datetime
from dateutil.relativedelta import relativedelta, MO

# Plotting
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

#%%
# df.to_pickle('storage\RBA_KYC_Accounts_ALL_Ids.pkl')
df = pd.read_pickle('storage/RBA_KYC_Accounts_ALL_Ids.pkl')

#%%
# Columns allocation

print('\n'*2)
print('Alek')
print(df.columns[0:9])
print('\n'*2)
print('Addison')
print(df.columns[9:18])
print('\n'*2)
print('Esperanza')
print(df.columns[18:27])
print('\n'*2)
print('Aziz')
print(df.columns[27:36])
print('\n'*2)
print('Bretti')
print(df.columns[36:])

#%%
df2 = df.iloc[:, 36:]

profile = ProfileReport(df2, title="RBA_KYC_Accounts >> Before >> JP", minimal=False)
profile.to_file("storage/df_report_before_jp.html")

#%%
df['score_card_Desc'].value_counts()
# %%
