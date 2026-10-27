import powerlaw
import matplotlib.pyplot as plt

# Let's use the blackouts dataset
data = powerlaw.load_test_dataset('blackouts') / 1e3

fit = powerlaw.Fit(data)

fit.plot_pdf(label='Data (PDF)')
fit.power_law.plot_pdf(linestyle='--', label='Power law fit (PDF)')
fit.exponential.plot_pdf(linestyle='--', label='Exponential fit (PDF)')

plt.title('blackouts')
plt.legend()
plt.show()