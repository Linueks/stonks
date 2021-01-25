from parameters_and_imports import *





def get_stock(force_update=True):


    if force_update:
        df = web.DataReader(stock_ticker, data_source='yahoo', start=start_date,
                            end=todays_date)
        df['Daily Return'] = df['Adj Close'].pct_change()
        df.to_hdf(f'stock_data\{stock_ticker}.h5', key='df')

    try:
        with open(f'stock_data\{stock_ticker}.h5') as f:
            time_since = os.path.getmtime(f)
            time_since_days = np.round(time_since / 8.64e7, 2)

            if time_since_days > 7:
                print(f'{time_since_days} since last update, consider running\
                        with force_update=True')
            df = pd.read_hdf(f)

    except FileNotFoundError:
        df = web.DataReader(stock_ticker, data_source='yahoo', start=start_date,
                            end=todays_date)
        df['Daily Return'] = df['Adj Close'].pct_change()
        df.to_hdf(f'stock_data\\{stock_ticker}.h5', key='df')
        print('hallo')

    finally:
        return df




if __name__=='__main__':
    get_stock()
