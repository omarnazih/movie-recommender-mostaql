from flask import Flask, jsonify, request
from api_recommender_systems import (hybrid_recommendations, content_recommendations, post_user_ratings, get_user_ratings)


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


@app.route('/post_user_ratings', methods=['GET'])
def get_post_user_ratings():
    userId = request.args.get('userId')
    userName = request.args.get('userName')
    movieId = request.args.get('movieId')
    movieName = request.args.get('movieName')
    rating = request.args.get('rating')
    review = request.args.get('review')

    # 1000 ,"karim" , 282035 , "test1" , 4.5 , "good"
    # print(int(userId), str(userName), int(movieId), str(movieName),float(rating), str(review))
    
    res = post_user_ratings(userId, userName, movieId, movieName, rating, review)
    if not res:
        return jsonify({'data': [], 'status': 404})
    return jsonify({'data': res, 'status': 200})


@app.route('/get_users_ratings', methods=['GET'])
def get_get_users_ratings():
    # Perform the necessary operations with the provided parameters
    # ...

    res = get_user_ratings
    return jsonify({'data': res, 'status': 200})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)