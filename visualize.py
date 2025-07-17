#importing packages
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#func to get dataset names
datasets = sns.get_dataset_names()

#loop through the dataset in sns
for data in datasets:
    print(data)

if 'healthexp' in datasets:
    print('the healthexp dataset is available')
else:
    print('the healthexp dataset is not available')

#loading healthexp
healthexp = sns.load_dataset('healthexp')
healthexp.head()

sns.jointplot(
    data=healthexp, 
    x="Spending_USD", 
    y="Life_Expectancy"
)
plt.savefig('jointplot_basic.png')

#adding a regression line to the plot
sns.jointplot(
    data=healthexp, 
    x="Spending_USD", 
    y="Life_Expectancy", 
    kind = 'reg'
)
plt.savefig('jointplot_reg.png')

sns.jointplot(
    data=healthexp, 
    x="Spending_USD", 
    y="Life_Expectancy", 
    hue='Country'
)
plt.savefig('jointplot_hue.png')

healthexp["Spending_USD_log"] = np.log10(healthexp["Spending_USD"])
sns.jointplot(
    data=healthexp, 
    x="Spending_USD_log", 
    y="Life_Expectancy", 
    hue='Country'
)
plt.savefig('jointplot_log_hue.png')
