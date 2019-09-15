"""
Simple plotting function as a template.
"""
import numpy


def plot_xy(data, label=None, markersize=4, color=None, ax=None, **kwargs):
    """
    Plots a simple cloud of points :math:`(X_i, Y_i)`.

    :param data: matrices, first column is X, second column i Y
    :param label: name of the curve
    :param marker_size: marker size
    :param color: color
    :param ax: existing axis
    :param kwargs: additional arguements for function
        `plot <https://matplotlib.org/3.1.0/api/_as_gen/
        matplotlib.pyplot.plot.html>`_
    :return: axis

    One example of this simple graph:

    .. plot::

        import numpy
        import matplotlib.pyplot as plt
        from td2a_plotting import plot_xy

        fig, ax = plt.subplots(1, 1)
        data = numpy.random.rand(10, 2)
        plot_xy(data, ax=ax)
        plt.show()
    """
    if not isinstance(data, numpy.ndarray):
        raise TypeError("data must be an array not {}".format(type(data)))
    if len(data.shape) != 2:
        raise ValueError(
            "data must be a matrix but shape is {}".format(data.shape))
    if data.shape[1] != 2:
        raise ValueError("data must be a matrix with two columns shape is {}"
                         "".format(data.shape))
    if ax is None:
        import matplotlib.pyplot as plt
        ax = plt.gca()

    ax.plot(data[:, 0], data[:, 1], '.', markersize=markersize,
            color=color, label=label, **kwargs)
    if label is not None:
        ax.legend()
    return ax
