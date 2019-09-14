# stock-market-analysis

Analyses stock market historical data and sentiment to predict stock prices using deep neural network

# Usage

* **[requirements.txt](https://github.com/Gunjan933/stock-market-analysis/blob/master/requirements.txt)** 
  
  - Helps to install dependencies assuming you have pip installed in your computer.
  
    ```console
    pip install -r requirements.txt
    ```

* **[stock_fetcher.py](https://github.com/Gunjan933/stock-market-analysis/blob/master/stock_fetcher.py)**

  - This helps to draw latest historical prices of stock data from Yahoo Finance Api. It takes 20 minutes or so, depending on your computing power and internet speed to update the latest stock market data
    
    ```console
    python stock_fetcher.py
    ```

* **[stock_sentiment.py](https://github.com/Gunjan933/stock-market-analysis/blob/master/stock_sentiment.py)** (Not Implemented yet)
  
  - Helps to add sentiment of any date for every stock data, ranging from [-1, 0, 1] for Negetive, Neutral and Positive
    
    ```console
    python stock_sentiment.py
    ```

* **[stock_merger.py](https://github.com/Gunjan933/stock-market-analysis/blob/master/stock_merger.py)** (Not Implemented yet)
  
  - Helps to merge every stock data into one and differentiates from X data and Y data.
    
    ```console
    python stock_merger.py
    ```