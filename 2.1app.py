from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# --- MongoDB Atlas Connection ---
# Replace the connection string below with your own MongoDB Atlas URI
MONGO_URI = "mongodb+srv://kankurtiabdulqadir_db_user:86gY0J8V1HYqbxVr@cluster0.y7d4ays.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client["flask_demo_db"]  # database name
collection = db["users"]       # collection name


@app.route('/')
def form():
    """Render the form page."""
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit_data():
    """Insert form data into MongoDB Atlas."""
    try:
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            flash("Please fill out all fields.", "error")
            return render_template('form.html')

        # Insert into MongoDB
        result = collection.insert_one({"name": name, "email": email})
        if result.inserted_id:
            return redirect(url_for('success'))
        else:
            flash("Error: Could not insert data.", "error")
            return render_template('form.html')

    except Exception as e:
        flash(f"Database error: {str(e)}", "error")
        return render_template('form.html')


@app.route('/success')
def success():
    """Render success page."""
    return render_template('success.html', message="Data submitted successfully!")


if __name__ == '__main__':
    app.run(debug=True)
