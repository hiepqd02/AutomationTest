import subprocess
import time
from flask import Flask, render_template, request,  redirect, url_for, send_from_directory, send_file

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_tests", methods=["POST"])
def run_tests():
 
    test_process = subprocess.Popen(["/bin/bash", "/home/tdhpisme/automationScript.sh"])
    while test_process.poll() is None:
        time.sleep(1)
    return redirect(url_for("report"))
    # return "Tests complete. View the report <a href='/report'>here</a>."

@app.route("/report")
def report():
    return render_template("report.html")




if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')



