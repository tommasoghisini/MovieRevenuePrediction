import pandas as pd
import numpy as np

Data = pd.DataFrame(data=input_table_1)

def cast(row):
  return [row['actor_1'], row['actor_2'], row['actor_3'], row['actor_4'], row['actor_5']]

def actor_movies(actor):
  A_movies = actor == Data['actor_1']
  A_movies += actor == Data['actor_2']
  A_movies += actor == Data['actor_3']
  A_movies += actor == Data['actor_4']
  A_movies += actor == Data['actor_5']
  return 

def prod_movies(prod_company):
    P_movies = prod_company == Data['production_company']
    return P_movies

def actor_pop(year,actor):
  newData = Data[actor_movies(actor)]
  newData = newData.loc[newData['year'] <= year]
  if len(newData) == 0:
    return 0
  return sum(newData['popularity'])/len(newData)

def prod_pop(year,prod_company):
  newData = Data[prod_movies(prod_company)]
  newData = newData.loc[newData['year'] <= year]
  if len(newData) == 0:
    return 0
  return sum(newData['popularity'])/len(newData)

def actor_bud(year,actor):
  newData = Data[actor_movies(actor)]
  newData = newData.loc[newData['year'] <= year]
  if len(newData) == 0:
    return 0
  return sum(newData['budget'])/len(newData)

def prod_bud(year,prod_company):
  newData = Data[prod_movies(prod_company)]
  newData = newData.loc[newData['year'] <= year]
  if len(newData) == 0:
    return 0
  return sum(newData['budget'])/len(newData)

def actor_rev(year,actor):
  newData = Data[actor_movies(actor)]
  newData = newData.loc[newData['year'] < year]
  if len(newData) == 0:
    return 0
  return sum(newData['revenue'])/len(newData)


def prod_rev(year,prod_company):
	newData = Data[prod_movies(prod_company)]
	newData = newData.loc[newData['year'] < year]
	if len(newData) == 0:
		return 0
	return sum(newData['revenue'])/len(newData)



Data['popularity actor 1'] = np.zeros(len(Data))
Data['popularity actor 2'] = np.zeros(len(Data))
Data['popularity actor 3'] = np.zeros(len(Data))
Data['popularity actor 4'] = np.zeros(len(Data))
Data['popularity actor 5'] = np.zeros(len(Data))

Data['budget actor 1'] = np.zeros(len(Data))
Data['budget actor 2'] = np.zeros(len(Data))
Data['budget actor 3'] = np.zeros(len(Data))
Data['budget actor 4'] = np.zeros(len(Data))
Data['budget actor 5'] = np.zeros(len(Data))

Data['revenue actor 1'] = np.zeros(len(Data))
Data['revenue actor 2'] = np.zeros(len(Data))
Data['revenue actor 3'] = np.zeros(len(Data))
Data['revenue actor 4'] = np.zeros(len(Data))
Data['revenue actor 5'] = np.zeros(len(Data))

Data['popularity production company'] = np.zeros(len(Data))
Data['budget production company'] = np.zeros(len(Data))
Data['revenue production company'] = np.zeros(len(Data))


for i in range(len(Data)):
  row = Data.iloc[i]
  cast_ = cast(row)
  year = row['year']
  actor = cast(row)[0]
  Data['popularity actor 1'][i] = actor_pop(year,actor)
  Data['budget actor 1'][i] = actor_bud(year,actor)
  Data['revenue actor 1'][i] = actor_rev(year, actor)
  actor = cast(row)[1]
  Data['popularity actor 2'][i] = actor_pop(year,actor)
  Data['budget actor 2'][i] = actor_bud(year,actor)
  Data['revenue actor 2'][i] = actor_rev(year, actor)
  actor = cast(row)[2]
  Data['popularity actor 3'][i] = actor_pop(year,actor)
  Data['budget actor 3'][i] = actor_bud(year,actor)
  Data['revenue actor 3'][i] = actor_rev(year, actor)
  actor = cast(row)[3]
  Data['popularity actor 4'][i] = actor_pop(year,actor)
  Data['budget actor 4'][i] = actor_bud(year,actor)
  Data['revenue actor 4'][i] = actor_rev(year, actor)
  actor = cast(row)[4]
  Data['popularity actor 5'][i] = actor_pop(year,actor)
  Data['budget actor 5'][i] = actor_bud(year,actor)
  Data['revenue actor 5'][i] = actor_rev(year, actor)
  prod_company = row['production_company']
  Data['popularity production company'][i] = prod_pop(year,prod_company)
  Data['budget production company'][i] = prod_bud(year,prod_company)
  Data['revenue production company'][i] = prod_rev(year, prod_company)


output_table_1 = Data

