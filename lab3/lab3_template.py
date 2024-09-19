from stock_data import STOCK_DATA # <- No touchy!


## a nested dictionary of STOCK_DATA, you may delete, modify, or use as is
stock_dict = dict()
for stock in STOCK_DATA:
    stock_dict[stock["symbol"]] = stock


# Below is ample code so you can see how to access nested dictionary keys. 
# You can delete this too if you don't need it!
for ticker in stock_dict.keys():
    print(ticker, ": ", stock_dict[ticker]["company"]) # ticker is the same as "symbol"
print("\n\n\n")
print(stock_dict["MMM"])
print(stock_dict["MSFT"]["initial_price"])



# 1. Print the difference between the 2007 price of each stock and the 2002 price. 
# Use conditional logic to indicate with a print statement whether the stock price went up or down.
#### ADD CODE HERE



#### 
# 2. What is the average initial price of all of the companies? 
#### ADD CODE HERE


####
# 3. Save all the stock tickers (The 3-5 letters labeled with "symbol" in each stock dictionary.) to a data structure, 
# you may choose the type (list, dictionary, tuple, string), sort the values to be in alphabetical order using Python. 
# Print all of the tickers in a loop, **two tickers per line.**
#### ADD CODE HERE


#####
# 4. Which company name (not symbol) had the highest stock price in 2002? 
#### ADD CODE HERE


####
#5. Which stock (company or symbol) had the smallest increase from their initial price to 2007? 
# (Decrease in price should not be counted.)
#### ADD CODE HERE


####
