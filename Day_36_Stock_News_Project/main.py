import requests
from datetime import date
from datetime import timedelta
from pandas.tseries.offsets import BDay
import os

STOCK_NAME = "AMZN"
COMPANY_NAME = "Amazon"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
api_key = os.environ.get("ALPHAADVANTAGE_API_KEY")
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key,
    "outputsize": "compact"
}

#Get the daily stock info for the stock
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()
#print(json.dumps(stock_data, indent=4))

#Get yesterday's date but use Pandas.BDay since yesterday might be a weekend.

yesterday = date.today() - BDay(1)
yesterday_string = yesterday.strftime("%Y-%m-%d")


#print(json.dumps(stock_data["Time Series (Daily)"][yesterday_string], indent=4))
yesterday_close_price = float(stock_data["Time Series (Daily)"][yesterday_string]["4. close"])


#2. - Get the day before yesterday's closing stock price
day_before_yesterday = yesterday - BDay(1)
day_before_yesterday_string = day_before_yesterday.strftime("%Y-%m-%d")
#print(type(day_before_yesterday_string))

day_before_yesterday_close_price = float(stock_data["Time Series (Daily)"][day_before_yesterday_string]["4. close"])


#3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = yesterday_close_price - day_before_yesterday_close_price
#print(positive_difference)


#4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_difference = (difference / yesterday_close_price) * 100
#print(percent_difference)
#5. - If TODO4 percentage is greater than 5 then print("Get News").

if abs(percent_difference) > 1.0:
    #print("Get News")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    news_api_key = os.environ.get("NEWSORG_API_KEY")
    news_params = {
        "apikey": news_api_key,
        "q": COMPANY_NAME,
        "from": day_before_yesterday_string
    }

    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    news_articles = response.json()["articles"][0:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

    #8. - Create a new list of the first 3 article's headline and description using list comprehension.
    articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in news_articles]
    #print(articles)

    #9. - Send each article as a separate message via Twilio. 

    for article in articles:
        if difference < 0:
            print(f"{STOCK_NAME}: 🔻{percent_difference:.2f}%\n{article}\n")
        else:
            print(f"{STOCK_NAME}: 🔺{percent_difference:.2f}%\n{article}\n")



