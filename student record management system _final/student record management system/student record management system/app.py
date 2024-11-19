from flask import Flask, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'sri'

# MySQL Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Vishak46?'  # Your MySQL password here
app.config['MYSQL_DB'] = 'db3'  # Your database name here
mysql = MySQL(app)

# Route to render the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to display available students
@app.route('/students')
def students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")  # Query to fetch student data
    student_info = cur.fetchall()
    cur.close()
    return render_template('homepage.html', students=student_info)  # Render student info

# Route to search students by ID
@app.route('/search', methods=['POST', 'GET'])
def search():
    search_results = []
    search_term = ''
    if request.method == "POST":
        search_term = request.form['student_id']
        cur = mysql.connection.cursor()
        query = "SELECT * FROM students WHERE student_id LIKE %s"
        cur.execute(query, ('%' + search_term + '%',))
        search_results = cur.fetchmany(size=1)
        cur.close()
        return render_template('homepage.html', students=search_results)

# Route to insert a new student
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        student_id = request.form['student_id']
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (student_id, name, age, grade) VALUES (%s, %s, %s, %s)", (student_id, name, age, grade))
        mysql.connection.commit()
        return redirect(url_for('students'))

# Route to delete a student
@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE student_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('students'))

# Route to edit student details (Display the Edit Form)
@app.route('/edit/<string:id_data>', methods=['GET'])
def edit(id_data):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students WHERE student_id=%s", (id_data,))
    student = cur.fetchone()  # Fetch the student details to edit
    cur.close()
    return render_template('edit_student.html', student=student)

# Route to handle the update of student details
@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE students SET name=%s, age=%s, grade=%s WHERE student_id=%s", (name, age, grade, student_id))
        mysql.connection.commit()
        return redirect(url_for('students'))  # Redirect back to the student list page

if __name__ == "__main__":
    app.run(debug=True)
