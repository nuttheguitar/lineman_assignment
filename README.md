# Project Title

Briefly introduce your project here, explaining its purpose and main functionalities.

## Folder Structure

- `app`: Contains a server-side Flask script hosting an inference model.
- `dataset`: Holds restaurant and user data necessary for model mapping and client result provision.
- `perf_test`: Includes performance testing scripts using K6 and stores results in `.csv` files.
- `app_gRPC`: Consists of a server-side gRPC script with an inference model.

## Prerequisites

- **Python**: Ensure Python is installed (recommended version 3.9.x).
- **Dependencies**: Install necessary dependencies by creating a virtual environment and installing packages listed in `requirements.txt` which place in `app` folder.
- **Docker**: Install Docker to manage containers for running the application

## Usage

- To run the application and see the results:

1. Ensure you have Docker installed on your system. If not, refer to the [Docker installation instructions](https://docs.docker.com/get-docker/).
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command to build and start the application:
    ```bash
    docker-compose up --build
    ```
   This command initiating the build process for the application containers. It might take some time to complete depending on the project's complexity and the network speed.
5. Once the containers are built and the application is running, you should be able to access the application at a specified URL or endpoint (https:localhost:5005/recommend/<user_id>).
6. The performance testing result will automatically save with in `perf_test` folder in `perf_result.csv` file

