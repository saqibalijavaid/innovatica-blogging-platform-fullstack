from dotenv import load_dotenv
load_dotenv()  # 👈 This loads values from .env into os.environ

from flask import Flask
from flask_cors import CORS
from config import Config
from routes.auth import auth_routes
from routes.user import user_routes
from routes.post import post_routes

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, supports_credentials=True, origins="http://localhost:5173")

# Register Blueprints
app.register_blueprint(auth_routes, url_prefix='/api')
app.register_blueprint(user_routes, url_prefix='/api/user')
app.register_blueprint(post_routes, url_prefix='/api/posts')

# ✅ Root route for testing
@app.route("/")
def home():
    return "✅ Hello! Innovatica Backend is working!"

if __name__ == '__main__':
    app.run(debug=True)
