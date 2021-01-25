from parameters_and_imports import *
from data_reader import get_stock



df = pd.read_hdf(f'stock_data\\{stock_ticker}.h5')



def plot_close_price(data,
                plot_log=False,
                moving_avg=False,
                volume=False,
                save_plot=False):
    """
    Assumes a pandas dataframe is passed.
    """

    fig, ax = plt.subplots(
        sharex=True,
        sharey=True,
        figsize=(16, 10))
    ax.set_title(f'{stock_ticker} Pricing from: {start_date} to {todays_date}')
    second_axis = False

    tracker = ''
    if plot_log:
        plt.plot(np.log(data['Close']),
                label=f'{stock_ticker} log close price')
        #print('1')
        tracker += 'log'


    if volume:
        tracker += 'volume'
        ax2 = ax.twinx()
        volume_plot = sns.lineplot(x=data.index, y=data['Volume'],
                    linestyle='-',
                    label=f'{stock_ticker} volume',
                    color='forestgreen',
                    alpha=0.6,
                    ax=ax2,
                    legend=None)
        volume_plot.set_ylabel('')
        #coloring in below the volume graph
        ax2.fill_between(
            data.index.values,
            0,
            data['Volume'].values,
            alpha=0.3,
            color='forestgreen',
            label=None)
        ax2.set_ylim([0, ax2.get_ylim()[1] * 4])
        plt.grid(True)
        ax.xaxis.grid(True, which='minor')
        ax2.xaxis.grid(False)
        ax2.yaxis.grid(False)
        ax2.yaxis.set_ticklabels([])
        #print('2')


    if moving_avg:
        tracker += f'moving{moving_avg}'
        values = data['Close'].rolling(window=moving_avg,
                                        center=False).mean()
        avg_plot = sns.lineplot(x=data.index, y=values,
                    label=f'{moving_avg} days moving average',
                    color='lightcoral',
                    ax=ax)
        #print('3')


    data_plot = sns.lineplot(x=data.index, y=data['Close'],
                label=f'{stock_ticker} close price',
                color='steelblue',
                ax=ax)
    data_plot.set_xlabel('Date', fontsize=16)
    data_plot.set_ylabel('Close Price [$]', fontsize=16)
    print(tracker)

    if volume:
        handles, labels = ax.get_legend_handles_labels()
        handles2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(
            handles + handles2,
            labels + labels2,
            loc='upper left')
    else:
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(
            handles,
            labels,
            loc='upper left')

    if save_plot:
        plt.savefig(f'figures\\{stock_ticker}_{tracker}')



plot_close_price(df, plot_log=False, moving_avg=20, volume=True, save_plot=False)

plt.show()
