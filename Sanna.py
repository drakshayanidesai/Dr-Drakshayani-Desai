import streamlit as st
import pandas as pd
from simplet5 import SimpleT5

df = pd.read_csv(r'C:\Users\DHattiyavar\AppData\Roaming\Python\Python39\site-packages\headline-text.csv')
st.title('T5 Transformer: Text Generation from Headings and Sub-Headings')
from sklearn.model_selection import train_test_split

train_df, test_df = train_test_split(df,test_size=0.3)
train_df.shape, test_df.shape

model = SimpleT5()

model.from_pretrained(model_type ="t5",model_name = "t5-base")
model.train(train_df=train_df[:5000],
            eval_df=test_df[:100],
            source_max_token_len = 128, 
            target_max_token_len = 50,
            batch_size = 8,max_epochs = 5,use_gpu = True)
st.header('The Input Text Used for Training is:')
RFP_Executive_Summary="""Prolifics is pleased to respond to Campbell’s Integration Strategy and Implementation RFP. 
We have a wealth of direct experience in similar such engagements with numerous clients across industries, including CPG. 
As described within this document, Prolifics can bring to bear a comprehensive strategy to help Campbell’s realize their digital transfor mation strategy"""

RFP_Context="""Prolifics has the following initial understanding of Campbell’s vision. As we move forward we will validate and refine this understanding as part of the Strategic Alignment Phase offered herein.
Business Vision: The Campbell Soup Company is an iconic food company that produces meals, beverages, and snacks and generates over USD 8.5 billion in annual revenue.
Campbell’s is embarking upon a journey of Digital transformation to unlock its full growth potential to build a stronger company that is prepared for the future. Campbell’s is already on the path of transforming innovation capabilities thru technology and culture.
Technology Vision :To improve reliability and availability as well as build greater flexibility and scalability into its core business technology environments, Campbell’s migrated to a single ERP platform on cloud. 
This helped to achieve high availability, scalability and improved resiliency at a global level, which has greatly reduced downtime, made manufacturing more resilient, and gained deeper insights into its supply chain
"""

st.header('The Given Title is:')
model.predict(RFP_Executive_Summary)
st.header(RFP_Executive_Summary)

st.header('The Predicted Paragraph is:')
model.predict(RFP_Context)
st.header(RFP_Context)
