from flask import Flask,render_template
app=Flask(__name__)


@app.route("/register")
def register():
    return render_template("reg.html")

@app.route("/login")
def log_in():
    return render_template("sign.html")

if __name__=='__main__':
    app.run(debug=True)