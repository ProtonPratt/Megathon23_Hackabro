from flask import Flask, request, jsonify, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    # Get the data from the POST request
    data = request.get_json()

    # Process the data (you can add your custom logic here)
    twitter_handle = data.get('twitter')
    linkedin_handle = data.get('linkedin')
    imdb_indicator = data.get('imdb')

    # You can now do something with the data, for example, store it in a database

    # Return a response (e.g., a JSON response)
    response = {'message': 'Data received successfully'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
