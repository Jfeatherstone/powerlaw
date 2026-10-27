import powerlaw
import matplotlib.pyplot as plt

# Divide by 1e3 prefactor to give people in thousands
data = powerlaw.load_test_dataset('blackouts') / 1e3

fig, ax = plt.subplots(1, 3, figsize=(12, 3.5))

# We can specify the specific axis we want to plot on for more
# complicated figures like this one.
powerlaw.plot_pdf(data, linear_bins=False, ax=ax[0])
ax[0].set_title('log bins, log scale')
ax[0].set_xscale('log')

powerlaw.plot_pdf(data, linear_bins=True, ax=ax[1])
ax[1].set_title('linear bins, linear scale')
ax[1].set_xscale('linear')

powerlaw.plot_pdf(data, linear_bins=True, ax=ax[2])
ax[2].set_title('linear bins, log scale')
ax[2].set_xscale('log')

fig.tight_layout()
plt.show()