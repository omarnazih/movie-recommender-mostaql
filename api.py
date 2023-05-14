from flask import Flask, jsonify
from api_recommender_systems import hybrid_recommendations
from api_recommender_systems import content_recommendations

from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/hybrid_recommendations/<userId>/<title>', methods=['GET'])
def get_hybrid_recommendations(userId, title):
    
    # Perform recommendation logic based on the userId and title
    # Replace this with your actual recommendation code
    recommendations = hybrid_recommendations(userId, title)

    # Return the recommendations as a JSON response
    return jsonify({'data': recommendations, 'status': 200})



@app.route('/content_recommendations/<title>', methods=['GET'])
def get_content_recommendations(title):
    # Perform recommendation logic based on the title
    # Replace this with your actual recommendation code
    recommendations = content_recommendations(title)

    # Return the recommendations as a JSON response
    return jsonify({'data': recommendations, 'status': 200})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)