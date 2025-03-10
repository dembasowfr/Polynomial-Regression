from process import data_processing, error_processing, polynomial_processing
import matplotlib.pyplot as plt

def main():
    """Main function to execute polynomial regression analysis."""
    # Load data
    x_train, r_train, x_test, r_test = data_processing.load_data("dataset/train.csv", "dataset/test.csv")
    
    # Degrees of polynomials to fit
    degrees = list(range(8))
    train_errors = []
    test_errors = []
    
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.flatten()
    
    for i, d in enumerate(degrees):
        poly_func = polynomial_processing.fit_polynomial(x_train, r_train, d)
        
        # Compute SSE
        sse_train = error_processing.compute_sse(r_train, poly_func(x_train))
        sse_test = error_processing.compute_sse(r_test, poly_func(x_test))
        
        train_errors.append(sse_train)
        test_errors.append(sse_test)
        
        # Plot polynomial fit
        polynomial_processing.plot_polynomial_fit(axes[i], x_train, r_train, poly_func, d)
    
    plt.tight_layout()
    plt.show()
    
    # Plot SSE vs. Degree
    error_processing.plot_sse_vs_degree(degrees, train_errors, test_errors)
    
    # Print SSE values
    for d, tr_err, te_err in zip(degrees, train_errors, test_errors):
        print(f"Degree {d}: Train SSE = {tr_err:.4f}, Test SSE = {te_err:.4f}")

if __name__ == "__main__":
    main()
