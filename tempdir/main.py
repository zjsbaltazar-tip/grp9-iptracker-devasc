from flask import Flask, render_template, request
from api import *

app = Flask(__name__, static_url_path="/static")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ip_address = request.form.get("ip_address")
        specificIP = SpecificIP()
        response = specificIP.completeLocation(ip_address)
        if response[1] != 200:
            response = getIPInfo(ip_address)
        return render_template("result.html", data=response[0], map_loc=response[1])
    return render_template("main.html")

@app.route("/about")
def about():
    member = [
        "Aras, Juanito",
        "Baltazar, Zeus James",
        "Crebello, Cynna Mae",
        "Moreno, Wenzel"
    ]
    return render_template("about.html", member=member)

if __name__=="__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=5050)
    