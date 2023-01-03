import numpy as np 
import pandas as pd
from tika import parser
import streamlit as st


#file = r'C:\Users\DHattiyavar\OneDrive - Prolifics Corporation Ltd.,\Desktop\CV\Automated-Resume-Screening-System-master\Original_Resumes\Rohini.pdf'
file = r'C:\Users\DHattiyavar\OneDrive - Prolifics Corporation Ltd.,\Desktop\CV\Automated-Resume-Screening-System-master\Original_Resumes\RajeshNandina.pdf'
file_data = parser.from_file(file)
text = file_data['content']
st.title("Resume Fields Extractor")
st.header('The Input Resume is:')
st.write(text)

st.header('The extracted Information is:')
extracted_text = {}
#E-MAIL
import re
def get_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

email = get_email_addresses(text)
extracted_text["E-Mail"] = email


def get_role(sentences):
    sub_patterns = ['[A-Z][a-z]* Developer','[A-Z][a-z]* lead','[A-Z][a-z]* Engineer','[A-Z][a-z]* leader']
    pattern = '({})'.format('|'.join(sub_patterns))
    role = re.findall(pattern, text)
    return role
role = get_role(text)
extracted_text["ROLE"] = role

sub_patterns = ['Client [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*','Client [A-Z][a-z]*']
pattern = '({})'.format('|'.join(sub_patterns))
client = re.findall(pattern, text)
extracted_text["Client"] = client
# client
new_clients = []
for i in client:
    new_clients.append(i.split('Client ')[1])
extracted_text["Client"] = new_clients
#Extract Organizations
sub_patterns = ['[A-Z][a-z]* Limited','[A-Z][a-z]* Pvt. Ltd.','[A-Z][a-z]* [A-Z][a-z]* Inc.','[A-Z][a-z]* [A-Z][a-z]* Services','[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* Services', '[A-Z][a-z]* Ltd','[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* Services',
                ]
pattern = '({})'.format('|'.join(sub_patterns))
Exp = re.findall(pattern, text)
extracted_text["Organization"] = Exp


st.write(extracted_text)

