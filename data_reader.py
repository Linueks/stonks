from parameters_and_imports import *



def get_stock():
    try:
        with open(f'stock_data\\{stock_ticker}') as f:
            df = pd.read_hdf(f)

    except IOError:
        df = web.DataReader(stock_ticker, data_source='yahoo', start=start_date,
                            end=todays_date)
        df['Daily Return'] = df['Adj Close'].pct_change()
        df.to_hdf(f'stock_data\\{stock_ticker}.h5', key='df')

    finally:
        return df
