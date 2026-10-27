import powerlaw
import matplotlib.pyplot as plt

data = powerlaw.load_test_dataset('blackouts') / 1e3

fit = powerlaw.Fit(data)

# Now examine the xmin fitting results
plt.plot(fit.xmin_fitting_results["xmins"], fit.xmin_fitting_results["distances"], label='KS')
plt.plot(fit.xmin_fitting_results["xmins"], fit.xmin_fitting_results["alpha"], label='$\\alpha$')
plt.plot(fit.xmin_fitting_results["xmins"], fit.xmin_fitting_results["valid_fits"], label='Is valid fit?')

plt.axvline(fit.xmin, linestyle='--', c='black', label='Chosen $x_{min}$')

plt.xlabel('$x_{min}$')
plt.xscale('log')
plt.legend()
plt.show()