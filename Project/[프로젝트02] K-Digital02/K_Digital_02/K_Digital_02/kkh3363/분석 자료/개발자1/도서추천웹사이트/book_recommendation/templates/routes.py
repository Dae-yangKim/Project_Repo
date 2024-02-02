from flask import Flask, render_template, url_for, request

@app.route("/")
@app.route("/index")
def index_func():
    return render_template("index.html", title="Home")

@app.route("/somepage", methods=["GET", "POST"])
def some_func():
    form_data = request.form

    if request.method == "POST":
        num1 = int(form_data["number1"])
        num2 = int(form_data["number2"])
        if form_data["button"] == "add":
            return render_template(
                "somepage.html", title="SomePage", result=num1 + num2
            )
        if form_data["button"] == "sub":
            return render_template(
                "somepage.html", title="SomePage", result=num1 - num2
            )
        if form_data["button"] == "mul":
            return render_template(
                "somepage.html", title="SomePage", result=num1 * num2
            )
        if form_data["button"] == "div":
            return render_template(
                "somepage.html", title="SomePage", result=num1 / num2
            )

    return render_template("somepage.html", title="SomePage")