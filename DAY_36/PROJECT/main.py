import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ''
NEWS_API_KEY = ''

account_sid = ''
auth_token = '' 


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}

response=requests.get(STOCK_ENDPOINT,params=stock_params)
data = response.json()["Time Series (Daily)"]
# print(data)

data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
# print(data_list)
yesterday_closing_price = yesterday_data['4. close']
# print(yesterday_closing_price)

#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
# print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

if difference > 0:
    up_down = '📈'
else:
    up_down = '📉'
    
# print(difference)

diff_percent = round((difference/float(yesterday_closing_price)) * 100)

if abs(diff_percent) > 1:
    # print("Get News.")
    news_params = {
        'apiKey':NEWS_API_KEY,
        'qInTitle':COMPANY_NAME,
    }
    news_response=requests.get(NEWS_ENDPOINT,params=news_params)
    articles=news_response.json()["articles"]
    # print(articles)
    three_articels = articles[:3]
    # print(three_articels)
    
    formatted_articels_list=[f'H{STOCK_NAME}:{up_down}:{diff_percent} Headline: {article['title']},\nBrief: {article['description']}' for article in three_articels]
    
    client = Client(account_sid, auth_token)
    
    for article in formatted_articels_list:    
        message = client.messages.create(
            body=article,
            from_='+',
            to='+' 
    )

    

#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

