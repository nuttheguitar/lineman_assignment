import grpc
import concurrent.futures
import recommender_pb2 as rs
import recommender_pb2_grpc as rs_grpc
import pickle
import pandas as pd
from sklearn.neighbors import NearestNeighbors

class RecommendationServicer(rs_grpc.RecommenderServicer):
    def Recommend(self, request, context):
        # Implement your recommendation logic here using user_id from request
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)

        user_df = pd.read_parquet("../dataset/user.small.parquet")
        restaurant_df = pd.read_parquet("../dataset/restaurant.mapping.parquet").set_index("index")
        
        user_id = request.userId
        user_data = user_df[user_df["user_id"] == user_id].drop(columns="user_id")
        if user_data.empty:
            return {"error": "User not found"}, 404

        dist, ind = model.kneighbors(user_data, n_neighbors=20)
        recommended_restaurant_ids = restaurant_df.iloc[ind[0]]["restaurant_id"].tolist()

        return rs.RecommendResponse(restaurantIds=recommended_restaurant_ids)

def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    rs_grpc.add_RecommenderServicer_to_server(RecommendationServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()