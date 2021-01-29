# City      Population  Year
# Paris     2248271     2020
# Oslo      1019531     2020
# Athens     664046     2012
# London    8908081     2018


import pandas as pd
# #
# # data = {
# #     'City': ['Paris', 'Oslo', 'Athens', 'London'],
# #     'Population': [2248271,1019531,664046,8908081],
# #     'Year': [2020,2020,2012,2018]
# # }
# #
# # df = pd.DataFrame(data)
# #
# # print(df)



data = {
    'Population': [2248271,1019531,664046,8908081],
    'Year': [2020,2020,2012,2018]
}

df = pd.DataFrame(data, index = ['Paris', 'Oslo', 'Athens', 'London'])

print(df.loc['Paris'])
print('----')
print(df.iloc[3])


df['Country'] = ['France', 'Norway','Greece','England']
df['Growth'] = [512214,5487,-12,8754]
df['Population'] = df['Population'] + df['Growth']
print(df)