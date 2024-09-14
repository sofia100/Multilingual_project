# load ambigous_reln_format.txt and make an excel sheet from it

import pandas as pd
import numpy as np

def load_data(file_path):
    with open(file_path, 'r') as f:
        data = f.readlines()
    return data

def make_excel(data):
    df = pd.DataFrame(columns=['description', 'relation', 'relation_code', 'gender'])
    for i in range(0, len(data), 4):
        df = df.append({'description': data[i].strip(),
                        'relation': data[i+1].strip(),
                        'relation_code': data[i+2].strip(),
                        'gender': data[i+3].strip()}, ignore_index=True)
    return df

def save_excel(df, file_path):
    df.to_excel(file_path, index=False)

def main():
    print("start")
    file_path = 'ambiguos_reln_format.txt'
    data = load_data(file_path)
    df = make_excel(data)
    save_excel(df, 'ambigous_reln_format.xlsx')

if __name__ == '__main__':
    main()
