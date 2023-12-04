#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install pandas')


# In[6]:



import yfinance as yf
import pandas as pd
# Load the CSV file into a DataFrame
df_stocks = pd.read_csv(r"C:\Users\Sai\Desktop\Capstone\Datasets\stocks.csv")


# Function to get company name from ticker symbol
def get_company_name(ticker_symbol):
    try:
        ticker = yf.Ticker(ticker_symbol)
        return ticker.info['longName']
    except:
        return None

# Getting unique tickers from the dataset
unique_tickers = df_stocks['Ticker'].unique()

# Creating a dictionary to map ticker symbols to company names
ticker_to_name = {ticker: get_company_name(ticker) for ticker in unique_tickers}

# Mapping the 'Ticker' column to the 'Company Name' using the dictionary
df_stocks['Company Name'] = df_stocks['Ticker'].map(ticker_to_name)


# In[7]:


# Saving the updated dataframe to a new CSV file
output_path = r"C:\\Users\\Sai\\Desktop\\Capstone\\Datasets\\updated_stocks.csv"
df_stocks.to_csv(output_path, index=False)

output_path


# In[ ]:





# In[ ]:





# In[ ]:




