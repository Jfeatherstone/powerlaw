import powerlaw
import matplotlib.pyplot as plt

data = powerlaw.load_test_dataset('fires')

# verbose=0 hides a progress bar; by default it will show
fit = powerlaw.Fit(data, verbose=0)

# Plot the distributions based on the data
# No need to pass the data since the Fit already has it
fit.plot_pdf(label='PDF')

# Plot some fits
fit.power_law.plot_pdf(linestyle='--', label='Power law fit')
fit.exponential.plot_pdf(linestyle='--', label='Exponential fit')

plt.title('fires')
plt.legend()
plt.show()