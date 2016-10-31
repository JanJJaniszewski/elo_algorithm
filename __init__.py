# all the imports
from CatProject.create_functions import *
import configparser

config = configparser.ConfigParser()
config.read('C:/Users/pole1/Documents/PyPros/CatProject/config.ini')

app = create_app(__name__, config)
db, Users, Events = create_table_repr(app)

