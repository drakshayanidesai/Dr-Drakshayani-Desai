#!/usr/bin/env python
# coding: utf-8

# In[77]:


#get_ipython().system('pip install recordlinkage')
import recordlinkage
from recordlinkage.datasets import load_febrl2
df = load_febrl2()
import pandas as pd
import numpy as np
import streamlit as st


# In[78]:
st.title('The input data set with duplicates is:')

df


# In[79]:


#df.info()


# In[80]:


#df.describe()


# In[81]:


df = df.astype(str).apply(lambda x: x.str.upper())


# In[82]:


#df


# In[83]:


import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize,sent_tokenize
nltk.download('perluniprops')
nltk.download('nonbreaking_prefixes')

from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer


# In[84]:


name_stopword = ["STREET", "ST", "PLACE", "RD", "ROAD"] 
df ['address_1_token'] = df['address_1'].apply(word_tokenize)
df['address_1_clean'] = df['address_1_token'].apply(lambda x: [word for word in x if word not in name_stopword])
df ['address_1_clean'] = df['address_1_clean'].apply(TreebankWordDetokenizer().detokenize)


# In[85]:


#df


# In[9]:


df=df.drop(columns=['address_1_token','address_1'],axis=1)


# In[10]:


#df


# In[11]:


df['postcode'] = df['postcode'].str.strip()
df['postcode']=df['postcode'].str.findall('[0-9]+')
df['postcode'] = df['postcode'].str.join("")
df['postcode'] = df['postcode'].fillna("")


# In[12]:


#df


# In[13]:


df['address_1_clean'] = df['address_1_clean'].str.replace("[\'\".,()*+&\/\-\\\+\!\%:;?]"," ")
df['address_2'] = df['address_2'].str.replace("[\'\".,()*+&\/\-\\\+\!\%:;?]"," ")


# In[14]:


from recordlinkage.index import Full
Full_Index_Table = Full().index(df)


# In[15]:


#st.header('Table Records: {len(df)} records,No of pairs: {len(Full_Index_Table)} pairs')


# In[16]:


from recordlinkage.index import Block
Block_Index_by_State = Block(left_on="state",right_on=None)
Block_Index_by_State_Pairs = Block_Index_by_State.index(df)


# In[17]:


#st.header('Table Records: {len(df)} records,No of pairs: {len(Block_Index_by_State_Pairs)} pairs')


# In[18]:


from recordlinkage.index import SortedNeighbourhood
Neighbour_Index_by_Name = SortedNeighbourhood(left_on="surname",right_on=None,window = 5)
Neighbour_Index_by_Name_Pairs = Neighbour_Index_by_Name.index(df)


# In[19]:


#st.header('Table Records: {len(df)} records,No of pairs: {len(Neighbour_Index_by_Name_Pairs)} pairs')


# In[20]:


#Combine the index Pairs Together
All_Index_Pairs = Block_Index_by_State_Pairs.append(Neighbour_Index_by_Name_Pairs)
#Remove duplicate Pairs 
All_Index_Pairs = All_Index_Pairs.drop_duplicates(keep='first')


# In[21]:


#All_Index_Pairs


# In[22]:


#df


# In[23]:


## create similarity measure 
compare = recordlinkage.Compare()
compare.string('given_name','given_name', method='jarowinkler', label = 'given_name_score')
compare.string('surname','surname', method='jarowinkler', label = 'surname_score')
compare.string('street_number','street_number', method='levenshtein', label = 'street_number_score')
compare.string('address_1_clean','address_1_clean', method='jarowinkler', label = 'address_1_score')
compare.string('address_2','address_2', method='jarowinkler', label = 'address_2_score')
compare.string('suburb','suburb', method='jarowinkler', label = 'suburb_score')
compare.string('postcode','postcode', method='levenshtein', label = 'postcode_score')
compare.string('state','state', method='jarowinkler', label = 'state_score')
compare.string('date_of_birth','date_of_birth', method='levenshtein', label = 'date_of_birth_score')
compare.string('soc_sec_id','soc_sec_id', method='levenshtein', label = 'soc_sec_id_score')
comparison_vectors = compare.compute(All_Index_Pairs,df)


# In[24]:


#comparison_vectors.head(5)


# In[25]:


df1,links = load_febrl2(return_links=True)


# In[26]:


#df1


# In[27]:


#df1.info()


# In[28]:


#df1.describe()


# In[29]:


df1 = df1.astype(str).apply(lambda x: x.str.upper())


# In[30]:


#df1


# In[31]:


name_stopword = ["STREET", "ST", "PLACE", "RD", "ROAD"] 
df1 ['address_1_token'] = df1['address_1'].apply(word_tokenize)
df1['address_1_clean'] = df1['address_1_token'].apply(lambda x: [word for word in x if word not in name_stopword])
df1 ['address_1_clean'] = df1['address_1_clean'].apply(TreebankWordDetokenizer().detokenize)


# In[32]:


df1=df1.drop(columns=['address_1_token','address_1'],axis=1)


# In[33]:


#df1


# In[34]:


df1['postcode'] = df1['postcode'].str.strip()
df1['postcode']=df1['postcode'].str.findall('[0-9]+')
df1['postcode'] = df1['postcode'].str.join("")
df1['postcode'] = df1['postcode'].fillna("")


