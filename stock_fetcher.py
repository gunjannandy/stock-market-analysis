import urllib.request, json, time, os, itertools
import pandas as pd
from multiprocessing import Pool
from datetime import datetime
try:
	 import httplib
except:
	 import http.client as httplib

def check_internet():
	 conn = httplib.HTTPConnection("www.google.com", timeout=5)
	 try:
		 conn.request("HEAD", "/")
		 conn.close()
		 return True
	 except:
		 conn.close()
		 return False

def get_historic_price(query_url,json_path,csv_path):
	
	loop_limit = 5
	while not check_internet() and loop_limit > 0:
		 print("Could not connect, trying again in 5 seconds...\r",end='')
		 time.sleep(5)
		 loop_limit -=1
	if loop_limit == 0:
		 return
	stock_id=query_url.split("&period")[0].split("symbol=")[1]
	
	try:
		with urllib.request.urlopen(query_url) as url:
			parsed = json.loads(url.read().decode())
	except:
		return
	
	else:
		# print(stock_id)
		# if os.path.exists(json_path+stock_id+'.json'):
		# 	os.remove(json_path+stock_id+'.json')
		# with open(json_path+stock_id+'.json', 'w') as outfile:
		# 	json.dump(parsed, outfile, indent=2)
		# print(stock_id+"                            \r",end=' ')
		try:
			# Date=[]
			# for i in :
			#	 Date.append(datetime.utcfromtimestamp(int(i)).strftime('%d-%m-%Y'))
			Date=parsed['chart']['result'][0]['timestamp']
			Low=parsed['chart']['result'][0]['indicators']['quote'][0]['low']
			Open=parsed['chart']['result'][0]['indicators']['quote'][0]['open']
			Volume=parsed['chart']['result'][0]['indicators']['quote'][0]['volume']
			High=parsed['chart']['result'][0]['indicators']['quote'][0]['high']
			Close=parsed['chart']['result'][0]['indicators']['quote'][0]['close']
			Adjusted_Close=parsed['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']

			df=pd.DataFrame(list(zip(Date,Low,Open,Volume,High,Close,Adjusted_Close)),columns =['Date','Low','Open','Volume','High','Close','Adjusted Close'])

			if os.path.exists(csv_path+stock_id+'.csv'):
				os.remove(csv_path+stock_id+'.csv')
			df.to_csv(csv_path+stock_id+'.csv', sep=',', index=None)
			print(stock_id+"                                          \r",end=' ')
			return
		except:
			return
			
def main():
	start = time.time()
	json_path = os.getcwd()+os.sep+".."+os.sep+"historic_data"+os.sep+"json"+os.sep
	csv_path = os.getcwd()+os.sep+".."+os.sep+"historic_data"+os.sep+"csv"+os.sep

	if not os.path.isdir(json_path):
		os.makedirs(json_path)
	if not os.path.isdir(csv_path):
		os.makedirs(csv_path)

	ticker_file_path = "Assets"+os.sep+"india.csv"
	country_df = pd.read_csv(ticker_file_path)
	# print("Total stocks:",len(country_df))
	# print(country_df.head(10))

	query_urls = []
	for ticker in country_df['Ticker']:
		print("Getting url for "+ticker+"                        \r",end=' ')
		query_urls.append("https://query1.finance.yahoo.com/v8/finance/chart/"+ticker+"?symbol="+ticker+"&period1=0&period2=9999999999&interval=1d&includePrePost=true&events=div%2Csplit")

	print("Getting data:                               ")
	with Pool(processes=10) as pool:
		 pool.starmap(get_historic_price, zip(query_urls, itertools.repeat(json_path), itertools.repeat(csv_path)))

	end= time.time()
	print("All downloads completed , time taken "+str(round(end-start,3))+" sec")


if __name__=="__main__":
	main()