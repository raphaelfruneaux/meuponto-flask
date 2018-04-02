from flask import Flask

from .database import db

from apps.healthcheck import api as api_healthcheck


app = Flask(__name__)
app.config.from_pyfile("settings.py")

db.init_app(app)

app.register_blueprint(api_healthcheck.app)


@app.errorhandler(404)
def page_not_found(error):
    return "not found!", 404
    

@app.after_request
def after_request(response):
    try:
        db.session.remove()
        db.session.refresh()
        db.close()
    except Exception as e:
        print(e)
    return response


@app.teardown_appcontext
def teardown_db(exception):
    try:
        db.session.remove()
        db.session.refresh()
        db.close()
    except Exception as e:
        print(e)


@app.teardown_request
def teardown_request(exception):
    try:
        if exception:
            db.session.rollback()
        db.session.remove()
    except Exception as e:
        print(e)