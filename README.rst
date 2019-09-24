
.. image:: https://circleci.com/gh/sdpython/td2a_plotting/tree/master.svg?style=svg
    :target: https://circleci.com/gh/sdpython/td2a_plotting/tree/master

td2a_plotting
=============

.. image:: https://raw.githubusercontent.com/sdpython/td2a_plotting/master/doc/_static/logo.png
    :width: 50

Simple template to package plotting functions. Material for teaching
`ensae_teaching_cs <https://github.com/sdpython/ensae_teaching_cs>`_.
It implements basic CI and documentation. One example of use:
`plot_plot_xy.py
<https://github.com/sdpython/td2a_plotting/blob/master/examples/plot_plot_xy.py>`_.

Generate the setup in subfolder ``dist``:

::

    python setup.py sdist

Generate the documentation in folder ``dist/html``:

::

    python -m sphinx -T -b html doc dist/html

Run the unit tests:

::

    python -m unittest discover tests examples

Or:

::

    python -m pytest
    
To check style:

::

    python -m flake8 td2a_plotting tests
