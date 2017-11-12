from flask import Flask, render_template
import json, urllib2

object = urllib2.urlopen("https://newsapi.org/v1/articles?source=al-jazeera-english&sortBy=top&apiKey=fbe8a0ea85934b5a8513dc6908fb92ad")
string = object.read()
d = json.loads(string)
articleDict = d["articles"]

my_app = Flask(__name__)

@my_app.route('/')
def root():
    print articleDict
    return render_template("AlJazeera.html", articles = articleDict)

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()