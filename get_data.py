import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyod.models.hbos import HBOS
from pyod.utils.data import evaluate_print

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

df = pd.read_csv('./data/training/uniq/20160318.csv', header=None, names=column_names, dtype=dtypes, parse_dates=[0])
#df2 = pd.read_csv('./data/march/week3/spam_flows_cut.csv', nrows=100, header=None, names=column_names, dtype=dtypes, parse_dates=[0])

df_group = df.groupby([df['timestamp'].dt.hour, df['timestamp'].dt.minute]).agg(['count'])
xaxis = np.arange(df_group.shape[0])
yaxis = df_group['timestamp'].values[:,0]
plt.plot(xaxis, yaxis)
plt.show()

outlier_fraction = 0.1
X_train = np.concatenate((xaxis, yaxis), axis=1)
#clf_name = 'HBOS'
#clf = HBOS()
#clf.fit(X_train)
#y_train_pred = clf.labels_
#y_train_scores = clf.decision_scores_ 
#evaluate_print(clf_name, y_train, y_train_scores)
