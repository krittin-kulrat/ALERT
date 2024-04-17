
import os
import pandas as pd


def preprocess(path: str, src: str):
    # Convert the path to absolute path
    abs_file_path = os.path.abspath(path)
    src = src.lower()
    if (abs_file_path[abs_file_path.rfind('.'):] == '.dat' and
       src == 'fallaiid'):
        # FallAIID data
        print('FallAIID')
    elif (abs_file_path[abs_file_path.rfind('.'):] == '.csv' and
          src == 'umafall'):
        # UMAFall or Arco
        print('UMAFall')
    elif (abs_file_path[abs_file_path.rfind('.'):] == '.csv' and
          src == 'arco'):
        print('Arco')
    else:
        raise ValueError("Unsupported database or incorrect file type")

def load_arco(path: str):
    df = pd.read_csv(path)
    if 'Feature Line' not in df.columns:
        raise ValueError("Unexpected file structure")
    for i in df['Feature Line'].unique():

