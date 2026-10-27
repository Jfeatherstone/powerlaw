import powerlaw
import matplotlib.pyplot as plt

# Any of these are fine to create a power law with a specific
# alpha value.
pl = powerlaw.Power_Law(xmin=1, xmax=1e3, alpha=2.0)

pl.plot_pdf(label='PDF')

samples = pl.generate_random((10000,))

powerlaw.plot_pdf(samples, label='Sampled PDF')

plt.legend()
plt.show()