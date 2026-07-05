# Solution of Nonlinear Equations — Newton-Raphson & Secant

Coursework project (Algorithmic Mathematics, Assignment 1) that finds the real root of

$$x \log_{10}(x) = 1.2$$

using the **Newton-Raphson** and **Secant** methods, and compares how fast each one
converges. Running it produces a 3-panel figure showing the geometric construction of each
method and a log-scale error comparison.

## Problem

Solve `f(x) = x·log₁₀(x) − 1.2 = 0`. Both methods converge to

```
x ≈ 2.740646
```

correct to five decimal places. Starting from `x₀ = 404`, Newton-Raphson reaches the root in
**7 iterations**; the Secant method from the bracket `[2, 4]` takes **5 iterations**.

The full worked solutions, formulae, and iteration tables are in `documents/` (`assignment1.tex`,
`lab.tex`).

## Requirements

- Python 3.11 (see `.python-version`)
- [numpy](https://numpy.org/) and [matplotlib](https://matplotlib.org/)

## Setup

Using [uv](https://docs.astral.sh/uv/) (recommended — matches `pyproject.toml`):

```bash
uv sync
```

Or with pip:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

This prints the root and iteration count for each method, for example:

```
Newton-Raphson root: 2.7406460960  (7 iterations)
Secant root:         2.7406460960  (5 iterations)
```

and saves the comparison figure to `outputs/problem3_methods.pdf`. The figure has three panels:

1. **Newton-Raphson** — the curve with tangent-line steps down to the x-axis.
2. **Secant Method** — the curve with secant-line steps between successive points.
3. **Convergence comparison** — `|error|` vs. iteration on a log scale for both methods.

## Project structure

```
.
├── main.py                        # Wires the problem through both solvers + plots the figure
├── src/
│   ├── __init__.py                # Re-exports the public API (import from `src`)
│   ├── mathematical_model/
│   │   ├── newton_raph.py         # newton_raphson(f, df, x0, ...)
│   │   └── secant.py              # secant(f, x0, x1, ...)
│   └── visualizer/
│       └── graph.py               # plot_newton, plot_secant, plot_convergence
├── tex_files/                     # LaTeX write-ups (worked solutions)
└── outputs/                       # Generated figures (problem3_methods.pdf)
```

## API notes

Both solvers return a `(root, history)` tuple, where `history` is the list of x-values visited:

```python
from src import newton_raphson, secant

root, history = newton_raphson(f, df, x0, tol=1e-8, max_iter=50)
root, history = secant(f, x0, x1, tol=1e-8, max_iter=50)
```

The two histories follow slightly different conventions, which matters when counting iterations:

- **Newton** history includes the single initial guess `x0`, so the iteration count is
  `len(history) - 1`.
- **Secant** history includes both initial guesses `x0` and `x1`, so the iteration count is
  `len(history) - 2`.

The plotting helpers in `src/visualizer/graph.py` consume these history lists directly to draw
each method's construction.
