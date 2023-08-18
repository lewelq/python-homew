import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data['ones'] = 1
pivot_table = pd.pivot_table(data, values='ones', columns=['whoAmI'], aggfunc=sum)
pivot_table.columns = [col + '_onehot' for col in pivot_table.columns]
result = pd.concat([data, pivot_table], axis=1)
result.drop('ones', axis=1, inplace=True)
print(result.head())
