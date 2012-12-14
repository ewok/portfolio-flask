from flask import request, session, redirect, url_for
from markupsafe._speedups import escape


def login():
    """ Login
    """
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            import config

            if config.USERNAME == escape(request.form['username'])\
            and config.PASSWORD == escape(request.form['password']):
                session['username'] = escape(request.form['username'])

                return redirect(url_for('admin'))

    return '''
        <form action="" method="post">
            <p><label>Name</label><input type=text name=username>
            <p><label>Password</label><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''


def logout():
    """ Logout
    """
    # remove the username from the session if its there
    session.pop('username', None)
    return redirect(url_for('index'))

def login_if_not_valid_user():
    """ Validatin user
    """
    if not 'username' in session:
        return redirect(url_for('login'))
