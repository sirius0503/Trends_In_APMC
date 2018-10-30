mport seaborn as sns, numpy as np
sns.set(); np.random.seed(0)
ax = sns.distplot(df1['msprice'].dropna())
