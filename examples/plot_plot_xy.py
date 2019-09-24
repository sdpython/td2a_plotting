"""
Example with sphinx-gallery
===========================

Simple example avec `sphinx-gallery
<https://github.com/sphinx-gallery/sphinx-gallery>`_.

Dummy example with `sphinx-gallery
<https://github.com/sphinx-gallery/sphinx-gallery>`_.
"""
import numpy
import matplotlib.pyplot as plt
from td2a_plotting import plot_xy

data1 = numpy.random.rand(200, 2)
data2 = numpy.random.rand(200, 2) + 2
data3 = numpy.random.rand(200, 2) + 2
data3[:, 1] += 1


fig, ax = plt.subplots(1, 2, figsize=(12, 4))

plot_xy(data1, ax=ax[0], label="D1")
plot_xy(data2, ax=ax[1], label="D2")
plot_xy(data3, ax=ax[1], label="D3")
ax[0].set_title("One curve.")
ax[1].set_title("Two curves on the same graphs.")

plt.show()
