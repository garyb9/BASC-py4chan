from utils import *
import numpy as np
import pandas as pd
import basc_py4chan as bp4
from collections import defaultdict
from os import path
from bs4 import BeautifulSoup as Soup

start = start_timer()
relPath = r'data\\'

def boardToCSV(boardStr):
    boardTag = '/' + boardStr + '/'
    print('Processing Board: ' + boardTag)
    board = bp4.Board(boardStr)
    threads = board.get_all_threads()
    dictDF = defaultdict(list)
    for thread in threads:
        for post in thread.posts:
            dictDF['Board'].append(boardTag)
            dictDF['Post ID'].append(post.post_id)
            dictDF['Subject'].append(post.subject)
            dictDF['Comment'].append(post.comment)
            dictDF['Image URL'].append(post.file1.file_url if post.has_file else None)
    df = pd.DataFrame(data = dictDF)
    df.to_csv(os.path.join(relPath, boardStr + '.csv'))
    print('Wrote Data Frame to ' + boardStr + '.csv')
    print(df)
    print('Done with: ' + boardTag)
    return df

def processBoards(boardsList):
    dfList = []
    for board in boardsList:
        dfList.append(boardToCSV(board))
    dfBoards = pd.concat(dfList)
    dfBoards.to_csv(os.path.join(relPath, '4chan.csv'))
    print(dfBoards)
    return dfBoards

def main():
    df4chan = processBoards(boardsList=['pol', 'v', 'g', 'mu', 'fit', 'vg', 'r9k'])
    print_run_data(start)

if __name__ == "__main__":
    main()