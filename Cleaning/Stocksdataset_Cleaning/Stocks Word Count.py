#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\Sai\Downloads\owid-covid-data.csv")

# Calculate the frequency of each ticker in the "Ticker" column
covid_year_frequency = df['Year'].value_counts()
covid_Country_frequency = df['location'].value_counts()
covid_Continenty_frequency = df['continent'].value_counts()


# Display the most frequently occurring tickers
print(covid_year_frequency.head(20))
print(covid_Country_frequency.head(20))
print(covid_Continenty_frequency.head(20))


# In[ ]:





# In[8]:


from collections import Counter
import re

data = pd.read_csv(r"C:\Users\Sai\Downloads\COVID-19 Hospitalization.csv")

# Columns with textual data
text_columns = [
    'Year', 'Bene_Geo_Desc', 'Bene_Mdcd_Mdcr_Enrl_Stus', 'Bene_Race_Desc', 
    'Bene_Sex_Desc', 'Bene_Mdcr_Entlmt_Stus', 'Bene_Age_Desc', 'Bene_RUCA_Desc'
]

# Combine text from these columns
combined_text = ' '.join(data[text_columns].astype(str).stack())

# Tokenize the text into words using a regular expression
words = re.findall(r'\w+', combined_text)

# Use Counter to count the frequency of each word
word_counts = Counter(words)

# Get the most common words
most_common_words = word_counts.most_common(100)
most_common_words


# In[ ]:




