import requests
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


def fetch_characters() -> list:
    base_url = "https://rickandmortyapi.com/api/character/"
    all_characters = []
    page = 1
    
    while True:
        params = {
            'species': 'Human',
            'status': 'Alive',
            'page': page
        }
        
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print(f"Error fetching data from API: {response.status_code}")
            break
        
        data = response.json()
        if 'results' not in data:
            break
        
        for character in data['results']:
            if "Earth" in character['origin']['name']:
                all_characters.append({
                    'Name': character['name'],
                    'Origin': character['origin']['name'],
                    'Location': character['location']['name'],
                    'Image Link': character['image']
                })
        
        if not data['info']['next']:
            break
        page += 1
    
    df = pd.DataFrame(all_characters)
    output_dir = '/app/output'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'rick_and_morty_human_characters.csv')
    df.to_csv(output_file, index=False)
    print(f"Characters exported to {output_file}")
    
    return all_characters


@app.route('/healthcheck', methods=['GET'])
def healthcheck() -> dict:
    return jsonify({
        "status": "healthy",
        "message": "Rick and Morty Characters API is up and running"
    }), 200


@app.route('/characters', methods=['GET'])
def get_characters_endpoint() -> dict: 
    characters = fetch_characters()
    
    limit = request.args.get('limit', type=int)
    if limit:
        characters = characters[:limit]
    
    return jsonify({
        "total_characters": len(characters),
        "characters": characters
    }), 200


@app.route('/export', methods=['GET'])
def export_characters() -> dict:
    fetch_characters()
    return jsonify({
        "message": "Characters exported to CSV",
        "file_path": "/app/output/rick_and_morty_human_characters.csv",
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
