from flask import Flask, render_template
from random import choice

app = Flask(__name__)

@app.route("/")
def home():
  s = sentence()
  return render_template('home.html', sentence=s)

def sentence():
  preposition = ["in","on","outside","beside","upside","around","beneath","above","placed gingerly inside"]
  determiner = ["his","her","our","my","your","their","its","everyone's"]
  location = ["court","roof","robot factory","astonished mouth","secret compartment","house","general direction","wildest dreams","butt"]

  sentence = "The ball is " + choice(preposition) + " " + choice(determiner) + " " + choice(location)

  return sentence

if __name__ == "__main__":
  app.run()
