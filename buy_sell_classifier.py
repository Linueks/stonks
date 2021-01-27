from parameters_and_imports import *
from data_reader import get_stock



def classify(current, future, ratio=1.02):
    """
    According to ratio tells you if it's a buy 1 or sell 0
    The ratio can be tuned to reflect i.e. percentage taken by bank etc
    """
    if float(future) > ratio * float(current):
        return 1
    else:
        return 0



def preprocess_df(df, verbose=False):#, training_percentage):
    """
    This function wants to take in a given dataframe and then make a new column
    with features 0 or 1 where 0 represents sell and 1 represents buy. This is
    determined from the variable "future_period_predict". This chooses the day
    to compare to in order to see if the price went up or down


    Should return training and validation data set.
    """

    df['future'] = df['Close'].shift(-future_period_predict)
    df.dropna(inplace=True)
    df['target'] = list(map(classify, df['Close'], df['future']))               # I feel this can be done cleaner with just dataframe operations
    #df['target'] = df['Close'].apply()
    #print(df['target'].value_counts()) #checking if the map worked
    training_data_length = np.int(np.ceil(len(df['Close'])\
                                        * training_percentage))
    #print(training_data_length)
    #print(df.iloc[60:80])


    x_train = []
    y_train = []


    for i in range(sequence_length, training_data_length):
        x_train.append(df['Close'].values[i-sequence_length:i])


    y_train = df['target'].values[sequence_length:training_data_length]
    x_train = np.array(x_train)

    #print(x_train[0].shape, y_train.shape)
    #print(x_train[0], x_train[1])                                              # Check the sequences in x_train with the corresponding values in
    #print(y_train[60], y_train[61])                                            # y train, they're shifted by the value sequence length from each other


    x_validation = []

    for i in range(training_data_length, len(df['Close'].values)):
        x_validation.append(df['Close'].values[i-sequence_length:i])


    x_validation = np.array(x_validation)
    y_validation = df['target'].values[training_data_length:]

    train_unique, train_counts = np.unique(y_train, return_counts=True)
    val_unique, val_counts = np.unique(y_validation, return_counts=True)

    if verbose:
        print(f'train data: {len(x_train)} validation: {len(x_validation)}')
        print(f'Dont buys: {train_counts[0]}, buys: {train_counts[1]}')
        print(f'VALIDATION Dont buys: {val_counts[0]}, buys: {val_counts[1]}')



    return x_train, y_train, x_validation, y_validation



def recurrent_net():
    return






stock_data = get_stock(stock_ticker, force_update=True)
x_train, y_train, x_validation, y_validation = preprocess_df(stock_data)
