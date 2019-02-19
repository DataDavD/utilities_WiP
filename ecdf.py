import numpy as np
import matplotlib.pyplot as plt

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
	n = len(data)

    # x-data for the ECDF: x
	x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    # Get percentiles:
    # Specify array of percentiles: percentiles
    percentiles = np.array([2.5, 25, 50, 75, 97.5])

    # Compute percentiles: ptiles_vers
    ptiles = np.percentile(data, percentiles)

    # plot the ECDF with percentiles marked as red diamonds
    plt.plot(x, y, marker='.', linestyle='none')
    plt.ylabel('ECDF')
    plt.xlabel('X')
    plt.plot(ptiles,
             percentiles/100,
             marker='D',
             color='red',
             linestyle='none')
    plt.show()

    # return x, y arrays
    return x, y
