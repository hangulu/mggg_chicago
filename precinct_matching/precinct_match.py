import numpy as np
import pandas as pd
from scipy import spatial
import collections
import pickle

races = ['white','black','hispanic','asian','middle eastern','undetermined']


demo_cols = ['NH_WHITE', 'NH_BLACK', 'NH_AMIN',	'NH_ASIAN',	'NH_NHPI', 'NH_OTHER', 'NH_2MORE', 'HISP']

df_chic_demo = pd.read_csv('chicago_prec_demo.csv',index_col=0).dropna()[demo_cols]
df_chic_demo.reindex(sorted(df_chic_demo.columns), axis=1)
df_chic_demo = df_chic_demo[(df_chic_demo.T !=0).any()]

df_camb_demo = pd.read_csv('camb_prec_demo.csv',index_col=0).dropna()[demo_cols]
df_camb_demo.reindex(sorted(df_camb_demo.columns), axis=1)
df_camb_demo = df_camb_demo[(df_camb_demo.T !=0).any()]

df_minn_demo = pd.read_csv('minn_prec_demo.csv',index_col=0).dropna()[demo_cols]
df_minn_demo.reindex(sorted(df_minn_demo.columns), axis=1)
df_minn_demo = df_minn_demo[(df_minn_demo.T !=0).any()]

# df_oakl_demo = pd.read_csv('oak_prec_demo.csv',index_col=-1).dropna()[demo_cols]
# df_oakl_demo.reindex(sorted(df_oakl_demo.columns), axis=1)
# df_oakl_demo = df_oakl_demo[(df_oakl_demo.T !=0).any()]
# print(df_oakl_demo)
# df_oakl_demo = df_oakl_demo.groupby('prec_mg')[demo_cols].agg('sum')

# print(df_oakl_demo)


# initialize a dictionary
# keys will be chicago precincts
# values with be pairs (P, s)
# P is a precinct in another city
# s is the cosine similarity in demographic space
chic_dict = {}

for row in df_chic_demo.itertuples():
	distpairs1 = []
	distpairs2 = []

	for r2 in df_camb_demo.itertuples():
		
		distpairs1.append((list(r2)[0],  1 - spatial.distance.cosine(list(row)[1:], list(r2)[1:])))


	for r2 in df_minn_demo.itertuples():

		distpairs2.append((list(r2)[0],  1 - spatial.distance.cosine(list(row)[1:], list(r2)[1:])))

	# for r2 in df_oakl_demo.itertuples():
		
	# 	distpairs.append((list(r2)[0],  1 - spatial.distance.cosine(list(row)[1:], list(r2)[1:])))


	## we're grabbing the 5 most similar in cambridge and the 15 most similar in mpls
	distpairs1.sort(key=lambda x: x[1], reverse=True)
	distpairs2.sort(key=lambda x: x[1], reverse=True)

	chic_dict[list(row)[0]] = distpairs1[:5] + distpairs2[:15]





camb_keep_cols = ['ID','1st Choice','2nd Choice','3rd Choice','4th Choice','5th Choice']
camb_prec_votes = collections.defaultdict(list)




# read in a bunch of election data
# I'm so sorry it has to look like this
df_camb_vote = pd.read_excel('Cambridge City Council CVR 2017.xlsx')

df_camb_vote['ID'] = df_camb_vote['ID'].apply(lambda x: str(x)[2:4] + '-' + str(x)[4:6])
df_camb_vote['ID'] = df_camb_vote['ID'].apply(lambda x: str(x).replace("-0","-"))
df_camb_vote['ID'] = df_camb_vote['ID'].apply(lambda x: str(x)[1:] if str(x)[0] == '0' else str(x))



df_camb_vote = df_camb_vote.drop(columns=[c for c in list(df_camb_vote) if c not in camb_keep_cols ])

df_camb_id = pd.read_csv('camb_demo_id_2017.csv',delimiter='\t',header=None)
df_camb_id = dict(zip(df_camb_id[0],df_camb_id[1]))


