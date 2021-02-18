from flask_restful import Resource, reqparse
from models.hotel import HotelModel

#lista de hoteis
hoteis_list = [
    
    #hotel 1
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas':4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
    },   
    #hotel 2
    {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'estrelas':4.4,
        'diaria': 380.90,
        'cidade': 'Santa Catarina'

    },
    #hotel 3
    {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'estrelas':3.9,
        'diaria': 320.20,
        'cidade': 'Santa Catarina'

    }

]



class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis_list} #será convertido pelo Flask para 'Json'


class Hotel(Resource):
    
    #todos os argumentos aceitaveis no JSON recebido:
    argumentos = reqparse.RequestParser()    
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    #Metodos Auxiliares:
    def find_hotel(hotel_id):
        for hotel in hoteis_list:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    #Metodos CRUD    
    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel: #if hotel is not None
            return hotel
        return {'message': 'Hote not found.'}, 404 #status code : not found
        
    
    def post(self, hotel_id):
        
        #Post: http://127.0.0.1:5000/hoteis/delta
        # {    
        # "nome": "Delta Hotel",
        # "estrelas": 4.9,
        # "diaria": 7720.34,
        # "cidade": "Rio de Janeiro"
        # }

        # Resgatando um novo Hotel enviado via Post no formatado JSON:
               
        #chave e valor de todos os arguementos passados:
        dados = Hotel.argumentos.parse_args() 
       
       #construindo novo hotel JSON
            # hotel_id passado via url (delta) 
        # novo_hotel = {'hotel_id': hotel_id, **dados }

        hotel_objeto = HotelModel(hotel_id, **dados )
        novo_hotel = hotel_objeto.objetoToJson() #convertendo para dicionario

        hoteis_list.append(novo_hotel)

        return novo_hotel, 200 # 200 sucesso
    
    def put(self, hotel_id):       
       
       #momento de captura dos dados
        dados = Hotel.argumentos.parse_args()
        
        #construindo novo hotel JSON
            # hotel_id passado via url (delta) 
        
        # opcao 1
        # novo_hotel ={
        #     'hotel_id': hotel_id,
        #     'nome': dados['nome'],
        #     'estrelas': dados['estrelas'],
        #     'diaria': dados['diaria'],
        #     'cidade': dados['cidade']
        # }

        # opcao 2
        #desempacota => **dados
        #novo_hotel = {'hotel_id': hotel_id, **dados }

        #opcao 3
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.objetoToJson()


        hotel = Hotel.find_hotel(hotel_id)
        #se hotel existe => atualiza
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200 #atualizado, 200 OK
        
        #se hotel não-existe => cria
        hoteis_list.append(novo_hotel)
        return novo_hotel, 201 #201 CREATED

    def delete(self, hotel_id):
        #Ex.: delete: http://127.0.0.1:5000/hoteis/bravo
        
        #hoteis_list = [retorno for hotel in hoteis_list condicao ]
        #nova lista sem o hotel passado em "hotel_id"
        global hoteis_list
        hoteis_list = [hotel for hotel in hoteis_list if hotel['hotel_id'] != hotel_id ]
        return {'message': 'Hotel deleted'}