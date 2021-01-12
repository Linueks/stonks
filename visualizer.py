from parameters_and_imports import *



df = pd.read_hdf(f'stock_data\\{stock_ticker}.h5')



def plot_close_price(data, plot_log=False, moving_avg=False):
    """
    Assumes a pandas dataframe is passed.
    """

    plt.title(f'Historical Price {stock_ticker}')
    plt.xlabel('Date')
    plt.ylabel('USD ($)')


    if plot_log:
        plt.plot(np.log(data['Close']))

    else:
        if moving_avg:
            values = data['Close'].rolling(window=moving_avg,
                                            center=False).mean()
            plt.plot(values, label=f'{moving_avg} days moving average')
        else:
            pass


        plt.plot(data['Close'], label=f'{stock_ticker} price')
        plt.legend()



plot_close_price(df, moving_avg=20)
plt.show()
