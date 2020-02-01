#importing necessarry libraries
#importing flask , jsonify,request
from flask import Flask,  jsonify, request
#importing mysql database library
# import MySQLdb
import mysql.connector
#seeting name to run this file as flask app
app = Flask(__name__)

#confugring my database here
# db = MySQLdb.connect("localhost", "root", "", "BookManager")

db = mysql.connector.connect(host='localhost',user="root",passwd="PWD",database="Bookmanager")
#method sends a get type request and obtains the list of tables present in current database
@app.route('/tables', methods=['GET'])
def get_tables():
    #initializing database cursor
    curs = db.cursor()
    try:
        #giving query to cursor to execute
        curs.execute("show tables")
        #obtaining result after executing query
        myresult = curs.fetchall()
        #converting the result into json
        return jsonify(myresult)
    except:
        print("Error: unable to fetch items")
    return get_bookstore_table()



# method sends a get type of request ,
# fetches and return the whole bookstore table in json format
@app.route('/bookstore', methods=['GET'])
def get_bookstore_table():
    # initializing database cursor
    curs = db.cursor()
    try:
        # giving query to cursor to execute
        curs.execute("select * from bookstore")
        # obtaining result after executing query
        myresult = curs.fetchall()
        print(type(myresult))
        # converting the result into json
        return jsonify(myresult)
    except:
        print("Error: unable to fetch items")
    return get_bookstore_table()



# method sends a post type of request ,
# executes the insertion query and returns the whole table with inserted values
@app.route('/add', methods=['POST'])
def add_new_book():
    # initializing database cursor
    curs = db.cursor()
    #fetching the data we have to add from request body
    add_data = request.json
    try:
        query="insert into bookstore(book_name,author,gener,pub_year,price) values('{}','{}','{}','{}',{});".format(add_data['book_name'],add_data['author'],add_data['gener'],add_data['pub_year'],add_data['price'])
        # giving query to cursor to execute
        curs.execute(query)
        # giving query to cursor to execute
        curs.execute("select * from bookstore")
        # obtaining result after executing query
        myresult = curs.fetchall()
        # converting the result into json
        return jsonify(myresult)
    except:
        print("Error: unable to fetch items")
    return "unable to add requested book into database"



# method sends a post type of request ,
# executes the deletion query and returns the whole table without the deleted values
@app.route('/delete', methods=['POST'])
def delete_book():
    # initializing database cursor
    curs = db.cursor()
    # fetching the data we have to delete from request body
    delete_data = request.json
    column_name =  delete_data.keys()
    try:
        query="delete from bookstore where {} = '{}';".format(column_name,delete_data[column_name])
        # giving query to cursor to execute
        curs.execute(query)
        # giving query to cursor to execute
        curs.execute("select * from bookstore")
        # obtaining result after executing query
        myresult = curs.fetchall()
        # converting the result into json
        return jsonify(myresult)
    except:
        print("Error: unable to fetch items")
    return "Unable to delete requested data from database"

#method sends a post type of request ,
# executes the updation query and returns the whole table with updated values
@app.route('/update', methods=['POST'])
def update_bookstore():
    # initializing database cursor
    curs = db.cursor()
    # fetching the data we have to update from request body
    update_data = request.json
    #extracting column names that are to be updated
    # we will take column name , value before updation , value after updation in json format request
    key = update_data['key']
    value_before = update_data['value before']
    updated_value = update_data['value to update']
    try:
        # updating the author column value
        author_query = "UPDATE bookstore SET {} = {} where {} = '{}';".format(key,updated_value,key,value_before)
        # giving query to cursor to execute
        curs.execute(author_query)
        # giving query to cursor to execute
        curs.execute("select * from bookstore")
        # obtaining result after executing query
        myresult = curs.fetchall()
        # converting the result into json
        return jsonify(myresult)
    except:
        print("Error: unable to fetch items")
    return "Value Updation Failed"


#base url directed towards getting whole table
@app.route('/')
def index():
    return get_bookstore_table()

if __name__ == '__main__':
    app.run(debug=True)

