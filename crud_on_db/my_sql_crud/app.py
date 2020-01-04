#importing necessarry libraries
#importing flask , jsonify,request
from flask import Flask,  jsonify, request
#importing mysql database library
import MySQLdb
#seeting name to run this file as flask app
app = Flask(__name__)

#confugring my database here
db = MySQLdb.connect("localhost", "root", "", "BookManager")

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
    add_data = list(request.json)
    try:
        query="insert into bookstore(book_name,author,gener,pub_year,price) values('{}','{}','{}','{}',{});".format(add_data[1],add_data[2],add_data[3],add_data[4],add_data[5])
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
    return get_bookstore_table()



# method sends a post type of request ,
# executes the deletion query and returns the whole table without the deleted values
@app.route('/delete', methods=['POST'])
def delete_book():
    # initializing database cursor
    curs = db.cursor()
    # fetching the data we have to delete from request body
    delete_data = list(request.json)
    try:
        query="delete from bookstore where book_name = '{}';".format(delete_data[1])
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
    return get_bookstore_table()



# method sends a post type of request ,
# executes the updation query and returns the whole table with updated values
@app.route('/update', methods=['POST'])
def update_book():
    # initializing database cursor
    curs = db.cursor()
    # fetching the data we have to update from request body
    update_data = list(request.json)
    try:
        #updating the name value
        name_query="UPDATE bookstore SET book_name = `{}' WHERE s_no = {};".format(update_data[1],update_data[0])
        #updating the author column value
        author_query ="UPDATE bookstore SET book_name = `{}' WHERE s_no = {};".format(update_data[2],update_data[0])
        #updating the gener column value
        gener_query="UPDATE bookstore SET book_name = `{}' WHERE s_no = {};".format(update_data[3],update_data[0])
        #updating the publication date column value
        pub_query="UPDATE bookstore SET book_name = `{}' WHERE s_no = {};".format(update_data[4],update_data[0])
        #updating the price column value
        price_query="UPDATE bookstore SET book_name = `{}' WHERE s_no = {};".format(update_data[5],update_data[0])
        # giving query to cursor to execute
        curs.execute(name_query)
        # giving query to cursor to execute
        curs.execute(author_query)
        # giving query to cursor to execute
        curs.execute(gener_query)
        # giving query to cursor to execute
        curs.execute(pub_query)
        # giving query to cursor to execute
        curs.execute(price_query)
        # giving query to cursor to execute
        curs.execute("select * from bookstore")
        # obtaining result after executing query
        myresult = curs.fetchall()
        # converting the result into json
        return jsonify(myresult)
    except:
        print("Error: unable to fetch items")
    return get_bookstore_table()


#base url directed towards getting whole table
@app.route('/')
def index():
    return get_bookstore_table()

if __name__ == '__main__':
    app.run(debug=True)

