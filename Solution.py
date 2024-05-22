# 1st step install and import modules
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from dateutil import parser

accounts = [
    "https://twitter.com/Mr_Derivatives",
    "https://twitter.com/warrior_0719",
    "https://twitter.com/ChartingProdigy",
    "https://twitter.com/allstarcharts",
    "https://twitter.com/yuriymatso",
    "https://twitter.com/TriggerTrades",
    "https://twitter.com/AdamMancini4",
    "https://twitter.com/CordovaTrades",
    "https://twitter.com/Barchart",
    "https://twitter.com/RoyLMattox",
]
# This part i commented because i entered 10 accounts manually to reduce the time
# accounts = []
# num_of_accounts = int(input("Number of accounts you wiil enter: "))
# for inputs in range(num_of_accounts):
#     account = input(f"Enter account {inputs+1} URL you want to search for: ")
#     accounts.append(account)
stocks = []
result = []
name = input("Enter stock name: ")
interval = int(input("Enter time entirval in minute: "))

# 2st step use chrome webdriver to fetch the url
driver = webdriver.Chrome()

for account in range(len(accounts)):
    # Here we fetch every url from the list
    respose = driver.get(accounts[account])
    # Made this time long to be able login to access real data
    time.sleep(60)
    # 3st step save page content/markup
    html = driver.page_source
    # 4st step create soup object to parse content
    soup = BeautifulSoup(html, "lxml")
    # 5st find all tweets to fetch date and content from it
    account_divs = soup.find_all(
        "div", {"class": "css-175oi2r r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu"}
    )
    # 6st step filter content by time to find tweets in interval we entered
    for account_div in account_divs:
        date = parser.parse(account_div.find("time").attrs["datetime"]).time().minute
        if date <= interval:
            stocks.append(
                account_div.find_all(
                    "a",
                    {
                        "class": "css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1loqt21"
                    },
                )
            )
for row in stocks:
    for column in row:
        result.append(column.text.upper())


# 6st step find the times stock was mention in it
def num_of_stockk(stock_name):
    return result.count(stock_name)


# print(result)
search = num_of_stockk(name)
print(f'""{name}" was mentioned "{search}" times in the last "{interval}" minutes."')
