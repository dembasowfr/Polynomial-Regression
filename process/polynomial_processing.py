import numpy as np
import matplotlib.pyplot as plt


def fit_polynomial(x_train, r_train, degree):
    """Fit a polynomial of given degree and return the polynomial function."""
    coeffs = np.polyfit(x_train, r_train, degree)
    return np.poly1d(coeffs)


def plot_polynomial_fit(ax, x_train, r_train, poly_func, degree):
    """Plot the polynomial fit along with training data on the given axis."""
    x_range = np.linspace(min(x_train), max(x_train), 100)
    ax.scatter(x_train, r_train, label="Training Data", color="blue")
    ax.plot(x_range, poly_func(x_range), label=f"Degree {degree} Fit", color="red")
    ax.set_xlabel("x")
    ax.set_ylabel("r")
    ax.set_title(f"Degree {degree}")
    ax.legend()