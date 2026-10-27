import powerlaw
import matplotlib.pyplot as plt

data = powerlaw.load_test_dataset('blackouts') / 1e3

# Apply a range on the possible values of alpha
fit = powerlaw.Fit(data, parameter_ranges={"alpha": [1, 2]})

# Now examine the xmin fitting results
plt.plot(fit.xmin_fitting_results["xmins"], fit.xmin_fitting_results["distances"], label='KS')
plt.plot(fit.xmin_fitting_results["xmins"], fit.xmin_fitting_results["alpha"], label='$\\alpha$')
plt.plot(fit.xmin_fitting_results["xmins"], fit.xmin_fitting_results["valid_fits"], label='Is valid fit?')

plt.axvline(fit.xmin, linestyle='--', c='black', label='Chosen $x_{min}$')

plt.xlabel('$x_{min}$')
plt.xscale('log')
plt.legend()
plt.show()