for c in camb_keep_cols[1:]:
	df_camb_vote[c] = df_camb_vote[c].apply(lambda e: df_camb_id[e].capitalize() if e in df_camb_id.keys() else np.nan)



df_camb_vote = df_camb_vote[pd.notnull(df_camb_vote['1st Choice'])]



for row in df_camb_vote.itertuples():
	
	camb_prec_votes[list(row)[1]].append(tuple([ str(s).lower().replace("middle eastern","asian") for s in list(row)[2:5]] + []))

####

df_camb_vote = pd.read_excel('Cambridge City Council CVR 2013.xlsx',sheet_name=1)
df_camb_vote['ID'] = df_camb_vote['ID'].apply(lambda x: str(x)[2:4] + '-' + str(x)[4:6])
df_camb_vote['ID'] = df_camb_vote['ID'].apply(lambda x: str(x).replace("-0","-"))
df_camb_vote['ID'] = df_camb_vote['ID'].apply(lambda x: str(x)[1:] if str(x)[0] == '0' else str(x))



df_camb_vote = df_camb_vote.drop(columns=[c for c in list(df_camb_vote) if c not in camb_keep_cols ])




for c in camb_keep_cols[1:]:
	df_camb_vote[c] = df_camb_vote[c].apply(lambda e: str(e).capitalize() if str(e).lower() in races else np.nan)



df_camb_vote = df_camb_vote[pd.notnull(df_camb_vote['1st Choice'])]


df_camb_vote = pd.read_excel('Cambridge City Council CVR 2015.xlsx',sheet_name=1)
df_camb_vote = df_camb_vote.rename(columns={ df_camb_vote.columns[0]: "ID" })

df_camb_vote['ID'] = df_camb_vote['ID'].apply(lambda x: str(x)[2:4] + '-' + str(x)[4:6])
df_camb_vote['ID'] = df_camb_vote['ID'].apply(lambda x: str(x).replace("-0","-"))
df_camb_vote['ID'] = df_camb_vote['ID'].apply(lambda x: str(x)[1:] if str(x)[0] == '0' else str(x))



df_camb_vote = df_camb_vote.drop(columns=[c for c in list(df_camb_vote) if c not in camb_keep_cols ])




for c in camb_keep_cols[1:]:
	df_camb_vote[c] = df_camb_vote[c].apply(lambda e: str(e).capitalize() if str(e).lower() in races else np.nan)



df_camb_vote = df_camb_vote[pd.notnull(df_camb_vote['1st Choice'])]




camb_prec_votes = collections.defaultdict(list)


for row in df_camb_vote.itertuples():
	
	camb_prec_votes[list(row)[1]].append(tuple([ str(s).lower().replace("middle eastern","asian") for s in list(row)[2:5]] + []))









for k,v in camb_prec_votes.items():
	camb_prec_votes[k] = collections.Counter(v)



minn_prec_votes = collections.defaultdict(list)




df_minn_vote = pd.read_csv('2017-mayor-cvr.csv').drop(columns = ['1st Choice','2nd Choice','3rd Choice','Count'])

df_minn_vote = df_minn_vote[pd.notnull(df_minn_vote['1st Choice_Race'])]

for row in df_minn_vote.itertuples():
	k = list(row)[1].replace("MINNEAPOLIS ",'').replace("W-",'W').replace("P-","P").replace(' ','-').replace("P0",'P')

	minn_prec_votes[k].append(tuple(      [ str(s).lower().replace("middle eastern","asian") for s in list(row)[2:]]))# + [np.nan,np.nan]))


df_minn_vote = pd.read_csv('2013-mayor-cvr.csv').drop(columns = ['1ST CHOICE MAYOR MINNEAPOLIS','2ND CHOICE MAYOR MINNEAPOLIS','3RD CHOICE MAYOR MINNEAPOLIS','COUNT'])

df_minn_vote = df_minn_vote[pd.notnull(df_minn_vote['1ST CHOICE MAYOR MINNEAPOLIS_Race'])]






