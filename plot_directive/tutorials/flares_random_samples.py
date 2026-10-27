import powerlaw
import matplotlib.pyplot as plt

data = powerlaw.load_test_dataset('flares')

# Note: no xmax, so the samples will be unbounded
fit = powerlaw.Fit(data)
samples = fit.power_law.generate_random((10000,))

fit.plot_pdf(label='Original PDF')
powerlaw.plot_pdf(samples, label='Sampled PDF')

plt.title('flares')
plt.legend()
plt.show()