# adding common imports here, might be bad practice dunno
import numpy as np
import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as datetime
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
#from data_reader import get_stock
import os


sns.set_style('whitegrid')
sns.color_palette('rocket')
#plt.style.use('ggplot')




stock_ticker = 'TSLA'
start_date = '2015-01-01'
end_date = '2021-01-07'
todays_date = datetime.date.today()



training_percentage = 0.8
batch_size = 64
epochs = 10
sequence_length = 60
future_period_predict = 1
