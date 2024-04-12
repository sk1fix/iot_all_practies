import numpy as np

def f(t, v):
    return np.sin(v * np.cos(2 * np.pi * t))

def spectral_weight(freq, v):
    t = np.linspace(0, 10, 100) 
    signal = f(t, v)
    spectrum = np.abs(np.fft.fft(signal))
    freq_index = int(freq * len(t))
    return spectrum[freq_index]

def find_max_spectrum_freq(v):
    t = np.linspace(0, 100,100)  
    freqs = np.fft.fftfreq(len(t))
    signal = f(t, v)
    spectrum = np.abs(np.fft.fft(signal))
    max_freq_index = np.argmax(spectrum)
    max_freq = freqs[max_freq_index]
    return max_freq

v = float(input("Введите значение v: "))

max_freq = find_max_spectrum_freq(v)
print("Неотрицательная частота с максимальным спектральным весом:", max_freq)