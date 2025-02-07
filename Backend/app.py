from flask import Flask, render_template  # Import Flask and render_template
from blueprints import register_blueprints  # Import the blueprint registration function

# Create the Flask app instance
app = Flask(__name__)

# Register Blueprints via the central function
register_blueprints(app)

@app.route('/')
def home():
    return render_template('home.html')  # Render the index.html template

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
