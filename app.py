from flask import Flask, render_template
import sqlite3

con = sqlite3.connect("players_20.db", check_same_thread=False)
cur = con.cursor()
app = Flask(__name__)

@app.route('/')
def w209():
    file='about9.jpg'
    return render_template('w209.html',file=file)

@app.route('/api')
def api():
    return("x": 2)

@app.route("/players/count")
def getPlayersCount():
    res = cur.execute("SELECT COUNT(*) as ct FROM users")
    return ("count" : res.fetchone()[0])

if __name__ == '__main__':
    app.run()
