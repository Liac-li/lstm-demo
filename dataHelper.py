import os
import time

import numpy as np
import pandas as pd

from tqdm import tqdm, trange

def loadAndDevide(csvfile, output_path):
    df = pd.read_csv(csvfile, encoding='utf-8')

    useids = df['PERSONID'].unique()
    for userid in tqdm(useids):
        tmp_df = df[df['PERSONID'] == userid]
        tmp_df.to_csv(os.path.join(output_path, str(userid) + '.csv'))
        
    print('Data Preprocess Over') 
    
if __name__ == '__main__':
    res_path = 'data/res'
    if not os.path.exists(res_path):
        os.mkdir(res_path)
        
    loadAndDevide('data/raw_train.csv', res_path)
    
