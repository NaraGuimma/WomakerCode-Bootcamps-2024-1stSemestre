from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/characters')
def characters():
    response = requests.get("https://rickandmortyapi.com/api/character")
    characters_data = response.json()["results"]
    return render_template('characters.html', characters=characters_data)

@app.route('/locations')
def locations():
    response = requests.get("https://rickandmortyapi.com/api/location")
    locations_data = response.json()["results"]
    return render_template('locations.html', locations=locations_data)

@app.route('/location/<int:location_id>')
def location_profile(location_id):
    response = requests.get(f"https://rickandmortyapi.com/api/location/{location_id}")
    location_data = response.json()
    return render_template('location_profile.html', location=location_data)

@app.route('/episodes')
def episodes():
    response = requests.get("https://rickandmortyapi.com/api/episode")
    episodes_data = response.json()["results"]
    return render_template('episodes.html', episodes=episodes_data)

@app.route('/episode/<int:episode_id>')
def episode_profile(episode_id):
    response = requests.get(f"https://rickandmortyapi.com/api/episode/{episode_id}")
    episode_data = response.json()
    return render_template('episode_profile.html', episode=episode_data)



if __name__ == '__main__':
    app.run(debug=True)
