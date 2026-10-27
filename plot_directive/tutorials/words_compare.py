import powerlaw
import matplotlib.pyplot as plt

# Let's use the words dataset
data = powerlaw.load_test_dataset('words')

# Remember this is a discrete dataset
fit = powerlaw.Fit(data, discrete=True)

fit.plot_pdf(label='Data (PDF)')
fit.power_law.plot_pdf(linestyle='--', label='Power law fit (PDF)')
fit.exponential.plot_pdf(linestyle='--', label='Exponential fit (PDF)')

plt.title('words')
plt.ylim([1e-10, 1e1])
plt.legend()
plt.show()