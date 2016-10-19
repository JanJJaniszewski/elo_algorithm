# all the imports
from CatProject.create_functions import *

app = create_app(__name__)
db, Users, Items, Events = create_table_repr(app)
