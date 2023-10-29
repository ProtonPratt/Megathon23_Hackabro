from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Rest of your code...


# Define the route for the form
@app.route('/submit', methods=['POST'])
def submit_form():
    # Ensure that the request contains JSON data
    if not request.is_json:
        return jsonify({'error': 'Invalid request. Expected JSON data.'}), 400

    # Get JSON data from the request
    data = request.get_json()

    # Access form data
    twitter_handle = data.get('twitter')
    linkedin_handle = data.get('linkedin')
    imdb_indicator = data.get('imdb')

    # Print or process the form data
    print(f'Twitter Handle: {twitter_handle}')
    print(f'LinkedIn Handle: {linkedin_handle}')
    print(f'IMDb Indicator: {imdb_indicator}')

    # You can do further processing or database storage here

    return jsonify({'message': 'Form submitted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
