# adding common imports here, might be bad practice dunno
import numpy as np
import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta
from sklearn.preprocessing import MinMaxScaler





stock_ticker = 'TSLA'
start_date = '2015-01-01'
end_date = '2021-01-07'
todays_date = date.today()



training_percentage = 0.8
batch_size = 1
epochs = 2
