from parameters_and_imports import *

dt = 0.1


def fourier_analysis(signal):
    fourier_transform = np.fft.fft(signal) / len(signal)
    frequency_range = np.fft.fftfreq(len(signal), dt)


    return fourier_transform, frequency_range



#get the stock quote
stock_data = web.DataReader(stock_ticker, data_source='yahoo', start=start_date,
                    end=todays_date)

number_of_points = len(stock_data['Close'].values)

fourier_coeffs, fourier_frequencies = fourier_analysis(stock_data['Close'].values)


plt.plot(fourier_frequencies[:number_of_points],
            np.abs(fourier_coeffs[:number_of_points]), c='indianred')
plt.xlabel('frequency [Hz]')
plt.ylabel('|X(f)| Fourier Coefficients')
plt.show()
