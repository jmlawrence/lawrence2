# VERSION 0.0.13.0 | STABLE 

import pandas as pd
import numpy as np

def initialize(context):
	set_symbol_lookup_date('2014-07-12')
	context.spy = symbol('SPY')
	context.dow = symbol("DOW")

	# USER SETTINGS START #
	
	context.bear_stock = symbol('COKE') # Bear Stock
	context.bull_stock = symbol('PEP') # Bull Stock

	# Whether the log should output extra info
	context.display_extra_info = True 

	# Shares to be traded per transaction
	context.bear_shares = 1000 
	context.bull_shares = 2500
	
	context.day = 0

	# The commisions per trade
	set_commission(commission.PerTrade(cost=5.00))

	# USER SETTINGS END #


def handle_data(context, data):
	c = context
	c.data = data
	coke = c.bear_stock
	pepsi = c.bull_stock
	coke_shares = dollars_of_shares(5000, coke, c)
	pepsi_shares = dollars_of_shares(5000, pepsi, c)
	c.stocks = [c.bear_stock, c.bull_stock]
	normal_spread = 20.39





#### AVAILABLE FUNCTIONS START ####

# spread_of([stock A], [stock B], [normal], c)
#		-> Returns the percentage(%) of spread between the two stocks off from the normal difference

# once_a_week(c)
# 	-> Returns whether it has been a week since last trade or not

# dollars_of_shares([dollar amount per trade], [stock to trade], c)
#		-> Returns the number of shares the given amount of money can buy of that stock at market price

# spy_is(["up" or "down"], c)           
#   -> Returns whether the S&P 500 is down or up for the day

# dow_is(["up" or "down"], c)        
#   -> Returns whether the Dow Jones Industrial Average is down or up for the day

# time_is(["time"])      
#   -> Returns whether it is a given time or not

# end_of_day(c)             
#   -> Returns whether it is 2:59 p.m. CST

# current_price([stock], c)    
#   -> Returns the current price of the given stock

# opening_price([stock], c)    
#   -> Returns the opening price for current day of the given stock

# percent_change([stock], c)    
#   -> Returns the percentage the stock has changed since opening

# close_positions(c)        
#   -> Closes all open market positions

# get_last_price([stock], c)
#   -> Returns the price of the stock price of the previous minute

# average_of([sample size], ["sample denomination"], [stock], c) 
#   -> Returns the average price of the given stock's sample size * sample denomination

# buy([stock], c)
#   -> Buys the predetermined amount of the given stock 

# sell([stock], c)
#   -> Sells the predetermined amount of the given stock

# cash_is(c)
#   -> Returns the amount of liquid assets available in portfolio 

# price_change([stock], c)
#   -> Returns for the given stock what percentage the price has change since last tick

# volume_is([stock], c)
#   -> Returns the volume for the given stock at the moment

# next_day(c)
#		-> Tells computer that it is the next day - needed when trying to do something once a week

####  AVAILABLE FUNCTIONS END  ####
				




				
				
				


				
				
				
				
# START TRADING LOOP #    
				
		
	if time_is("1:30"):
		next_day(c)
		if spread_of(coke, pepsi, normal_spread, c) < -1:
			buy(coke, coke_shares, c)
			sell(pepsi, pepsi_shares, c)
				
		elif spread_of(coke, pepsi, normal_spread, c) > 1:
			sell(coke, coke_shares, c)
			buy(pepsi, pepsi_shares, c)

					
	if end_of_day() and once_a_week(c):
		print("2%" < "23%")
		close_positions(c)
												


# END TRADING LOOP # 
												
												
												
												

												


												
												

												
												
												
												
# HELPER FUNCTIONS #
def next_day(c):
	c.day += 1

def dollars_of_shares(amount, stock, c):
	return amount/current_price(stock, c) 

def price_change(stock, c):
	return abs((current_price(stock, c)/get_last_price(stock, c))-1) * 100
		
def spread_of(bearStock, bullStock, normal, context):
	return (((current_price(bullStock, context) / current_price(bearStock, context)) - 1) * 100) - normal

def once_a_week(context):
	return (context.day % 5 == 5)

def buy(stock, amount, c):
	trade("buy", stock, amount, c)

def sell(stock, amount, c):
	trade("sell", stock, amount, c)
				
def percent_change(stock, context):
	return (current_price(stock, context) / opening_price(stock, context))

def opening_price(stock, context):
	return context.data[stock].open_price

def current_price(stock, context):
	return context.data[stock].price

