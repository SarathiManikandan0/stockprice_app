# Stock Price Web App

This is a simple web application built with Streamlit that displays real-time stock prices.

## Installation

1. Ensure that you have Python 3 and pip installed on your system.
   - For Ubuntu or Debian-based systems, run the following commands:
     ```
     $ sudo apt update
     $ sudo apt upgrade -y
     $ sudo apt install python3-pip -y
     ```

2. Install the required dependencies by running the following command:
$ pip install streamlit yfinance

## Usage

1. Clone this repository to your local machine:
$ git clone <repository-url>

2. Navigate to the project directory:
$ cd stock-price-web-app


3. Open the `app.py` file and make any desired modifications:
$ vi app.py


4. Run the Streamlit app:
$ streamlit run app.py --server.port 80


5. Access the web app by opening your browser and visiting the following URL:
http://localhost:80


6. To stop the Streamlit app, press `Ctrl+C` in the terminal.

7. Optionally, if you want to use `pipenv` for managing dependencies, you can run the following command before step 2:
$ pipenv install yfinance


Feel free to customize and enhance the web app according to your specific requirements.
Remember to replace <repository-url> with the actual URL of your GitHub repository.
