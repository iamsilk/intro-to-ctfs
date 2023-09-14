from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        expression = request.form["expression"]
        try:
            result = eval(expression)
        except Exception as e:
            result = f"Error: {str(e)}"
        return render_template("index.html", expression=expression, result=result)
    return render_template("index.html", expression=None, result=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)