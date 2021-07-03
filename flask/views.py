from flask import Flask,render_template,url_for
from models import *
from commandForm import *
from config import *




###PROGRAMME FLASK###

app = Flask(__name__)
app.config.from_object(Config)

###PAGE D'ACCUEIL, LISTANT LES ARTISTES, LES ALBUMS, ET LES GENRES###

@app.route('/')
@app.route('/home')
def home():
    artists = Artists.select()
    albums = Albums.select()
    genres = Genres.select()
    return render_template('index.html', artists=artists, albums=albums, genres=genres)

#####################################################################

###PAGE INFORMATIONS D'UN ARTISTE###

@app.route('/home/artist<artistId>')
def artiste(artistId):
    unArtist = Artists.select().where(Artists.artist_id == artistId)
    albumsArtist = Albums.select().join(Artists).where(Artists.artist_id == artistId)
    return render_template('artiste.html', unArtist=unArtist, albumsArtist=albumsArtist)

####################################

###PAGE INFORMATIONS D'UN ALBUM###

@app.route('/home/album<albumId>')
def album(albumId):
    unAlbum = Albums.select().where(Albums.album_id == albumId)
    chansonsAlbum = Tracks.select().join(Albums).where(Albums.album_id == albumId)
    return render_template('album.html', unAlbum=unAlbum, chansonsAlbum=chansonsAlbum)

##################################

###PAGE INFORMATIONS D'UN GENRE###

@app.route('/home/genre<genreId>')
def genre(genreId):
    unGenre = Genres.select().where(Genres.genre_id == genreId)
    chansonsGenre = Tracks.select().join(Genres).where(Genres.genre_id == genreId)
    return render_template('genre.html', unGenre=unGenre, chansonsGenre=chansonsGenre)

##################################

###PAGE LISTE DES CLIENTS###

@app.route('/clients')
def clients():
    clients = Customers.select()
    return render_template('clients.html', clients=clients)

############################

###PAGE INFORMATIONS D'UN CLIENT###

@app.route('/clients/client<clientId>')
def client(clientId):
    leClient = Customers.select().where(Customers.customer_id == clientId)
    lesCmdClient = Invoices.select().join(Customers).where(Customers.customer_id == clientId)
    return render_template('infoClient.html', leClient=leClient, lesCmdClient=lesCmdClient)

###################################

###PAGE INFORMATIONS D'UNE COMMANDE###

@app.route('/clients/client<clientId>/commande<commandId>')
def commande(clientId, commandId):
    uneCommande = Invoices.select().where(Invoices.invoice_id == commandId)
    itemsCommand = InvoiceItems.select().join(Invoices).where(Invoices.invoice_id == commandId)
    
    prixTot = 0
    for itemCommand in itemsCommand:
       prix = itemCommand.unit_price
       prixTot = prixTot + prix
    
    nomChansons = Tracks.select().join(InvoiceItems).where(InvoiceItems.invoice == commandId)
    
    return render_template('commande.html', uneCommande=uneCommande, itemsCommand=itemsCommand, nomChansons=nomChansons, prixTot=prixTot)

#######################################


###PAGE LISTE DES EMPLOYES###

@app.route('/employes')
def employes():
    employes = Employees.select()
    return render_template('employe.html', employes=employes)

############################

###PAGE INFORMATIONS SUR UN EMPLOYE###

@app.route('/employes/<employeId>')
def employe(employeId):
    unEmploye = Employees.select().where(Employees.employee_id == employeId)
    nomClients = Customers.select().join(Employees).where(Employees.employee_id == employeId)
    Emp = Employees.alias()
    manager = Employees.select(Employees.first_name, Employees.last_name, Emp.first_name, Emp.last_name).join(Emp, JOIN.LEFT_OUTER, on=(Employees.reports_to == Emp.employee_id)).where(Employees.employee_id == employeId)
    return render_template('infoEmploye.html', nomClients=nomClients, unEmploye=unEmploye, manager=manager)

#####################################

    
    

@app.route('/addcommand', methods=['GET', 'POST'])
def addcommand():
    form = CommandForm()
    return render_template('AjoutCommande.html', form=form)

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
