from parameters_and_imports import *
from data_reader import get_stock



def classify(current, future, ratio=1.03):
    """
    According to ratio tells you if it's a buy 1 or sell 0
    The ratio can be tuned to reflect i.e. percentage taken by bank etc
    """
    if float(future) > ratio * float(current):
        return 1
    else:
        return 0



def preprocess_df(df):#, training_percentage):
    """
    This function wants to take in a given dataframe and then make a new column
    with features 0 or 1 where 0 represents sell and 1 represents buy.

    """
    df = df.drop('future', 1)
    #print(df)

    #df = df.drop('Daily Return')
    #df.dropna(inplace=True)

    #for col in df.columns:
    #    if col != 'target':
    #        print(col)
    #        df[col] = df[col].pct_change()
    #        df.dropna(inplace=True)
    #        df[col] = preprocessing.scale(df[col].values)

    #df.dropna(inplace=True)


    return df



#NAME = f"{SEQ_LEN}-SEQ-{FUTURE_PERIOD_PREDICT}-PRED-{int(time.time())}"


stock_data = get_stock(stock_ticker)

stock_data['future'] = stock_data['Close'].shift(-future_period_predict)
print(stock_data)

stock_data.dropna(inplace=True)
stock_data['target'] = list(map(classify, stock_data['Close'], stock_data['future']))
print(stock_data)
print(stock_data['target'].value_counts())


stock_data = preprocess_df(stock_data)
#print(stock_data)
