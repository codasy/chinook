from flask import Flask,render_template,url_for
from models import *



###PROGRAMME FLASK###

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    artists = Artists.select()
    albums = Albums.select()
    genres = Genres.select()
    return render_template('index.html', artists=artists, albums=albums, genres=genres)

@app.route('/clients')
def clients():
    clients = Customers.select()
    return render_template('clients.html', clients=clients)

@app.route('/clients/<clientId>')
def client(clientId):
    leClient = Customers.select().where(Customers.customer_id == clientId)
    leClient.execute()
    return render_template('infoClient.html', leClient=leClient)
    

@app.route('/employes')
def employes():
    employes = Employees.select()
    return render_template('employe.html', employes=employes)

@app.route('/employes/<employeId>')
def employe(employeId):
    unEmploye = Employees.select().where(Employees.employee_id == employeId)
    unEmploye.execute()
    return render_template('infoEmploye.html', unEmploye=unEmploye)

@app.route('/addcommand')
def addcommand():
    return render_template('ajoutcommande.html')

@app.before_request
def before_request():
    database.connect()

@app.after_request
def after_request(response):
    database.close()
    return response




    
     
            

if __name__ == "__main__":
    app.run()

######################
