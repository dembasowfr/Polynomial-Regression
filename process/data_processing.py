import pandas as pd


def load_data(train_path, test_path):
    """Load and preprocess training and test datasets."""
    train_data = pd.read_csv(train_path, header=None, names=["x", "r"])
    test_data = pd.read_csv(test_path, header=None, names=["x", "r"])
    
    train_data = train_data.apply(pd.to_numeric, errors='coerce').dropna()
    test_data = test_data.apply(pd.to_numeric, errors='coerce').dropna()
    
    return train_data["x"].values, train_data["r"].values, test_data["x"].values, test_data["r"].values