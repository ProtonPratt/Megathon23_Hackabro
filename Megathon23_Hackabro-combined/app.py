from flask import Flask, request, jsonify, render_template, url_for
import tweepy

consumer_key = 'TEsiWEIdS5x9rdQGq51VXDCxt'
consumer_secret = 'ImcW9oWZmOmkiLwvnGk5utcXKK2Gojs6gVjA6Eu50b6EXtcvXC'
access_token = '1214570308369186816-L87aeqNHfTGVQtCzskvvd843OYVeD9'
access_token_secret = 'aeZ84XdjwIPios0BhkzTWH8bkQBgjZJOAHBk6eKZgZzIV'

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

api = tweepy.API(auth, wait_on_rate_limit=True)

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

    # Screen name of the Twitter user you want to scrape
    screen_name = twitter_handle

    # Get user profile information
    user = api.get_user(screen_name=screen_name)    
    print("User Profile Information:")
    print("Name:", user.name)
    print("Username:", user.screen_name)
    print("Description:", user.description)
    print("Followers Count:", user.followers_count)
    print("Friends Count:", user.friends_count)
    print("Tweets Count:", user.statuses_count) 



    # Return a response (e.g., a JSON response)
    response = {'message': 'Data received successfully'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
