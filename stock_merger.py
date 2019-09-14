import os, glob, difflib, time, datetime
import pandas as pd
seperator = os.path.sep

def main():

	KB = 2**10  # KB = 2^10 Bytes
	threshold_size = 500 *KB   # CSV files below this size won't be taken into consideration 
	
	ticker_name = "HATHWAY.BO"
	company_name = "Jet Airways"

	ticker_file_path = "assets"+seperator+"india.csv"
	ticker_df = pd.read_csv(ticker_file_path)

	csv_path = csv_path = os.getcwd()+seperator+".."+seperator+"historic_data"+seperator+"csv"+seperator

	try:
		if ticker_name:
			ticker_for_the_company = ticker_name
		elif company_name:	
			exact_company_name = (difflib.get_close_matches(company_name, ticker_df['Name'])[0])
			ticker_for_the_company = ticker_df.loc[ticker_df['Name'] == exact_company_name, 'Ticker'].iloc[0]
	
	except:
		# raise
		print("Company name "+company_name+" not found.")
		return
	
	else:
		try:
			merged_df = pd.read_csv(csv_path+ticker_for_the_company+".csv")
		
		except:
			raise
			print("'"+ticker_for_the_company+".csv' not found.")
			return
		
		else:
			file_names = []
			for file_path in glob.glob(csv_path+'*.csv'):
				file_size = os.stat(file_path).st_size
				if file_size < threshold_size:
					continue
				file_names.append(file_path)

			total_count = len(file_names)

			for file_number, file_path in enumerate(file_names):
				temp_df = pd.read_csv(file_path)
				print("Merging ("+str(file_number)+"/"+str(total_count)+") ", file_path.split(seperator)[-1]+"                        \r", end=' ')
				merged_df = pd.merge(merged_df, temp_df, on='Date', how='left')

			# all left over NaN only columns will be removed
			merged_df = merged_df.dropna(axis=1, how='all')

			# change linux time stamp to DD-MM-YY
			merged_df['Date'] = merged_df['Date'].map(lambda x: datetime.datetime.utcfromtimestamp(int(x)).strftime('%d-%m-%Y'))

			merged_file = "assets"+seperator+"Merged.csv"
			if os.path.exists(merged_file):
				os.remove(merged_file)
			print("Saving Merged.csv...                         \r", end=' ')
			merged_df.to_csv(merged_file, sep=',', index=None)
			print("Saved Merged.csv! ("+str(int(os.stat(merged_file).st_size/(2**10)))+" KB)                            ")
			# print(merged_df.head(10))

if __name__ == '__main__':
	start= time.time()
	main()
	end= time.time()
	print("Time taken "+str(round(end-start,3))+" sec")