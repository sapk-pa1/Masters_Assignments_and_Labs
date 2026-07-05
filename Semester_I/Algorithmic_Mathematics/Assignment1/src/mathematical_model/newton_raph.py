def newton_raphson(f, df, x0, tol=1e-8, max_iter=50):
    """
    Find a root of f using the Newton-Raphson method.
 
    Parameters
    ----------
    f   : function            -> the function whose root we seek
    df  : function            -> derivative of f
    x0  : float               -> initial guess
    tol : float               -> convergence tolerance on |f(x)|
    max_iter : int            -> maximum number of iterations
 
    Returns
    -------
    root    : float
    history : list of x-values at each iteration (includes x0)
    """
    history = [x0]
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ZeroDivisionError(f"Zero derivative at x = {x}. No update possible.")
        x_new = x - fx / dfx
        history.append(x_new)
        if abs(x_new - x) < tol or abs(f(x_new)) < tol:
            return x_new, history
        x = x_new
    print("Newton-Raphson: max iterations reached without full convergence.")
    return x, history
 