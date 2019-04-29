from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    # return redirect(url_for('about'))
    return render_template('index.html')



@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


