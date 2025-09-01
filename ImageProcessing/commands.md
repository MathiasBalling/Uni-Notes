# Jupyter notebook from nvim

## Syntax

```python
# py:percent format

# %% [markdown]
# This is a markdown cell

# %%
# This is a python cell
def f(x):
  return 3*x+1
```

## Usage

This makes a pair of synced py and ipynb files, `<name>.sync.py` and `<name>.sync.ipynb`.

```bash
python -m jupyter_ascending.scripts.make_pair --base <name>
```

Start jupyter and open the notebook:

```bash
python -m jupyter notebook <name>.sync.ipynb
```

Convert `<name>.ipynb` to `<name>.py` in py percent format

```bash
jupytext --to py:percent <name>.ipynb
```

Sync the code into the jupyter notebook (without nvim plugin):

```bash
python -m jupyter_ascending.requests.sync --filename <name>.sync.py
```

Run that cell of code (without nvim plugin):

```bash
python -m jupyter_ascending.requests.execute --filename <name>.sync.py --line 16
```

## Installation

```bash
pip install jupyter_ascending && \
python -m jupyter nbextension     install jupyter_ascending --sys-prefix --py && \
python -m jupyter nbextension     enable jupyter_ascending --sys-prefix --py && \
python -m jupyter serverextension enable jupyter_ascending --sys-prefix --py
```

You can confirm it's installed by checking for `jupyter_ascending` in:

```bash
python -m jupyter nbextension     list
python -m jupyter serverextension list
```

If your jupyter setup includes multiple python kernels that you'd like to use with jupyter ascending, you'll need to complete this setup in each of those python environments separately.

Refer:
[jupyter_ascending/README.md at main · imbue-ai/jupyter_ascending](https://github.com/imbue-ai/jupyter_ascending/blob/main/README.md)
