from flask import Flask, render_template
import queries_db as db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin-panel')
def admin_panel():
    return render_template('rest-AdminPanel.html')

@app.route('/listRestaurants')
def listRestaurants():
    baseDeDatos = db.Database()
    
    #RUN JUST ONCE TO TEST POPULATE DB, then comment out again to avoid duplicates
    #baseDeDatos.test_populate_Restaurants()
    
    restaurants = baseDeDatos.list_Restaurants()

    print(restaurants)
    
    return render_template('restaurants.html', restaurants=restaurants)