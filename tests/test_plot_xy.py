"""
Unit tests for ``plot_xy``.
"""
import unittest
import numpy
import matplotlib.pyplot as plt
from td2a_plotting import plot_xy


class TestPlotxy(unittest.TestCase):
    "Tests for submodule plot_xy"

    def test_bad_cases(self):
        with self.assertRaises(TypeError):
            data = []
            plot_xy(data)
        with self.assertRaises(ValueError):
            data = numpy.random.rand(10, 3, 2)
            plot_xy(data)
        with self.assertRaises(ValueError):
            data = numpy.random.rand(10, 3)
            plot_xy(data)

    def test_graph(self):
        plt.gca()
        fig, ax = plt.subplots(1, 1)
        data = numpy.random.rand(10, 2)
        plot_xy(data, ax=ax)
        plt.clf()

    def test_graph_noax(self):
        data = numpy.random.rand(10, 2)
        ax = plot_xy(data)
        self.assertTrue("Axes" in str(ax))
        plt.clf()

    def test_graph_label(self):
        data = numpy.random.rand(10, 2)
        ax = plot_xy(data, label="data")
        self.assertTrue("Axes" in str(ax))
        plt.clf()


if __name__ == '__main__':
    unittest.main()
