from flask import Flask, render_template
import json, urllib2

object = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=3acJTFZozU7cOC5kbBhfcjrBaH6ipPVCwLMBpmLh")
string = object.read()
d = json.loads(string)

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template("NASA.html", picture = d["hdurl"], description = d["explanation"])

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()