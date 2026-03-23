"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from sqlalchemy import select

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

#@app.route("/token", methods=["POST"])
#def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

@api.route('/people', methods=['GET'])
def get_all_characters():
    all_people = db.session.execute(select(Character)).scalars().all()
    list_of_dictionaries = []
    for person in all_people:
        list_of_dictionaries.apend(person.serialize())
    
    return jsonify(list_of_dictionaries), 200

@api.route('/people/<int:person_id>', methods=["GET"])
def get_single_person(person_id):
    person = db.session.get(Character, person_id) 
    if person is None:
        return jsonify({"msg": "Charcater does not exist"}), 404
    return jsonify(person.serialize()), 200 #with fetches and responses back end and front end
   

@api.route('/planets', methods=["GET"])
def get_all_planets(planet):
    all_planets = db.session.execute(select(Planet)).scalars().all()
    list_of_dictionaries = []
    for person in all_planets:
        list_of_dictionaries.apend(person.serialize())
    return jsonify(list_of_dictionaries), 200
   

@api.route('/planets/<int:planet_id>', methods=["GET"])
def get_single_planet(planet_id):
    planet = db.session.get(planet_id)
    if planet is None:
        return jsonify({"msg":" Planet deos not exist"}), 404
    return jsonify(planet_id.serialize()), 200
    

@api.route('/users', methods=['GET'])
def get_all_users(users):
    user = db.session.get(users)
    if user is None:
        return jsonify({"msg":" User deos not exist"}), 404
    return jsonify(users.serialize()), 200
    
@api.route('/users/<int:user_id>/favorites', methods=['GET'])
def get_user_favorites(user_id):
    found_user = db.session.get(User, user_id)
    if found_user is None:
        return jsonify({"msg":" User does not exist"}), 404
    serialized_user = found_user.serialized()
    return jsonify({
        "user_id": serialized_user.id,
        "favorite_characters": serialized_user.favorite_characters,
        "favorite_planets": serialized_user.favorite_planets,
    }),
    

@api.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    body = request.json
    found_user = db.session.get(User, body["user_id"])
    new_fave_planet = db.session.get(Planet, planet_id)
    if found_user is None or new_fave_planet is None:
        return jsonify ({"planet or user not found"}), 404
    found_user.favorite_planets.append(new_fave_planet)
    db.sesion.commit()
    serialized_user = found_user.serialized()
    return jsonify ({"favorite_planets": serialized_user.favorite_planets}), 200
    

@api.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    body = request.json
    found_user = db.session.get(User, body["user_id"])
    delete_fave_planet = db.session.get(Character, planet_id)
    if found_user is None or delete_fave_planet is None:
        return jsonify ({"person or user not found"}), 404
    found_user.favorite_planet.remove(delete_fave_planet)
    db.sesion.commit()
    serialized_user = found_user.serialized()
    return jsonify ({"favorite_planets": serialized_user.favorite_planets}), 200

    

@api.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_person(people_id):
    body = request.json
    found_user = db.session.get(User, body["user_id"])
    new_fave_person = db.session.get(Character, people_id)
    if found_user is None or new_fave_person is None:
        return jsonify ({"person or user not found"}), 404
    found_user.favorite_characters.append(new_fave_person)
    db.sesion.commit()
    serialized_user = found_user.serialized()
    return jsonify ({"favorite_characters": serialized_user.favorite_characters}), 200

@api.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_person(people_id):
    body = request.json
    found_user = db.session.get(User, body["user_id"])
    delete_fave_person = db.session.get(Character, people_id)
    if found_user is None or delete_fave_person is None:
        return jsonify ({"person or user not found"}), 404
    found_user.favorite_characters.remove(delete_fave_person)
    db.sesion.commit()
    serialized_user = found_user.serialized()
    return jsonify ({"favorite_characters": serialized_user.favorite_characters}), 200
    


#@api.route('/users/favorites', methods=["GET"])
#def get_all_favorites(favorites):
 #   favorite = db.session.get(favorites)
  #  if favorite is None:
   #     return jsonify({"msg": "Favorite does not exist"}), 404
    #return jsonify(favorite.serialize()),200
    



#@api.route('/favorite/people/<int:people_id>', methods=['POST'])
#def add_favorite_person(people_id):
    #pass



#@api.route('/favorite/people/<int:people_id>', methods=['DELETE'])
#def delete_favorite_person(people_id):
    #pass

