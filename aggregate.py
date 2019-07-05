import pandas as pd
import os, glob

def merge_files():
    # GET PATH
    # os.getcwd() #get current working directory
    dataPath = os.path.join(os.getcwd(), "seperatedData")
    mergedPath = os.path.join(os.getcwd(), "merged.txt")

    #change dir to extracted file
    os.chdir(dataPath)

    # used to get all file extension .txt
    #fileList = glob.glob("*.txt")

    #init dataframe and get all file extension .txt into dataframe
    dfList = [f for f_ in [glob.glob(e) for e in ['*.txt']] for f in f_]
    # print(dfList)

    tempDf = []

    # loop filelist to merge all files
    for filename in dfList:
        # print(filename)
        df = pd.read_csv(filename, header=0)
        # print(df)
        tempDf.append(df)

    # merge file and save to .txt file
    mergeDf = pd.concat(tempDf,axis=0)
    # print(mergeDf)
    mergeDf.to_csv(mergedPath, index=None)

    return


# main method
def main():
    merge_files()

if __name__ == '__main__':
    main()