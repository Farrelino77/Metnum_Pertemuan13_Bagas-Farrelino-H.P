import numpy as np
import time
import math
import matplotlib.pyplot as plt


# Fungsi untuk integrasi
def f(x):
    return 4 / (1 + x**2)

# Metode integrasi trapezoid
def trapezoid_integration(f, a, b, N):
    x = np.linspace(a, b, N+1)
    y = f(x)
    h = (b - a) / N
    integral = (h / 2) * np.sum(y[:-1] + y[1:])
    return integral

# Menghitung galat RMS
def rms_error(approximation, reference):
    return np.sqrt((approximation - reference) ** 2)

# Nilai referensi pi
pi_reference = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Hasil pengujian
results = []

for N in N_values:
    start_time = time.time()
    pi_approx = trapezoid_integration(f, 0, 1, N)
    end_time = time.time()
    error = rms_error(pi_approx, pi_reference)
    execution_time = end_time - start_time
    results.append((N, pi_approx, error, execution_time))

# Mencetak hasil pengujian
for N, pi_approx, error, execution_time in results:
    print(f"N: {N}, Pi Approximation: {pi_approx}, RMS Error: {error}, Execution Time: {execution_time}")

# Plotting hasil
Ns = [result[0] for result in results]
pis = [result[1] for result in results]
errors = [result[2] for result in results]
times = [result[3] for result in results]

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.plot(Ns, pis, marker='o')
plt.xscale('log')
plt.xlabel('N')
plt.ylabel('Estimated Pi')
plt.title('Estimated Pi vs N')

plt.subplot(1, 3, 2)
plt.plot(Ns, errors, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('RMS Error')
plt.title('RMS Error vs N')

plt.subplot(1, 3, 3)
plt.plot(Ns, times, marker='o')
plt.xscale('log')
plt.xlabel('N')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time vs N')

plt.tight_layout()
plt.show()
