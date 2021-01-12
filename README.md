My Python Notebooks
===================

![Python39](http://img.shields.io/badge/python-3.9-blue.svg?v=1)
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](./LICENSE)

Jupyter notebooks are version controlled as Markdown files thanks to Jupyter's plugin [Jupytext](https://jupytext.readthedocs.io/en/latest/).

## Install environment

`pip install -r requirements.txt`

## To run locally

`jupyter notebook`

## To view online

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pierre-dejoue/python-notebooks/master)

## To Convert to/from Markdown format

```
jupytext --to ipynb Circumcircle.md
jupytext --to md    Circumcircle.ipynb
```
