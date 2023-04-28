from flask import Flask
from flask import render_template
from flask import jsonify 


JOBS=[
  {
    'id':1,
    'title':"Data Analysit",
    'location':'NY, USA',
    'salary':'150,000 $'
  },
  {
    'id':2,
    'title':"Data Scientist",
    'location':'Maryland, USA',
    'salary':'250,000 $'
  },
  {
    'id':3,
    'title':"Frontend Developer",
    'location':'Sanfransisco, USA',
    'salary':'170,000 $'
  },
    {
    'id':4,
    'title':"Backend Developer",
    'location':' Washington, USA',
    'salary':'270,000 $'
  },
]


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html',JOBS=JOBS)

@app.route("/api/jobs")
def jobs_list():
    return jsonify(JOBS)


if __name__=="__main__":
  app.run("0.0.0.0",debug=True)