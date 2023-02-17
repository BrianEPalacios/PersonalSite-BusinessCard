from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home_page():
    date = datetime.datetime.now()
    year = date.year
    return render_template("index.html", year=year)


@app.route('/portfolio')
def portfolio_page():
    date = datetime.datetime.now()
    year = date.year
    return render_template("portfolio.html", year=year)


if __name__ == "__main__":
    app.run(debug=True)