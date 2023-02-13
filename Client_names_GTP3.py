import streamlit as st

import pandas as pd
import openai
import numpy as np
import pickle
from tika import parser

COMPLETIONS_MODEL = "code-davinci-002"
openai.api_key = "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"


#st.header('The Input Resume is:')
file = st.file_uploader("Choose a resume for parsing")
file_data = parser.from_file(file)
context = file_data['content']
st.header('The Input Resume is:')
st.write(context)
openai_prompt =  context
openai_prompt += '''

Answer the following questions:
 - Email?

 - Client name with role and duration?



Answers: 
'''


Client_names = openai.Completion.create(
    prompt=openai_prompt,
    temperature=0,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    model=COMPLETIONS_MODEL
)["choices"][0]["text"].strip(" \n")


st.title('The extracted information Email, Client, Role and Duration is:')
st.write(Client_names)