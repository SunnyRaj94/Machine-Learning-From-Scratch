#importing necessarry libraries
#importing flask , jsonify,request

from flask import Flask,  jsonify, request
import pymongo
#seeting name to run this file as flask app
app = Flask(__name__)
#making a mongo db client to interact eith mongodb server
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#making an object of database with the help of mongodb client
my_database = myclient["BookManager"]
#making an object of bookstore collection to perform query operations
my_col = my_database["bookstore"]
#base url directed towards getting whole table
@app.route('/')
def index():
    return show_collections()

#method that takes get type of request
#returns the list of collections that are present in current database
@app.route('/db', methods=['GET'])
def show_collections():
    #obtaining the list of collection names present inside database
    my_result=my_database.list_collection_names()
    #returning json response
    return jsonify(my_result)


#method that takes get type of request
#returns the list of enteries that are present in current collection
@app.route('/entries', methods=['GET'])
def get_collection_items():
    #obtaining the list of collection names present inside database
    my_result=list(my_col.find())
    #looping just to remove object id
    for i in range(len(my_result)):
        #making object id 0
        my_result[i]['_id']=0
    #returning json response
    return jsonify(my_result)


#method that takes post type of request
#returns the list of enteries that are present in current collection after inserting one
@app.route('/create', methods=['POST'])
def create_collection_item():
    #taking json request
    creation_data = request.json
    #inserting json request into database
    my_col.insert_one(creation_data)
    #fetching data after created entry and returning updated collection
    return get_collection_items()


#method that takes post type of request
#returns the list of enteries that are present in current collection after deleting the requested entry
@app.route('/delete', methods=['POST'])
def delete_collection_item():
    #taking json request
    deletion_data = request.json
    #inserting json request into database
    my_col.delete_one(deletion_data)
    #fetching data after created entry and returning updated collection
    return get_collection_items()


#method that takes post type of request
#returns the list of enteries that are present in current collection after updating the requested entry
@app.route('/update', methods=['POST'])
def update_collection_item():
    #taking json request
    updation_data = request.json
    print("hiiiiii",updation_data)
    #inserting json request into database
    my_col.update_one(updation_data[0],updation_data[1])
    #fetching data after created entry and returning updated collection
    return get_collection_items()



if __name__ == '__main__':
    app.run(debug=True)