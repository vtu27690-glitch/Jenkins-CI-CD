
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

logs = [
    "ModuleNotFoundError no module named pandas",
    "ModuleNotFoundError no module named flask",
    "No module named numpy",
    "ImportError cannot import module",
    "ImportError failed to import package",

    "SyntaxError invalid syntax",
    "SyntaxError unexpected token",
    "IndentationError unexpected indent",
    "SyntaxError was never closed",

    "ConnectionError connection refused",
    "Connection timed out",
    "Failed to connect to server",
    "Network unreachable",

    "AssertionError test failed",
    "Unit test failed expected value",
    "Test case failure",
    "Assertion failed",
]

categories = [
    "ModuleNotFoundError",
    "ModuleNotFoundError",
    "ModuleNotFoundError",
    "ImportError",
    "ImportError",

    "SyntaxError",
    "SyntaxError",
    "SyntaxError",
    "SyntaxError",

    "ConnectionError",
    "ConnectionError",
    "ConnectionError",
    "ConnectionError",

    "AssertionError",
    "AssertionError",
    "AssertionError",
    "AssertionError",
]

model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(logs, categories)

joblib.dump(model, "failure_model.pkl")

print("ML model trained successfully!")