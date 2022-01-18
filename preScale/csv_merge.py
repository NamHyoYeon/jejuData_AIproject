import pandas as pd
import glob
import os
import sys

path = 'C:/Users/user/Desktop/Data/'
output_file = 'C:/Users/user/Desktop/Data/merge.csv'

all_files = glob.glob(os.path.join(path, '*'))
all_data_frames = []

for file in all_files:
    data_frame = pd.read_csv(file, index_col=None, encoding='utf-8-sig')
    all_data_frames.append(data_frame)

data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)

data_frame_concat.to_csv(output_file, encoding='utf-8-sig', index=False)
