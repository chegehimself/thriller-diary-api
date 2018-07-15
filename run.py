# run.py

# for running the server

# import app and entries blueprint
from app import app
from app.views import entries_bp, ent_bp

# register entry Blueprint
app.register_blueprint(ent_bp)
app.register_blueprint(entries_bp)

# start the app in debugging mode
if __name__ == '__main__':
    app.run(debug=True)
