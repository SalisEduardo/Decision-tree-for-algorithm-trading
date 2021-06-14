
import pandas as pd
from pandas_datareader import data as web
import numpy as np
from datetime import datetime
from time import  sleep

from extract_data import extract_fin_data

#Extraction
date_beg = datetime(2010,1,1)
date_end = datetime(2021,5,31)

#Exchange Traded Fund with the intention to replicate the Bovespa Index
product = ["BOVA11.SAO"]

df = extract_fin_data(product, date_beg, date_end)

df_copy = df.copy()
df_copy.columns = df_copy.columns.droplevel()

df_copy. to_csv("bova11_pure.csv")