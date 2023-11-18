from flask import Flask, jsonify, request
import pickle
import pandas as pd
from sklearn.neighbors import NearestNeighbors

app = Flask("__name__")

# Load model, user data, and restaurant data
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

user_df = pd.read_parquet("user.parquet")
restaurant_df = pd.read_parquet("restaurant.mapping.parquet").set_index("index")

def recommend_restaurants(user_id):
    # Find 20 nearest neighbors to recommend restaurants
    user_data = user_df[user_df["user_id"] == user_id].drop(columns="user_id")

    if user_data.empty:
        return {"error": "User not found"}, 404

    dist, ind = model.kneighbors(user_data, n_neighbors=20)
    recommended_restaurant_ids = restaurant_df.iloc[ind[0]]["restaurant_id"].tolist()
    return {"restaurant": recommended_restaurant_ids}, 200

@app.route('/recommend/<user_id>', methods=['GET'])

def recommend(user_id):
    if request.method == 'GET':
        result, status_code = recommend_restaurants(user_id)
        return jsonify(result), status_code

@app.route('/ready', methods=['GET'])
def ready():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)