import powerlaw
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

alpha_arr = np.linspace(0.5, 2.5, 100)
num_samples = 10 # per alpha value
N = 3000

fit_alpha_arr = np.zeros((len(alpha_arr), num_samples))

for i in range(len(alpha_arr)):
    for j in range(num_samples):
        theoretical_dist = powerlaw.Power_Law(xmin=1, xmax=1e6, alpha=alpha_arr[i])
        data = theoretical_dist.generate_random(N)

        fit = powerlaw.Fit(data, xmin=1, xmax=np.max(data))

        fit_alpha_arr[i,j] = fit.power_law.alpha

for i in range(len(alpha_arr)):
    plt.scatter(np.repeat(alpha_arr[i], num_samples), fit_alpha_arr[i], alpha=0.1, c='tab:blue')

plt.plot(alpha_arr, alpha_arr, '--', c='tab:orange', label='$y=x$')

plt.xlabel('True alpha')
plt.ylabel('Fit alpha')

plt.title('Continuous power law validation')
plt.legend()
plt.show()