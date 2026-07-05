def secant(f, x0, x1, tol=1e-8, max_iter=50):
    """
    Find a root of f using the Secant method.
 
    Parameters
    ----------
    f   : function -> the function whose root we seek
    x0, x1 : float -> two initial guesses
    tol : float    -> convergence tolerance
    max_iter : int -> maximum number of iterations
 
    Returns
    -------
    root    : float
    history : list of x-values at each iteration (includes x0, x1)
    """
    history = [x0, x1]
    for i in range(max_iter):
        f0, f1 = f(x0), f(x1)
        if f1 - f0 == 0:
            raise ZeroDivisionError("Division by zero: f(x1) == f(x0).")
        x_new = x1 - f1 * (x1 - x0) / (f1 - f0)
        history.append(x_new)
        if abs(x_new - x1) < tol or abs(f(x_new)) < tol:
            return x_new, history
        x0, x1 = x1, x_new
    print("Secant: max iterations reached without full convergence.")
    return x_new, history