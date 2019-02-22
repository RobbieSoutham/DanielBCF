from flask import render_template
from app import app

#If errors occur, send to error page
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404
