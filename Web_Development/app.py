from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')  # http://127.0.0.1:5000
def home():
    message = request.args.get('message', None)
    return render_template('home.html', message=message)

@app.route('/about')  # http://127.0.0.1:5000/about 
def about():
    return render_template('about.html')

@app.route('/service')  # http://127.0.0.1:5000/service
def service():
    return render_template('service.html')

@app.route('/query')  # http://127.0.0.1:5000/query
def query():
    return render_template('query.html')

@app.route('/user_query', methods=['GET', 'POST'])
def user_query():
    if request.method == "POST":
        conn = sqlite3.connect("userdata.db")
        name = request.form['name']
        age = int(request.form['age'])
        address = request.form['address']
        college = request.form['college']
        branch = request.form['branch']
        roll_no = int(request.form['roll_no'])
        query_sub = request.form['query_sub']

        user_data = (name, age, address, college, branch, roll_no, query_sub)
        insert_data_query = """
        INSERT INTO userecord (name, age, address, college, branch, roll_no, query_sub) VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cur = conn.cursor()
        cur.execute(insert_data_query, user_data)
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('home', message="Your data is saved successfully!"))

@app.route('/fetch_data')  # http://127.0.0.1:5000/fetch_data
def fetch_data():
    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM userecord")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('fetch_data.html', rows=rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
