import numpy as np

# Functions
def y0(t, A0, f0):
    return A0 * np.sin(2 * np.pi * f0 * t)

def y1(t, A0, A1, f0, f1):
    return y0(t, A0, f0) + y0(t, A1, f1)

def y2(t, A0, A1, f0, f1, T):
    output = np.zeros(len(t))
    for i in range(len(t)):
        if t[i] < T/2:
            output[i] = y0(t[i], A0, f0)
        else:
            output[i] = y0(t[i], A1, f1)
    return output


# DFTs and Co.

def dft(data):
    """
    Discrete Fourier transform of real data.
    Input : Time serie of size N
    Output : Time serie of size N//2+1
    """
    N = len(data)
    output = np.zeros(N, dtype=complex)
    for n in range(N):
        for j in range(N):
            output[n] += data[j] * np.exp(-2 * np.pi * 1j * n * j / N)
    return output[:int(N/2) + 1] / N

def fdft(data):
    """
    Fast discrete Fourier transform of real data with Numpy and matrix operations.
    Input: Time serie of size N
    Output: Time serie of size N//2+1
    """
    N = len(data)
    exp = np.exp(-2 * np.pi * 1j / N * np.dot(np.arange(N)[:,np.newaxis], np.arange(N)[np.newaxis,:]))
    output = np.dot(data, exp) / N
    return output[:N//2+1]

def dftfreq(N, T):
    """
    Returns frequency coordinates for the DFT functions.
    Input: Size of the time series, and time step.
    Output: Frequency serie of size N//2+1
    """
    N = int(N/2) + 1
    freq = np.zeros(N)
    for n in range(N):
        freq[n] = n/T
    return freq
