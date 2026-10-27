import powerlaw
import matplotlib.pyplot as plt

# Let's use the words dataset
data = powerlaw.load_test_dataset('words')

# Remember this is a discrete dataset
fit = powerlaw.Fit(data, discrete=True)

fit.plot_pdf(label='Data (PDF)')
fit.power_law.plot_pdf(linestyle='--', label='Power law fit (PDF)')
fit.lognormal.plot_pdf(linestyle='--', label='Lognormal fit (PDF)')

plt.title('words')
plt.legend()
plt.show()