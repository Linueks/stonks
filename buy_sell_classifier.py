from parameters_and_imports import *
from data_reader import get_stock



def classify(current, future, ratio=1.0):
    """
    According to ratio tells you if it's a buy 1 or sell 0
    The ratio can be tuned to reflect i.e. percentage taken by bank etc
    """
    if float(future) > ratio * float(current):
        return 1
    else:
        return 0



def preprocess_df(df, training_percentage):



    return



#NAME = f"{SEQ_LEN}-SEQ-{FUTURE_PERIOD_PREDICT}-PRED-{int(time.time())}"


stock_data = get_stock(stock_ticker)


stock_data['future'] = stock_data['Close'].shift(-future_period_predict)
stock_data.dropna(inplace=True)
stock_data['target'] = list(map(classify, stock_data['Close'], stock_data['future']))
print(stock_data)
