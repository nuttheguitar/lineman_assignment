from concurrent import futures
import time
import threading
import random
from grpc_testing import _interceptor

import grpc
import recommender_pb2 as rs
import recommender_pb2_grpc as rs_grpc

def run():
    # Establish a gRPC channel to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = rs_grpc.RecommenderStub(channel)

        request = rs.RecommendRequest(userId='u00001')
        response = stub.Recommend(request)

        # Process the response
        recommended_restaurant_ids = response.restaurantIds
        print("Recommended Restaurant IDs:", recommended_restaurant_ids)


def load_test():
    target_rate = 5  # 5 requests per second
    time_interval = 1.0 / target_rate

    # Track response times for percentile calculation
    response_times = []
    num_requests = 100 

    for _ in range(num_requests):
        start_time = time.time()

        # Execute the gRPC request
        run()

        end_time = time.time()
        response_time = (end_time - start_time) * 1000  # Response time in milliseconds
        response_times.append(response_time)

        # Sleep for the time interval to match the target rate
        time.sleep(max(0, time_interval - (end_time - start_time)))

    # Calculate the 90th percentile response time
    response_times.sort()
    percentile_90 = response_times[int(num_requests * 0.9)]
    print(f"90th percentile response time: {percentile_90} ms")

if __name__ == '__main__':
    load_test_thread = threading.Thread(target=load_test)
    load_test_thread.start()
    load_test_thread.join()