for row in df_minn_vote.itertuples():
	k = list(row)[1].replace("MINNEAPOLIS ",'').replace("W-",'W').replace("P-","P").replace(' ','-').replace("P0",'P')

	minn_prec_votes[k].append(tuple(      [ str(s).lower().replace("middle eastern","asian") for s in list(row)[2:]]))# + [np.nan,np.nan]))




df_minn_vote = pd.read_csv('2017-ward-4-cvr.csv').drop(columns = ['1st Choice','2nd Choice','3rd Choice','Count'])

df_minn_vote = df_minn_vote[pd.notnull(df_minn_vote['1st Choice_Race'])]

for row in df_minn_vote.itertuples():
	k = list(row)[1].replace("MINNEAPOLIS ",'').replace("W-",'W').replace("P-","P").replace(' ','-').replace("P0",'P')

	minn_prec_votes[k].append(tuple(      [ str(s).lower().replace("middle eastern","asian") for s in list(row)[2:]]))# + [np.nan,np.nan]))



df_minn_vote = pd.read_csv('2017-ward-5-cvr.csv').drop(columns = ['1st Choice','2nd Choice','3rd Choice','Count'])

df_minn_vote = df_minn_vote[pd.notnull(df_minn_vote['1st Choice_Race'])]

for row in df_minn_vote.itertuples():
	k = list(row)[1].replace("MINNEAPOLIS ",'').replace("W-",'W').replace("P-","P").replace(' ','-').replace("P0",'P')

	minn_prec_votes[k].append(tuple(      [ str(s).lower().replace("middle eastern","asian") for s in list(row)[2:]]))# + [np.nan,np.nan]))


df_minn_vote = pd.read_csv('2017-ward-11-cvr.csv').drop(columns = ['1st Choice','2nd Choice','3rd Choice','Count'])

df_minn_vote = df_minn_vote[pd.notnull(df_minn_vote['1st Choice_Race'])]

for row in df_minn_vote.itertuples():
	k = list(row)[1].replace("MINNEAPOLIS ",'').replace("W-",'W').replace("P-","P").replace(' ','-').replace("P0",'P')

	minn_prec_votes[k].append(tuple(      [ str(s).lower().replace("middle eastern","asian") for s in list(row)[2:]]))# + [np.nan,np.nan]))


for k,v in minn_prec_votes.items():
	minn_prec_votes[k] = collections.Counter(v)


chic_impute = collections.defaultdict(dict)


for k,v in camb_prec_votes.items():
	if v == []:
		print("remove")
		camb_prec_votes.pop(k,None)



# for each precinct in chicago
# for each match precint P in that dictionary
# use the weight s on P times the percentage of
#.  people in P voting each preference schedule
#.  and sum, then normalize so that the total
#.  votes is equal to VAP
for prec in chic_dict.keys():
	for match in chic_dict[prec]:

		# if minn
		if match[0][0] == 'W':

			for k,v in minn_prec_votes[match[0]].items():
				
				if k in chic_impute[prec].keys():
					chic_impute[prec][k] += v*match[1]**1
				else:
					chic_impute[prec][k] = v*match[1]**1



		# camb
		else:
			if match[0] == "3-2A":
				m = "3-2"
			else: 
				m = match[0]

			for k,v in camb_prec_votes[m].items():
				
				if k in chic_impute[prec].keys():
					chic_impute[prec][k] += v*match[1]**1
				else:
					chic_impute[prec][k] = v*match[1]**1


df_chic_demo = pd.read_csv('chicago_prec_demo.csv',index_col=0).dropna()

for k,v in chic_impute.items():
	tot = sum(list(v.values()))
	
	for k2 in v.keys():
		v[k2] = v[k2]/tot * df_chic_demo.at[k,'VAP']





# save the results as a dictionary in pickle

# this is a dictionary with keys chicago precincts
# values: a dictionary with keys vote schedules and values
#. estimated counts of votes for that schedule
with open('chicago_rcv_race_3','wb') as f:
	pickle.dump(chic_impute,f)


# we'll save our demographic dictionary too, just because
with open('chicago_prec_matches','wb') as f:
	pickle.dump(chic_dict,f)













