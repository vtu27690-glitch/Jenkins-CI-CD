
from flask import Flask, request, render_template_string
import joblib
import os

app = Flask(__name__)
model = joblib.load("failure_model.pkl")

def analyze_error(log):
    prediction = model.predict([log])[0]
    probabilities = model.predict_proba([log])[0]
    confidence = round(max(probabilities) * 100, 2)

    solutions = {
        "ModuleNotFoundError": "Install the missing Python package using pip.",
        "SyntaxError": "Check Python syntax, brackets, indentation and spelling.",
        "ImportError": "Check import statements and installed packages.",
        "ConnectionError": "Check network connection and server availability.",
        "PermissionError": "Check file permissions and access rights.",
        "AssertionError": "Check the failed test case and expected output."
    }

    return {
        "error": prediction,
        "solution": solutions.get(prediction, "Review the Jenkins build log."),
        "confidence": confidence
    }

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>CI/CD AI Monitor</title>
<style>
body {
    background: #101827;
    color: white;
    font-family: Arial;
    text-align: center;
    padding: 35px;
}
h1 { color: #38bdf8; }
.card {
    background: #1e293b;
    padding: 25px;
    margin: 25px auto;
    border-radius: 12px;
    max-width: 700px;
}
textarea {
    width: 90%;
    height: 130px;
    padding: 12px;
    border-radius: 8px;
}
button {
    background: #0284c7;
    color: white;
    padding: 12px 25px;
    border: none;
    border-radius: 7px;
    cursor: pointer;
    margin-top: 15px;
}
.result {
    background: #334155;
    padding: 18px;
    margin-top: 20px;
    border-radius: 8px;
    text-align: left;
}
</style>
</head>
<body>

<h1>CI/CD Build Failure Notification System</h1>

<div class="card">
<h2>AI Build Failure Analysis</h2>
<p>Paste your Jenkins build error log below.</p>

<form method="POST">
<textarea name="log" placeholder="Paste build error log here..."
required></textarea><br>
<button type="submit">Analyze Build Failure</button>
</form>

{% if result %}
<div class="result">
    <h3>AI Analysis Result</h3>

    <p><b>Predicted Error:</b> {{ result.error }}</p>

    <p><b>Suggested Solution:</b> {{ result.solution }}</p>

    <p><b>ML Confidence:</b> {{ result.confidence }}%</p>
</div>
{% endif %}

</div>
</body>
</html>
"""
@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        log = request.form.get("log", "").strip()

        if log:
            result = analyze_error(log)
        else:
            result = {
                "error": "No Log Provided",
                "solution": "Please paste a Jenkins build error log.",
                "confidence": 0
            }

    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(debug=True)



    

