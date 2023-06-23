from flask import Flask, render_template,request,redirect
import os
import json
app = Flask(__name__)

@app.route("/")
def index():
    with open('./db/data.json') as f:
        data = json.load(f)
    baladias = []
    wilayas = []
    jobs = []
    for x in data:
        baladias.append(x["baladia"])
        wilayas.append(x["wilaya"])
        jobs.append(x["job"])
    f.close()
    return render_template("home.html",data=data,l=len(data),baladias = set(baladias),wilayas = set(wilayas), jobs=set(jobs))

@app.route("/new",methods=["GET","POST"])
def new():
    if request.method == "POST":
        with open('./db/data.json',"r") as f:
            data = json.load(f)
            d = {
            "name":request.form["name"] +" "+ request.form["familyName"],
            "job":request.form["jobType"],
            "baladia":request.form["town"],
            "wilaya":request.form["state"],
            "rate":0,
            "tel":request.form["phoneNumber"],
            "location":0}
            data.append(d)
            f.close()
        with open('./db/data.json',"w") as f:
            json.dump(data, f)
            f.close()
            return redirect("/")
    return render_template("create-account.html")


# Here's how you create a route
# @app.route("/routeName")
# def functionName():
#    return render_template("fileName.html")

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=4000)
