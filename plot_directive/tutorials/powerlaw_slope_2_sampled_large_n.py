# The first argument is equivalent to `size` from all
# numpy.random functions.
samples = pl.generate_random((1000000,))

pl.plot_pdf(label='Original PDF')
powerlaw.plot_pdf(samples, label='Sampled PDF')

plt.legend()
plt.show()