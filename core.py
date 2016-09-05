import requests
import bs4

current_data = requests.get('http://www.morningstar.com/stocks/xnas/msft/quote.html')
prior_income_statement = requests.get('http://financials.morningstar.com/income-statement/is.html?t=MSFT&region=USA&culture=en_US')
prior_balance_sheet = requests.get('http://financials.morningstar.com/balance-sheet/bs.html?t=MSFT&region=usa&culture=en-US')
prior_cash_flow = requests.get('http://financials.morningstar.com/cash-flow/cf.html?t=MSFT&region=usa&culture=en-US')


# This is the page tag for last price
# //*[@id="last-price-value"]


