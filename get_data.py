import numpy as np
import pandas as pd
from pyod.models.knn import KNN
from joblib import dump, load

column_names = [
    'timestamp', 'duration', 'source_ip', 'dst_ip', 'source_port', 'dst_port',
    'protocol', 'flags', 'forward_status', 'type_of_service', 'packets', 'bytes', 'type'
]

dtypes = {
    #'timestamp': datetime,
    'duration': float,
    'source_ip': str,
    'dst_ip': str,
    'source_port': int,
    'dst_port': int,
    'protocol': str,
    'flags': str,
    'forward_status': int,
    'type_of_service': int,
    'packets': int,
    'bytes': int,
    'type': str
}

df = pd.read_csv('./data/training/uniq/20160318.csv', nrows=10000, header=None, names=column_names, dtype=dtypes, parse_dates=[0])
df2 = pd.read_csv('./data/march/week3/spam_flows_cut.csv', nrows=100, header=None, names=column_names, dtype=dtypes, parse_dates=[0])

print(df.head(10))
print('-------\n\n')
print(df2.head(10))
print('*******\n\n')
df_group = df.groupby([df['timestamp'].dt.time]).mean()
print(df_group.head(10))
