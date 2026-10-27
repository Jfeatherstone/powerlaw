import powerlaw
import matplotlib.pyplot as plt

data = powerlaw.load_test_dataset('words')

# These accept matplotlib plot keywords like 'label'
powerlaw.plot_pdf(data, label='PDF')
powerlaw.plot_cdf(data, label='CDF')
powerlaw.plot_ccdf(data, label='CCDF')

plt.title('words')
plt.legend()
plt.show()