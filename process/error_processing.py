import matplotlib.pyplot as plt
import numpy as np


def compute_sse(actual, predicted):
    """Compute the Sum of Squared Errors (SSE)."""
    return np.sum((actual - predicted) ** 2)


def plot_sse_vs_degree(degrees, train_errors, test_errors):
    """Plot SSE values against polynomial degrees."""
    plt.figure(figsize=(6, 4))
    plt.plot(degrees, train_errors, label="Train SSE", marker="o", color="blue")
    plt.plot(degrees, test_errors, label="Test SSE", marker="o", color="red")
    plt.xlabel("Polynomial Degree")
    plt.ylabel("Sum of Squared Errors (SSE)")
    plt.title("SSE vs. Polynomial Degree")
    plt.legend()
    plt.show()