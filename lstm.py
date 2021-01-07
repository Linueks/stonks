import numpy as np
import pandas_datareader as web
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt


stock_ticker = 'TSLA'
start_date = '2015-01-01'
end_date = '2021-01-07'


#get the stock quote
df = web.DataReader(stock_ticker, data_source='yahoo', start=start_date,
                    end=end_date)


"""
plt.figure(figsize=(16,8))
plt.plot(df['Close'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD [$]', fontsize=18)
plt.show()
"""


#generating training and test samples
data = df.filter(['Close'])
dataset = data.values
training_percentage = 0.8
training_data_length = np.int(np.ceil(len(dataset) * training_percentage))


#Scaling variables usually results in better analysis
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)
training_data = scaled_data[0:training_data_length, :]
print(training_data)


#splitting into x_train and y_train datasets. Here the
x_train = []
y_train = []
for i in range(60, len(training_data)):
    x_train.append(training_data[i-60:i, 0])
    y_train.append(training_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)


# The LSTM model expects:
# [number of samples, number of time steps, number of features]
# x_train shape = (1756, 60) -> (1756, 60, 1)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))


#Build the LSTM network model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(units=50, return_sequences=False))
model.add(Dense(units=25))
model.add(Dense(units=1))

#compile model using optimizer of choice, ADAM is common
model.compile(optimizer='adam', loss='mean_squared_error')

#train the model
batch_size = 2
epochs = 10
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs)
model.save(f'saved_models/my_model_bs{batch_size}_eps{epochs}')

test_data = scaled_data[training_data_length - 60:, :]
x_test = []
y_test = dataset[training_data_length:, :]
for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i, 0])

x_test = np.array(x_test)
#reshape in same way as for the x_training data, this is because the model
#expects the format to be three dimensional.
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))


predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)


mean_squared_error = np.mean((predictions - y_test)**2)
root_mean_squared_error = np.sqrt(mean_squared_error)

print(f'MSE: {mean_squared_error}, RMSE: {root_mean_squared_error}')



#Plotting and comparison code
train = data[:training_data_length]
valid = data[training_data_length:]
valid['Predictions'] = predictions

plt.figure(figsize = (16, 8))
plt.title(f'LSTM-model for {stock_ticker}')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price [$]', fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.show()
