from app import app
from flask import redirect, session, url_for


@app.route('/logout', methods=['get', 'post'])
def logout():
    session['admin'] = None
    session['worker'] = None
    session['responsible'] = None
    return redirect(url_for('index'))