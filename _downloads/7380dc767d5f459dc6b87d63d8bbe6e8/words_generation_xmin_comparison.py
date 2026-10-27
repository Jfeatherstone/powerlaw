import powerlaw
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
num_samples = 10000

data = powerlaw.load_test_dataset('words')

fig, ax = plt.subplots(1, 2, figsize=(10, 4.5))

fit = powerlaw.Fit(data, xmin=1, xmax=1e5, discrete=True, estimate_discrete=True)
samples = fit.power_law.generate_random(size=num_samples)

fit.plot_pdf(label='Original data', ax=ax[0])

powerlaw.plot_pdf(samples, label='Sampled data \nestimate_discrete=True', ax=ax[0])

fit = powerlaw.Fit(data, xmin=1, xmax=1e5, discrete=True, estimate_discrete=False)
samples = fit.power_law.generate_random(size=num_samples)

powerlaw.plot_pdf(samples, label='Sampled data \nestimate_discrete=False', ax=ax[0])

ax[0].set_title('xmin = 1')
ax[0].legend(fontsize=12)

fit = powerlaw.Fit(data, xmin=10, xmax=1e5, discrete=True, estimate_discrete=True)
samples = fit.power_law.generate_random(size=num_samples)

fit.plot_pdf(label='Original data', ax=ax[1])

powerlaw.plot_pdf(samples, label='Sampled data \nestimate_discrete=True', ax=ax[1])

fit = powerlaw.Fit(data, xmin=10, xmax=1e5, discrete=True, estimate_discrete=False)
samples = fit.power_law.generate_random(size=num_samples)

powerlaw.plot_pdf(samples, label='Sampled data \nestimate_discrete=False', ax=ax[1])

ax[1].set_title('xmin = 10')
ax[1].legend(fontsize=12)

fig.suptitle('words')
fig.tight_layout()
plt.show()