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

Start jupyter and open the notebook:

```bash
jupyter notebook <name>.ipynb
```

Convert `<name>.ipynb` to `<name>.py` in py percent format

```bash
jupytext --to py:percent <name>.ipynb
```
