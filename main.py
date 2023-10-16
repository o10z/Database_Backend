from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///countries.db'
db = SQLAlchemy(app)


#
class Country(db.Model):
    __tablename__ = "Country"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


# Initialize the database
with app.app_context():
    db.create_all()


# Adds country to the database
@app.route('/add_country', methods=['POST'])
def add_country():
    data = request.get_json()
    country_name = data.get('name')

    if country_name:
        new_country = Country(name=country_name)
        db.session.add(new_country)
        db.session.commit()
        return jsonify({'message': 'Country was added'}), 201
    else:
        return jsonify({'error': '...Something went wrong...'}), 400


# Gets all countries in the database
@app.route('/get_countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()
    country_list = [{'id': country.id, 'name': country.name} for country in countries]
    return jsonify(country_list)


if __name__ == '__main__':
    app.run(debug=True)
