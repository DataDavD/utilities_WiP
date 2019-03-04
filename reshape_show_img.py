import matplotlib.pyplot as plt
import numpy as np

def show_as_image(sample, shape):
    """ Function that takes image encoded as 1D array and reshapes it to
        the specified shape - must be specified as such (2,2). It then displays
        the image.
    """
    bitmap = sample.reshape((13, 8))
    plt.figure()
    plt.imshow(bitmap, cmap='gray', interpolation='nearest')
    plt.colorbar()
    plt.show()
