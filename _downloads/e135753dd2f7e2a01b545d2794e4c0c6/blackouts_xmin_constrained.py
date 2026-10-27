import powerlaw
import matplotlib.pyplot as plt

data = powerlaw.load_test_dataset('blackouts') / 1e3

def constraint(dist):
    N = 100
    return len(dist.data) - N

constraint_dict = {"type": 'ineq',
                   "fun": constraint,
                   "dists": ['power_law']}

fit = powerlaw.Fit(data, parameter_constraints=constraint_dict)

plt.plot(fit.xmin_fitting_results["xmins"], fit.xmin_fitting_results["distances"], label='KS distance')
plt.plot(fit.xmin_fitting_results["xmins"], fit.xmin_fitting_results["valid_fits"], label='Is valid fit')

plt.axvline(fit.xmin, linestyle='--', c='black', label='Optimal $x_{min}$')

plt.xlabel('$x_{min}$')
plt.xscale('log')
plt.legend()
plt.show()