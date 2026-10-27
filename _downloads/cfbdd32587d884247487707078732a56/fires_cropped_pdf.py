import powerlaw
import matplotlib.pyplot as plt

xmin = 10
xmax = 1e4

data = powerlaw.load_test_dataset('fires')

fit = powerlaw.Fit(data, xmin=xmin, xmax=xmax)

fit.plot_pdf(label='Cropped PDF')
fit.plot_pdf(original_data=True, label='Full PDF')

plt.title('fires')
plt.legend()
plt.show()