import investpy
import pandas as pd

serch_result = investpy.search_quotes(text='AAPL', products=['stocks'], countries=['brazil'], n_results= 10)

print(serch_result[0])

print(serch_result[0].retrieve_recent_data())

print(type(serch_result[0].retrieve_recent_data()))