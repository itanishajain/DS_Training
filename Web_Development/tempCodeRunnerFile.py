@app.route('/fetch_data')   # http://127.0.0.1:5000/fetch_data
# def fetch_data():
#     conn = sqlite3.connect("userdata.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM userecord")
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return render_template('fetch_data.html', rows=rows)