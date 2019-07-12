import pandas as pd, numpy as np
import os, glob, patoolib

def pivot(extractedPath):
	extractedFileList = os.listdir("Extracted")
	for filename in extractedFileList:
		if filename in ['Concatenated-Merged.csv']:
			df = pd.read_csv(os.path.join(extractedPath, filename), header=0, index_col=None)
			# manipulate data
			df = df.replace(-9999,np.nan)
			df["Temp"]=df["Temp"]/10.0
			# table = pd.pivot_table(df, index=["ID"], columns="Year", values="Temp")
			table = pd.pivot_table(df, index=["ID", "Year"], values=["Temp","DewTemp","WindSpeed"], 
				aggfunc={ 'Temp' : [min, max, np.mean],
						  'DewTemp' : [min, max, np.mean],
						  'WindSpeed' : [min, max, np.mean] } )
			print(table)

	# write to new csv file
	if "Pivoted_Data.csv" not in extractedFileList:
		table.to_csv(os.path.join(extractedPath, "Pivoted_Data.csv"))
	else:
		print(filename + " already exist!")
		
	return

def extractFiles(compressedData, extractedPath):
	# patoolib can extract .zip, .gz, .tar, .rar, etc..
	# patoolib.extract_archive('<zip_filename>', outdir='<path>', program='<zip_program>')
	# if no outdir, file will be extracted to current dir
	# patoolib.extract_archive('testing.rar')

	filesList = [f for f_ in [glob.glob(e) for e in ['*.zip']] for f in f_]
    # print (filesList)

	if not os.path.exists(extractedPath):
		os.makedirs(extractedPath)

	extractedFileList = os.listdir("Extracted")
	extractedFile = []
	for ef in extractedFileList:
		extractedFile.append(os.path.splitext(ef)[0])
		# print (extractedFile)

	for f in filesList:
        # convert from list to string
		filename = f.split('.')[0]
		# print (filename)
		# print (extractedFile)

		if filename not in extractedFile:
            # print(f)
			patoolib.extract_archive(f, outdir=extractedPath)
		else:
			print(filename + " already exist!")

	return

# main method
def main():
	print('Start')

	compressedData = os.path.join(os.getcwd(), "Concatenated-Merged.zip")
	extractedPath = os.path.join(os.getcwd(), "Extracted")

	print('Extracting File')
	extractFiles(compressedData, extractedPath)
	print('Pivoting table')
	pivot(extractedPath)

	print('Finish')
    

if __name__ == '__main__':
    main()