'''

     ####  ##    ######
    ##     ##      ##
    ##     ##      ##
    ##     ##      ##
     ####  #####   ##    (Maciej Workiewicz)

This simple simulation helps to develop intuition for the Central Limit
Theorem.

If you ever wondered how does the CLT really work, but didn't find the
mathematical proof enough, then you can try this Python script and see for
yourself how does the distribution of the sample of means change in response
to the change in the size of each sample. You can also vary the number of
the samples.

It is best to set the number of samples to a large number to get a better
representation of the distribution of sample means.

ver 1.1 (2014) Maciej Workiewicz
'''
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import norm

print ('''
Choose a distribution you want to sample from:
    0 - Uniform (0, 1)
    1 - Chi-square (df = 1)
    2 - Gamma (2, 2)
    3 - Laplace (1, 1)
    4 - Binomial (1, 0.1)
    5 - Poisson (5)
    ''')

a1 = int(raw_input('Distribution: '))
ns = int(raw_input('Number of samples: '))  # number of samples
ss = int(raw_input('Sample size (max = 1,000,000): '))  # sample size

'''
Population is set to 1 million

Feel free to play and change the values of the distributions or add
a new one.
'''

if a1 == 0:
    Population = np.random.rand(1000000)  # a vector
    d_name = 'Uniform U(0,1), n=1,000,000'
elif a1 == 1:
    Population = np.random.chisquare(1, 1000000)
    d_name = 'Chisquare (df=1), n=1,000,000)'
elif a1 == 2:
    Population = np.random.gamma(2, 2, 1000000)
    d_name = 'Gamma (2, 2), n=1,000,000)'
elif a1 == 3:
    Population = np.random.laplace(1, 1, 1000000)
    d_name = 'Laplace (1, 1), n=1,000,000)'
elif a1 == 4:
    Population = np.random.negative_binomial(1, 0.1, 1000000)
    d_name = 'Binomial (1, 0.1), n=1,000,000)'
elif a1 == 5:
    Population = np.random.poisson(5, 1000000)
    d_name = 'Poisson (5), n=1,000,000)'

Sample_means = np.zeros(ns)

for b1 in np.arange(ns):  # sample from population
    Sample = random.sample(Population, ss)
    s_mean = np.mean(Sample)
    Sample_means[b1] = s_mean

s_s_mean = np.mean(Sample_means)

'''
Now we will plot a histogram of the population to see how does the original
density function look like and plot the histogram of the distribution of the
sample means.

I also fitted a normal distribution to show how should the distribution
of the sample means look like if the sample size went to infinity.
'''

plt.figure(1, facecolor='white', figsize=(8.2, 11.2))
plt.suptitle('Central Limit Theorem: '+d_name, size=14)
plt.subplots_adjust(hspace=.5)
plt.subplot(211)
plt.hist(Population, bins=20, rwidth=0.8, alpha=0.6)
plt.title('Histogram of the population, size=1,000,000', size=11)

plt.subplot(212)
x = np.arange(0, 2+s_s_mean, 0.01)
plt.hist(Sample_means, bins=20, normed=1, rwidth=0.8, alpha=0.6)
plt.plot(x, norm.pdf(x, *norm.fit(Sample_means)), color='green')
plt.title('Histogram of the sample means, sample size = ' + str(ss) +
          ', number of samples = ' + str(ns), size=11)

plt.show()
