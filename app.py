from flask import Flask
from config import Config, db
from flask_wtf.csrf import CSRFProtect

# Import blueprints
from routes.admin_routes import admin_bp
from routes.collection_routes import collection_bp
from routes.sorting_routes import sorting_bp
from routes.refurbishment_routes import refurbishment_bp
# from routes.lifecycle_routes import lifecycle_bp
from routes.device_routes import device_bp

app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)

# Initialize DB with the app
db.init_app(app)

# Register blueprints
app.register_blueprint(collection_bp)
app.register_blueprint(sorting_bp)
app.register_blueprint(refurbishment_bp)
# app.register_blueprint(lifecycle_bp)
app.register_blueprint(device_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)