def close_positions(context):
	log.info("# START CLOSING ALL POSITIONS #")
	for stock in context.stocks:
		if context.portfolio.positions[stock].amount < 0:
			trade("buy", stock, context.portfolio.positions[stock].amount, context)
		elif context.portfolio.positions[stock].amount > 0:
			trade("sell", stock, context.portfolio.positions[stock].amount, context)
	log.info("# ALL POSITIONS CLOSED #")
				
def end_of_day():
	return time_is("2:59")
				
def spy_is(string, c):
	if string.lower() == "up":
		return c.data[c.spy].open_price < c.data[c.spy].price
	else:
		return c.data[c.spy].open_price > c.data[c.spy].price

def dow_is(string, c):
	if string.lower() == "up":
		return c.data[c.dow].open_price < c.data[c.dow].price
	else:
		return c.data[c.dow].open_price > c.data[c.dow].price

def get_last_price(stock, c):
	hist = history(bar_count=3, frequency='1m', field='price')
	return hist[stock][-3]

def average_of(num, timeInterval, stock, context):
	timeInterval = timeInterval.lower()
	if timeInterval == "day" or timeInterval == "days":
		if num == 1:
			hist = history(bar_count=1, frequency='1d', field='price')
		elif num == 7 or num == "week":
			hist = history(bar_count=7, frequency='1d', field='price')
		elif num == 30 or num == "month":
			hist = history(bar_count=30, frequency='1d', field='price')
		elif num == 365 or num == "year":
			hist = history(bar_count=365, frequency='1d', field='price')

	elif timeInterval == "hour" or timeInterval == "hours":
		if num == 1:
			hist = history(bar_count=60, frequency='1m', field='price')
		elif num == 2:
			hist = history(bar_count=120, frequency='1m', field='price')
		elif num == 3:
			hist = history(bar_count=180, frequency='1m', field='price')
		elif num == 4:
			hist = history(bar_count=240, frequency='1m', field='price')

		elif timeInterval == "minutes" or timeInterval == "minute":    
			if num == 1:
				hist = history(bar_count=2, frequency='1m', field='price')
			elif num == 5:
				hist = history(bar_count=5, frequency='1m', field='price')
			elif num == 10:
				hist = history(bar_count=10, frequency='1m', field='price')
			elif num == 25:
				hist = history(bar_count=25, frequency='1m', field='price')
			elif num == 50:
				hist = history(bar_count=50, frequency='1m', field='price')
			elif num == 100:
				hist = history(bar_count=100, frequency='1m', field='price')
			elif num == 180:
				hist = history(bar_count=180, frequency='1m', field='price')

	return hist.mean()[stock]

def volume_is(stock, context):
	return context.data[stock].volume

def cash_is(context):
	return  context.portfolio.cash

def time_is(s):
	currentTime = get_datetime()
	hourAndMinute = parseTime(s)
	currentHour = str((currentTime.hour - 5) % 12)
	currentHour = "12" if currentHour == "0" else currentHour
	currentMin = str(currentTime.minute)
	currentMin = checkDigits(currentMin)
	return (hourAndMinute[0] == currentHour and hourAndMinute[1] == currentMin)

def parseTime(s):
	minute = s[-2:]
	hour = s[:-3]
	return [hour, minute]

def displayTime():
	time = get_datetime()
	currentHour = str((time.hour - 5) % 12)
	currentHour = "12" if currentHour == "0" else currentHour
	currentMin = checkDigits(time.minute)
	return(currentHour + ":" + currentMin)

def display_info(context, stock, data):
	avg = average_of(1, "day", stock, context)
	content = "Current Price > AVG" if (avg < context.data[stock].price) else "Current Price < AVG"
	log.info("AVG: {0} | Current Price: ${1} | {2} | VOL: {3}".format(
		avg, context.data[stock].price, content, context.data[stock].volume))

def checkDigits(num):
	s = str(num)
	if len(s) == 1:
		return ("0" + s)
	else:
		return s
						
def getAmOrPm():
	if get_datetime().hour < 17:
		return "a.m."
	else:
		return "p.m."
				
def trade(command, stock, amount, c):
	if amount != 0 and amount != None:
		shares = abs(amount)
		data = c.data
		if command.lower() == "buy":
			order(stock, shares)
		else:
			order(stock, -shares)
						
		log.info("Placing an order to {0} {1} shares at {2} {3} at ${4} per share.".format(
			command.upper(), shares, displayTime(), getAmOrPm(), data[stock].price))

		if c.display_extra_info: 
			display_info(c, stock, data)
