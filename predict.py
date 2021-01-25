from tensorflow import keras
from parameters_and_imports import *
import argparse
from data_reader import get_stock




"""
parser = argparse.ArgumentParser()
parser.add_argument('model',
                default='saved_models\my_model_bs1_eps10',
                help='current format for model name:\
                my_model_bsX_epsY, where bs is batch size and eps is epochs')
args = parser.parse_args()
model_name = args.model


for some reason getting error when using the f-string so have to hard code name i guess........
print(f'saved_models\{args.model}')
print(model_name)
print('saved_models\\' + model_name)
print('saved_models\my_model_bs1_eps10')
print(f'saved_models\\{args.model}')
"""




# I want to get it working like this but not working for some reason
#model = keras.models.load_model('saved_models\\' + model_name)
model = keras.models.load_model('saved_models\my_model_bs1_eps10')



#this number 60 is arbitrary i think, just using it for now
start = todays_date - datetime.timedelta(days=60)
#this causes problems because there're no values for sundays and holidays
#can get around by using the start_date set in params and imports and picking
#out the last 60 values present in that data
"""
last_sixty_days = web.DataReader(stock_ticker, data_source='yahoo',
                            start=start, end=todays_date)
"""


stock_data = get_stock()
last_sixty_days = stock_data.filter(['Close'])[-60:].values
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(last_sixty_days)
last_sixty_days_scaled = scaler.transform(last_sixty_days)



X_test = []
X_test.append(last_sixty_days_scaled)
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
print(X_test.shape)


tomorrows_price = model.predict(X_test)
tomorrows_price = scaler.inverse_transform(tomorrows_price)


print(f'Predicted price for tomorrow: {tomorrows_price[0,0]}')
print(f'Prediction as a percentage of the previous days price: {tomorrows_price[0,0] / last_sixty_days[-1,0]}')
