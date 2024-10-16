# Financial Sentiment Analysis Chatbot

This project implements a chatbot that performs sentiment analysis on financial texts using a fine-tuned LLaMA model.

## Setup

1. Clone the repository:   ```
   git clone https://github.com/blakeamory/financial-sentiment-app.git
   cd financial-sentiment-app   ```

2. Create a virtual environment and activate it:   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`   ```

3. Install the required packages:   ```
   pip install -r requirements.txt   ```

## Running the Application Locally

1. Run the main.py script:   ```
   python main.py   ```

2. Open your web browser and navigate to the URL provided by Gradio (usually http://localhost:7860).

## Running the Application in Google Colab

1. Open the `Financial_Sentiment_Analysis.ipynb` notebook in Google Colab.
2. Run all cells in the notebook.
3. Click on the URL provided by Gradio to open the chat interface.

## Fine-tuning the Model

To fine-tune the LLaMA model on your financial sentiment data:

1. Ensure your data is in the `data/all_financial_sentiment_data.csv` file.
2. Run the fine-tuning script:   ```
   python fine_tune.py   ```

## Project Structure

- `backend/`: Django backend for the chatbot API
- `frontend/`: Gradio frontend for the chat interface
- `data/`: Directory containing the financial sentiment dataset
- `fine_tune.py`: Script for fine-tuning the LLaMA model
- `main.py`: Script for running the application locally
- `Financial_Sentiment_Analysis.ipynb`: Notebook for running the application in Google Colab
- `requirements.txt`: List of Python dependencies
- `README.md`: This file

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
