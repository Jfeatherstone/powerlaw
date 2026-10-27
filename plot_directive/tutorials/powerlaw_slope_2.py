import powerlaw
import matplotlib.pyplot as plt

# Any of these are fine to create a power law with a specific
# alpha value.
pl = powerlaw.Power_Law(xmin=1, parameters={'alpha': 2.0})
pl = powerlaw.Power_Law(xmin=1, parameters=[2.0])
pl = powerlaw.Power_Law(xmin=1, alpha=2.0)

pl.plot_pdf(label='PDF')
pl.plot_ccdf(label='CCDF')

plt.legend()
plt.show()