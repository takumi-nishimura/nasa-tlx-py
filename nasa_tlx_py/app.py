import csv
import datetime

from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    date = datetime.datetime.now()
    q1 = request.form["q1"]
    q2 = request.form["q2"]
    q3 = request.form["q3"]
    q4 = request.form["q4"]
    q5 = request.form["q5"]
    q6 = request.form["q6"]
    q_list = [q1, q2, q3, q4, q5, q6]
    q_list = [int(i) for i in q_list]
    q_list.sort()
    awwl = (
        q_list[0] * 1
        + q_list[1] * 2
        + q_list[2] * 3
        + q_list[3] * 4
        + q_list[4] * 5
        + q_list[5] * 6
    ) / 21

    with open("nasa_tlx_result.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, name, awwl, q1, q2, q3, q4, q5, q6])

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3333)
