import powerlaw
import matplotlib.pyplot as plt

xmin = 10
xmax = 1e4

data = powerlaw.load_test_dataset('fires')
fit = powerlaw.Fit(data, xmin=xmin, xmax=xmax)

fig, ax = plt.subplots(1, 2, figsize=(9, 4))

fit.plot_pdf(label='Cropped PDF', ax=ax[0])
fit.plot_pdf(original_data=True, label='Full PDF', ax=ax[0])
ax[0].legend()

fit.plot_ccdf(label='Cropped CCDF', ax=ax[1])
fit.plot_ccdf(original_data=True, label='Full CCDF', ax=ax[1])
ax[1].legend()

fig.suptitle('fires')
fig.tight_layout()
plt.show()