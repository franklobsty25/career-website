from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Accra',
    'salary': 'GHS 10,000.00',
  },
  {
    'id': 2,
    'title': 'Data Science',
    'location': 'Kumasi',
    'salary': 'GHS 15,000.00',
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$ 20,000.00',
  }
]

@app.route("/")
def hello_colonkoded():
  return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run("0.0.0.0", debug = True)