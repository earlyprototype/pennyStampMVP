from flask import Flask, request, jsonify
from src.utils.cache import get_cached_data, cache_data
from src.api.yfinance import fetch_stock_data
from src.llm.llama import generate_code
from backend.sandbox import execute_sandboxed_code  # Import the sandbox function
import pandas as pd
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from the Config class


app = Flask(__name__)

@app.route('/api/stock_data', methods=['GET'])
def stock_data():
    ticker = request.args.get('ticker')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Input validation
    if not ticker or not start_date or not end_date:
        return jsonify({'error': 'Missing required parameters'}), 400

    cached_data = get_cached_data(ticker, start_date, end_date)
    if cached_data:
        return jsonify(cached_data)

    try:
        data_dict = fetch_stock_data(ticker, start_date, end_date)
        if data_dict is None:
            return jsonify({'error': 'No data found for this ticker and date range'}), 404

        cache_data(ticker, start_date, end_date, data_dict)
        return jsonify(data_dict)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/generate_code', methods=['POST'])
def generate_code_api():
    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    generated_code = generate_code(prompt)
    return jsonify({'code': generated_code})

@app.route('/api/execute_code', methods=['POST'])
def execute_code_api():
    code = request.json.get('code')
    if not code:
        return jsonify({'error': 'Code is required'}), 400

    ticker = request.args.get('ticker')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    try:
        data_dict = fetch_stock_data(ticker, start_date, end_date)
        if data_dict is None:
            return jsonify({'error': 'No data found for this ticker and date range'}), 404
        df = pd.DataFrame.from_records(data_dict)  # Convert to DataFrame

        output, error = execute_sandboxed_code(code, df)

        return jsonify({'output': output, 'error': error})

    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)