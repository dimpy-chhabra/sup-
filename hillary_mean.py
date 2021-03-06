import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

data_news_hillary = pd.read_csv('data_news_hillary.csv')
data_news_trump = pd.read_csv('data_news_Trump.csv')
#source_name	desc_subjectivity	desc_polarity	titl_subjectivity	titl_polarity

a = data_news_hillary.source
b = data_news_hillary.desc_subjectivity
c = data_news_hillary.desc_polarity
d = data_news_hillary.titl_subjectivity
e = data_news_hillary.titl_polarity

mean_desc = np.mean(c)
mean_title = np.mean(e)

print("The Mean of Desc Polarity for Hillary is {}".format(mean_desc))
print("The Mean of Title Polarity for Hillary is {}".format(mean_title))