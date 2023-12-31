from mongoengine import connect
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'password')
db_name = config.get('DB', 'db_name')

connect(host=f'mongodb+srv://{mongo_user}:{mongodb_pass}@cluster0.xbtnffb.mongodb.net/{db_name}')


# import configparser

# config = configparser.ConfigParser()
# config.read('config.ini')

# mongo_url = config.get('DB', 'url')



# from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://HWmongoDB:0FyBlogUxQMx6NC8@cluster0.kxyddip.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


# from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://Hw08mongo:qwerty1234@cluster0.pnnu3x7.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

# # Create a new client and connect to the server
# client = MongoClient(uri, ssl=False)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


# from mongoengine import *
# uri = "mongodb+srv://Hw08mongo:qwerty1234@cluster0.s9aqskd.mongodb.net/?retryWrites=true&w=majority"
# # Create a new client and connect to the server
# bd = connect(host=uri, ssl=False, db="hw8")
# # Send a ping to confirm a successful connection
# try:
#     bd.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

