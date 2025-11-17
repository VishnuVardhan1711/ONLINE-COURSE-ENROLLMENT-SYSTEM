from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy course list (simulate a small database)
COURSES = [
    {"id": 1, "name": "Python for Beginners"},
    {"id": 2, "name": "Web Development with Flask"},
    {"id": 3, "name": "Data Science Basics"}
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/courses')
def courses():
    return render_template("courses.html", courses=COURSES)

@app.route('/enroll', methods=['POST'])
def enroll():
    student_name = request.form['name']
    course_id = request.form['course']
    course_name = next(c['name'] for c in COURSES if str(c['id']) == course_id)

    return render_template("success.html",
                           student=student_name,
                           course=course_name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