# In[35]:


#df1


# In[36]:


df1['address_1_clean'] = df1['address_1_clean'].str.replace("[\'\".,()*+&\/\-\\\+\!\%:;?]"," ")
df1['address_2'] = df1['address_2'].str.replace("[\'\".,()*+&\/\-\\\+\!\%:;?]"," ")


# In[37]:


from recordlinkage.index import Full
Full_Index_Table = Full().index(df1)


# In[38]:


#print(f"Table Records: {len(df1)} records,No of pairs: {len(Full_Index_Table)} pairs")


# In[39]:


from recordlinkage.index import Block
Block_Index_by_State = Block(left_on="state",right_on=None)
Block_Index_by_State_Pairs = Block_Index_by_State.index(df1)


# In[40]:


#print(f"Table Records: {len(df1)} records,No of pairs: {len(Block_Index_by_State_Pairs)} pairs")


# In[41]:


from recordlinkage.index import SortedNeighbourhood
Neighbour_Index_by_Name = SortedNeighbourhood(left_on="surname",right_on=None,window = 5)
Neighbour_Index_by_Name_Pairs = Neighbour_Index_by_Name.index(df1)


# In[42]:


#print(f"Table Records: {len(df1)} records,No of pairs: {len(Neighbour_Index_by_Name_Pairs)} pairs")


# In[43]:


#Combine the index Pairs Together
All_Index_Pairs = Block_Index_by_State_Pairs.append(Neighbour_Index_by_Name_Pairs)
#Remove duplicate Pairs 
All_Index_Pairs = All_Index_Pairs.drop_duplicates(keep='first')


# In[44]:


#All_Index_Pairs


# In[45]:


#df1


# In[46]:


## create similarity measure 
compare = recordlinkage.Compare()
compare.string('given_name','given_name', method='jarowinkler', label = 'given_name_score')
compare.string('surname','surname', method='jarowinkler', label = 'surname_score')
compare.string('street_number','street_number', method='levenshtein', label = 'street_number_score')
compare.string('address_1_clean','address_1_clean', method='jarowinkler', label = 'address_1_score')
compare.string('address_2','address_2', method='jarowinkler', label = 'address_2_score')
compare.string('suburb','suburb', method='jarowinkler', label = 'suburb_score')
compare.string('postcode','postcode', method='levenshtein', label = 'postcode_score')
compare.string('state','state', method='jarowinkler', label = 'state_score')
compare.string('date_of_birth','date_of_birth', method='levenshtein', label = 'date_of_birth_score')
compare.string('soc_sec_id','soc_sec_id', method='levenshtein', label = 'soc_sec_id_score')
comparison_vectors = compare.compute(All_Index_Pairs,df1)


# In[47]:


#comparison_vectors.head(5)


# In[ ]:





# In[48]:


duplicate_pairs_vectors = compare.compute(links,df1)


# In[49]:


duplicate_pairs = duplicate_pairs_vectors.reset_index()
duplicate_pairs_1 = duplicate_pairs["level_0"]+ ',' + duplicate_pairs["level_1"]
duplicate_pairs_2 = duplicate_pairs["level_1"]+ ',' + duplicate_pairs["level_0"]
final_duplicate_pairs = pd.DataFrame(duplicate_pairs_1.append(duplicate_pairs_2))
comparison_pairs = comparison_vectors.reset_index()
comparison_pairs['join_keys'] = comparison_pairs["rec_id_1"]+','+comparison_pairs["rec_id_2"]
# 1 represent Duplicates, 0 represent non duplicates
comparison_pairs['Label'] = np.where(comparison_pairs["join_keys"].isin(final_duplicate_pairs[0]),"1","0")
comparison_pairs.groupby(['Label'])['join_keys'].count()


# In[50]:


#get_ipython().system('pip install xgboost')


# In[51]:


import xgboost as xgb
from xgboost import XGBClassifier
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


# In[52]:


## Model Training



#Index Composite Variables
Model_Data_Set = comparison_pairs.set_index(['join_keys','rec_id_1','rec_id_2'])

#Split Data Into Label and Features
y= Model_Data_Set.Label
x= Model_Data_Set.drop(['Label'],axis=1)

#Create Training & Test Set 
seed = 10
test_size = 0.4
x_train, x_test, y_train, y_test = model_selection.train_test_split(x,y,test_size=test_size, random_state=seed, stratify=y)

pd.Series(y_test).value_counts()


# In[53]:


#Apply XGB Model 
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_train = le.fit_transform(y_train)
model= xgb.XGBClassifier(learning_rate = 0.05, n_estimators=300, max_depth=5)
model.fit(x_train, y_train)
#print(model)

y_pred = pd.DataFrame(model.predict(x_test))
predictions = y_pred
predictions['predict'] = y_pred


st.title('The List of Duplicates are:')
dfcombine = pd.merge(x_test.reset_index(),predictions[['predict']],how='left',left_index= True, right_index = True)
#st.write(dfcombine)


# In[59]:


dfcombine.loc[dfcombine["predict"] == 1]
st.write(dfcombine)


# In[ ]:



