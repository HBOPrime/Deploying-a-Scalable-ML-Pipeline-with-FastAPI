import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from ml.model import train_model, compute_model_metrics, inference
from ml.data import apply_label

# TODO: implement the first test. Change the function name and input as needed
def test_model_type():
    """
    Ensure that the model type being used is RandomForest
    """
    X = np.random.rand(50, 4)
    y = np.random.randint(0, 2, size=50)
    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier)

# TODO: implement the second test. Change the function name and input as needed
def test_model_metrics():
    """
    Test that metrics returned are valid
    """
    X = np.random.rand(30, 3)
    y = np.random.randint(0, 2, size=30)
    model = train_model(X, y)
    preds = inference(model, X)
    pr, re, fb = compute_model_metrics(y, preds)
    assert isinstance(pr, float)
    assert isinstance(re, float)
    assert isinstance(fb, float)
    assert 0.0 <= pr <= 1.0
    assert 0.0 <= re <= 1.0
    assert 0.0 <= fb <= 1.0

# TODO: implement the third test. Change the function name and input as needed
def test_apply_label():
    """
    Test that the expected outputs from the tests are returned
    """
    expected_outputs = {'>50K','<=50K'}
    assert apply_label([1]) in expected_outputs
    assert apply_label([0]) in expected_outputs
