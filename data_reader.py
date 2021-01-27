from parameters_and_imports import *





def get_stock(df, force_update=False):


    if force_update==True:
        print('Force update')
        df = web.DataReader(stock_ticker, data_source='google', start=start_date,
                            end=todays_date)
        df['Daily Return'] = df['Adj Close'].pct_change(periods=1)
        df.to_hdf(f'stock_data\{stock_ticker}.h5', key='df')

    try:
        with open(f'stock_data\{stock_ticker}.h5') as f:
            print('Local')
            time_since = os.path.getmtime(f.name)
            time_since_days = np.round(time_since / 8.64e7, 2)

            if time_since_days > 7:
                print(f'{time_since_days} days since last update, consider running with force_update=True')
            df = pd.read_hdf(f.name)

    except FileNotFoundError:
        print('FileNotFoundError')
        df = web.DataReader(stock_ticker, data_source='yahoo', start=start_date,
                            end=todays_date)
        df['Daily Return'] = df['Adj Close'].pct_change()
        df.to_hdf(f'stock_data\\{stock_ticker}.h5', key='df')
        print('hallo')

    finally:
        return df




if __name__=='__main__':
    get_stock()
