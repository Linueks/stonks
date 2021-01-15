from parameters_and_imports import *



df = pd.read_hdf(f'stock_data\\{stock_ticker}.h5')



def plot_close_price(data, plot_log=False, moving_avg=False, volume=False):
    """
    Assumes a pandas dataframe is passed.
    """


    if plot_log:
        plt.plot(np.log(data['Close']),
                label=f'{stock_ticker} log close price')

    else:
        if moving_avg:
            values = data['Close'].rolling(window=moving_avg,
                                            center=False).mean()
            sns.lineplot(x=data.index, y=values,
                        label=f'{moving_avg} days moving average',
                        color='lightcoral')


        if volume:
            fig, ax = plt.subplots(
                sharex=True,
                sharey=True,
                figsize=(16, 10))
            close_plot = sns.lineplot(x=data.index, y=data['Close'],
                        label=f'{stock_ticker} close price',
                        color='steelblue', ax=ax)
            close_plot.axes.set_title(f'Close Price of {stock_ticker}',
                                        fontsize=18)
            close_plot.set_xlabel('Date', fontsize=16)
            close_plot.set_ylabel('Close Price [$]', fontsize=16)
            ax2 = ax.twinx()
            volume_plot = sns.lineplot(x=data.index, y=data['Volume'],
                        label=f'{stock_ticker} volume',
                        color='forestgreen',
                        alpha=0.6,
                        ax=ax2)
            volume_plot.set_ylabel('')
            #coloring in below the volume graph
            ax2.fill_between(
                data.index.values,
                0,
                data['Volume'].values,
                alpha=0.3,
                color='forestgreen')
            ax2.set_ylim([0, ax2.get_ylim()[1] * 3])
            plt.grid(True)


            handles, labels = plt.gca().get_legend_handles_labels()
            new_labels, new_handles = [], []
            for handle, label in zip(handles, labels):
                if label not in new_labels:
                    new_labels.append(label)
                    new_handles.append(handle)


            lines = ax.get_lines() + ax2.get_lines() + new_handles


            ax.xaxis.grid(True, which='minor')
            ax2.xaxis.grid(False)
            ax2.yaxis.grid(False)
            ax2.yaxis.set_ticklabels([])



            """
            sns.displot(data['Volume'], len(data['Volume']),
                        density=True)
            sns.lineplot(x=data.index, y=data['Close'],
                        label=f'{stock_ticker} close price',
                        color='steelblue')
            """

        else:
            #plt.plot(data['Close'], label=f'{stock_ticker} price')
            sns.lineplot(x=data.index, y=data['Close'],
                        label=f'{stock_ticker} close price',
                        color='steelblue')

        plt.legend()



plot_close_price(df, volume=True)
plt.show()
