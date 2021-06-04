
#Bibliotecas
import pandas as pd
from pandas_datareader import data as web
import numpy as np
from datetime import datetime
from time import  sleep
from alpha_vantage.timeseries import TimeSeries

#my key for the use of th API
from key import key 


#function to extract stock information with pandas data reader and alphavantage
def extract_fin_data(tickers, inic, fim):
      import pandas as pd
      from pandas_datareader import data as web
      import numpy as np
      
      dfs = []
      for ticker in tickers:    
        df_preco = web.DataReader(ticker, 'av-daily-adjusted', start = inic, end=fim, api_key=(key))
        df_preco.index = pd.to_datetime(df_preco.index, format ='%Y-%m-%d').to_period('D')
        dfs.append(df_preco)
        df_completo = pd.concat(dfs, axis = 1,keys= tickers)  
      return df_completo



ts = TimeSeries(key=key, output_format = 'pandas')

#function not working as expected
def fin_data(tickers, beg, end,p):
      
      '''
      Returns a Mult Index Dataframe, which column represents a table with the stock information
      tickers (list): list of strings with stock tickers
      beg (str): beginning date of the period (Y-M-D)
      end (str) : ending date of the period (Y-M-D)

      '''
      
      df_completo=[]
      contador = 0
      for tag in tickers:
          contador = contador + 1
          if contador % 5 == 0:
                  sleep(65)    
          try:
            
            dados,meta_dados = ts.get_daily_adjusted(tag)
            dados= dados.sort_index()
            dados.index = pd.to_datetime(dados.index)
            dados.index = dados.index.to_period(p)
            df_completo.append(dados[beg:end].rename(columns = {'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. adjusted close': 'adj close', '6. volume': 'volume','7. dividend amount': 'dividend amount',"8. split coefficient":"split coefficient"}))
      
          except: 
            continue
      
      df_completo_concat = pd.concat(df_completo,axis=1,keys= tickers)
      return df_completo_concat
        

      










