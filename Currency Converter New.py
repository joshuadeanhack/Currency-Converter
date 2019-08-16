from __future__ import division

rates = { "GBP-EUR":1.10, "EUR-USD":1.11, "GBP-USD":1.22, "GBP-YEN": 129.36 }

def find(rates, fx):
	try:
		return rates[fx]
	except:
		return -1


def getInputs():
	amount = raw_input("Enter amount: ")
	firstCurrency = raw_input("Enter Currency To Convert From: ")
	secCurrency = raw_input("Enter Currency To Convert To: ")
	try:
		fAmount = float(amount)
		sFirst = str(firstCurrency)
		sSecond = str(secCurrency) 
		if fAmount>0 and len(sFirst)==3 and len(sSecond)==3:		
			return fAmount, sFirst, sSecond	
	except Exception as e:
		print e
	else:
		print "Please specify a positive number and a Currency Symbol e.g. USD"
	if amount=="-999" or firstCurrency=="-999" or secCurrency=="-999":
		return 0,"",""		#Something to escape the recursion
	return getInputs()


def main():
	amount,currency1,currency2 = getInputs()
	
	rate = find(rates,currency1 + "-" + currency2)	
	if rate == -1:
		rate = 1/ find(rates,currency2 + "-" + currency1) 	#Try the other way around
	if rate == -1:
		print "Currency Pair Not Found"		#Neither way works, wrong inputs
		return main()
	return "{} {} converted to {} is: {:.2f}".format(amount,currency1,currency2,rate*amount)

print main()
