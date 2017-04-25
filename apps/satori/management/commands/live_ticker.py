#http://finance.google.com/finance/info?client=ig&q=NSE:HDFC

"""

>>> from yahoo_finance import Share
>>> yahoo = Share('YHOO')
>>> print yahoo.get_open()
'36.60'
>>> print yahoo.get_price()
'36.84'
>>> print yahoo.get_trade_datetime()
'2014-02-05 20:50:00 UTC+0000'

"""