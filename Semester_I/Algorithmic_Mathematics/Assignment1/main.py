from src import secant, newton_raphson, plot_newton, plot_secant, plot_convergence
import matplotlib.pyplot as plt
import numpy as np

def main():
    LOG10E = 0.4342944819  # log10(e)
    f  = lambda x: x*np.log10(x) - 1.2
    df = lambda x: np.log10(x) + LOG10E
    true_root = 2.740646
 
    # Newton from x0 = 404 (as in the assignment)
    nr_root, nr_hist = newton_raphson(f, df, 404.0)
    # Secant from a sensible bracket near the root
    sc_root, sc_hist = secant(f, 404, 405)
 
    print(f"Newton-Raphson root: {nr_root:.10f}  ({len(nr_hist)-1} iterations)")
    print(f"Secant root:         {sc_root:.10f}  ({len(sc_hist)-2} iterations)") 
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    plot_newton(f, df, nr_hist, axes[0], x_range=(0.5, 5.0))
    plot_secant(f, sc_hist, axes[1], x_range=(0.5, 5.0))
    plot_convergence(nr_hist, sc_hist, true_root, axes[2])
    plt.tight_layout()
    fig.savefig("outputs/problem3_methods.pdf")
    plt.show()


if __name__ == "__main__":
    main()
