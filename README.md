# stock-market-analysis

Analyses stock market historical data and sentiment to predict stock prices using deep neural network.

#### This project is still under construction

## Project report (Not Complete):
#### [Stock Market Analysis (at google docs)](https://docs.google.com/document/d/1gcgvTQXWzORDAhtZyQVfNQ9ScLQ6Zz_JJp8X3R20l0o/edit?usp=sharing)

## Learn sentiment analysis of stock data from Twitter

### Easy:

* **[Goel Mittal - Stock Market Prediction Using Twitter Sentiment Analysis](http://cs229.stanford.edu/proj2011/GoelMittal-StockMarketPredictionUsingTwitterSentimentAnalysis.pdf)**

### Medium:

* **[IIT Bhubaneswar - Sentiment Analysis of Twitter Data for
Predicting Stock Market Movements](https://arxiv.org/pdf/1610.09225.pdf)**

### Legendary:

* **[Johan Bollen - Twitter mood predicts the stock market](https://arxiv.org/pdf/1010.3003&)**

## Usage

### Below is the step by step guide:

* **[requirements.txt](https://github.com/Gunjan933/stock-market-analysis/blob/master/requirements.txt)** 
  
  - Helps to install dependencies assuming you have pip installed in your computer.
  
    ```console
    pip install -r requirements.txt
    ```

* **[stock_fetcher.py](https://github.com/Gunjan933/stock-market-analysis/blob/master/stock_fetcher.py)**

  - This helps to draw latest historical prices of stock data from Yahoo Finance Api. It takes 20 minutes or so, depending on your computing power and internet speed to update the latest stock market data.
    
    ```console
    python stock_fetcher.py
    ```

* **[stock_sentiment.py](https://github.com/Gunjan933/stock-market-analysis/blob/master/stock_sentiment.py)** (Not Implemented yet)
  
  - Helps to add sentiment of any date for every stock data, ranging from [-1, 0, 1] for Negetive, Neutral and Positive.
    
    ```console
    python stock_sentiment.py
    ```

* **[stock_merger.py](https://github.com/Gunjan933/stock-market-analysis/blob/master/stock_merger.py)**
  
  - Helps to merge every stock data into one and differentiates from X data and Y data. 
    you have to specify some parameters inside the code, as command lines argument aren't ready yet:
      * Specify **threshold_size** which will not include the stock data which are less than that size (It is mainly to remove the stocks that have no implications on stock data)
      * Specify the **ticker name** or **company name** which can be found in **[assets /](https://github.com/Gunjan933/stock-market-analysis/tree/master/assets)**.
  
    ```console
    python stock_merger.py
    ```
