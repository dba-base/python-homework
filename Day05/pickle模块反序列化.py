__author__ = "xiaoyu hao"

import pprint, pickle

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1['a'])

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()

# with open('data.pkl','rb') as fp:
#     data1 = pickle.load(fp)
#     pprint.pprint(data1)

