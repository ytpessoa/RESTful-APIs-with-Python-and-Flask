
####### Aplicação: pesquisar hoteis, estrelas, diarias ########

from flask import Flask
from flask_restful import  Api

#from pacote.arquivo import Classe
from resources.hotel import Hoteis, Hotel





app = Flask(__name__)
api = Api(app)

########## Endpoints ##############
#api.add_resource(Classe, '/endpoint')
api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')


if __name__ == '__main__':
    app.run(debug=True)
    

# ambvirt\Scripts\activate
# python app.py
# http://127.0.0.1:5000/hoteis
# Postman -> New Collectoion -> New Request -> http://127.0.0.1:5000/hoteis