from CatProject import *
from flask import request, session, redirect, url_for, render_template, flash
import pandas as pd

db = db
app = app
Users = Users
Events = Events


@app.route('/', methods=['GET'])
def red():
    return redirect(url_for('login'))


@app.cli.command('initdb')
def initdb():
    """Initializes the database."""
    db.create_all()
    print('Initialized the database.')


@app.cli.command('check_tables')
def see_tables():
    tables = ['Items', 'Users', 'Events']
    for tab in tables:
        q = 'select * from {}'.format(tab)
        df = pd.read_sql(q, db.session.bind)
        print(df.head())


@app.cli.command('update_items')
def add_items():
    """Adds all items that are found in the items folder to the database"""
    item_csv_path = '{}/item_table.csv'.format(config['Paths']['item_folder'])
    items = pd.read_csv(item_csv_path)
    items.to_sql('items', db.session.bind, if_exists='replace')
    print('Item table updated based upon Excel file {}'.format(item_csv_path))

# TODO MAIN: Further develop show items to really show items.
@app.route('/show_items')
def show_items():
    q = 'select * from Items'
    items = pd.read_sql(q, db.session.bind)
    return render_template('show_items.html', entries=items)


# TODO When registering, save Username and Password in User table
@app.route('/login', methods=['GET', 'POST'])
def login():
    # flash (request.form)
    error = None
    if request.method == 'POST':
        if request.form['submit'] == 'Login' and request.form['username'] == app.config['USERNAME'] and request.form['password'] == app.config['PASSWORD']:
            session['logged_in'] = True
            return redirect(url_for('show_items'))
        elif request.method == 'POST' and request.form['submit'] == 'Register':
            session['logged_in'] = True
            # Write session related stuff
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            # Register user
            u = Users(session['username'], session['password'])
            db.session.add(u)
            db.session.commit()
            flash('You are now logged in')
            return redirect(url_for('show_items'))
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return render_template('login.html', error=None)