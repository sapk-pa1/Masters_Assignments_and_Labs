import numpy as np 
import matplotlib.pyplot as plt 



def plot_newton(f, df, history, ax, x_range):
    xs = np.linspace(*x_range, 400)
    ax.plot(xs, f(xs), 'b-', lw=2, label='f(x)')
    ax.axhline(0, color='gray', lw=1)
 
    for i in range(len(history) - 1):
        x = history[i]
        fx, dfx = f(x), df(x)
        x_next = history[i + 1]
        # tangent line from (x, f(x)) down to the x-axis at x_next
        ax.plot([x, x], [0, fx], 'g--', lw=1, alpha=0.6)
        ax.plot([x, x_next], [fx, 0], 'r-', lw=1.2, alpha=0.8)
        ax.plot(x, fx, 'ko', ms=5)
        ax.annotate(f'$x_{i}$', (x, 0), textcoords="offset points",
                    xytext=(0, -15), ha='center', fontsize=9)
 
    root = history[-1]
    ax.plot(root, 0, 'r*', ms=16, label=f'root ≈ {root:.6f}')
    ax.set_title(f'Newton-Raphson ({len(history) - 1} iterations)')
    ax.legend()
    ax.grid(alpha=0.3)
 
 
def plot_secant(f, history, ax, x_range):
    xs = np.linspace(*x_range, 400)
    ax.plot(xs, f(xs), 'b-', lw=2, label='f(x)')
    ax.axhline(0, color='gray', lw=1)
 
    for i in range(len(history) - 2):
        x0, x1 = history[i], history[i + 1]
        f0, f1 = f(x0), f(x1)
        x2 = history[i + 2]
        # secant line through (x0, f0) and (x1, f1), extended to axis
        ax.plot([x0, x1], [f0, f1], 'r-', lw=1.2, alpha=0.8)
        ax.plot([x1, x2], [f1, 0], 'r-', lw=1.2, alpha=0.4)
        ax.plot([x0, x1], [f0, f1], 'ko', ms=5)
 
    root = history[-1]
    ax.plot(root, 0, 'r*', ms=16, label=f'root ≈ {root:.6f}')
    ax.set_title(f'Secant Method ({len(history) - 2} iterations)')
    ax.legend()
    ax.grid(alpha=0.3)
 
 
def plot_convergence(newton_hist, secant_hist, true_root, ax):
    n_err = [abs(x - true_root) for x in newton_hist]
    s_err = [abs(x - true_root) for x in secant_hist]
    ax.semilogy(range(len(n_err)), n_err, 'o-', label='Newton-Raphson')
    ax.semilogy(range(len(s_err)), s_err, 's-', label='Secant')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('|error|  (log scale)')
    ax.set_title('Convergence comparison')
    ax.legend()
    ax.grid(alpha=0.3, which='both')