import numpy as np

def calculate_Nyquist(bandwidth, signalization_levels):
    result = 2 * bandwidth * np.log2(signalization_levels)
    return result

def calculate_Shannon(bandwidth, signal_to_noise_ratio):
    result = bandwidth * np.log2(1 + signal_to_noise_ratio)
    return result

def main():
    bandwidth = 3000  # in Hz
    signalization_levels = 4  # e.g., for QPSK
    signal_to_noise_ratio = 10  # in linear scale

    nyquist_capacity = calculate_Nyquist(bandwidth, signalization_levels)
    shannon_capacity = calculate_Shannon(bandwidth, signal_to_noise_ratio)

    print(f"Nyquist Capacity: {nyquist_capacity} bits/second")
    print(f"Shannon Capacity: {shannon_capacity} bits/second")

if __name__ == "__main__":
    main()