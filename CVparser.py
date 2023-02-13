import numpy as np 
import pandas as pd
from tika import parser
import streamlit as st


#file = r'C:\Users\DHattiyavar\OneDrive - Prolifics Corporation Ltd.,\Desktop\CV\Automated-Resume-Screening-System-master\Original_Resumes\Rohini.pdf'
#file = r'C:\Users\DHattiyavar\OneDrive - Prolifics Corporation Ltd.,\Desktop\CV\Automated-Resume-Screening-System-master\Original_Resumes\RajeshNandina.pdf'
file = st.file_uploader("Choose a resume for parsing")
file_data = parser.from_file(file)
text = file_data['content']
st.header('The Input Resume is:')
st.write(text)


#file_data = parser.from_file(file)
#text = file_data['content']
#st.title("Resume Fields Extractor")
#st.header('The Input Resume is:')
#st.write(text)

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
    sub_patterns = ['Role\W+[A-z]* [A-z]*','Role Played[\n]+[^\r\n]+','[A-Z][a-z]* Developer','[A-Z][a-z]* lead','[A-Z][a-z]* Engineer','[A-Z][a-z]* leader']
    pattern = '({})'.format('|'.join(sub_patterns))
    role = re.findall(pattern, text)
    return role
role = get_role(text)
extracted_text["ROLE"] = role

def get_client(sentences):
    sub_patterns = ['Client\t+:  [A-z]* [A-z]*','Client\t+:  [A-Z]* [A-z]*','\t+[A-z]* [a-z]* Client','Client : [A-Z][a-z].*','Client\W+[A-Z][a-z]* [a-z]* [a-z]* [A-Z]* [A-Z][a-z]*','Client \n+:.*','Client\t+:\t.*','Client\W+ [A-z][a-z]* [A-z][a-z]*','Client    : [\n]+[^\r\n]+','Client [B\] [A-Z][a-z] [A-Z][a-z]* [A-Z][a-z]* ','Client [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*','Client [A-Z][a-z]*','CLIENT [A-Z][a-z]*','CLIENT [B\][a-zA-Z._/ ]*','CLIENT [B\][a-zA-Z._/ ][a-zA-Z._/ ]*', '[A-Z][a-z]* [A-Z][a-z]* Group, Inc.','Client [B\][A-Z._/ ]* ,* [A-Z][a-z]*','[B\][A-Z._/ ]* BANK']
    pattern = '({})'.format('|'.join(sub_patterns))
    client = re.findall(pattern, text)
    return client
client = get_client(text)
extracted_text["CLIENT"] = client
    #Client.append(client)
# client
#new_clients = []
#for i in client:
    #new_clients.append(i.split('Client ')[1])
#extracted_text["Client"] = new_clients
#Extract Organizations

sub_patterns = ['[A-Z][a-z]* [A-Z][a-z]* pvt ltd','[A-Z][a-z]* [A-Z][a-z]* Infotech','.*Pvt.Ltd','[A-Z]* [A-Z]* Limited','[A-Z][a-z]* technologies Ltd','[A-Z._/ ]* PVT LTD','[A-Z][a-z]* [A-Z][a-z]* solutions','[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* Pvt Ltd','[A-Z]* [A-Z][a-z]* Pvt Ltd','[A-Z][a-z]* [A-Z][a-z]* Private Limited','[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* Lab','[A-Z][a-z]* [A-Z][a-z]* Private Limited','[A-Z][a-z]* Limited', '[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* Pvt Ltd ','[A-Z][a-z]* [A-Z][a-z]* Inc.','[A-Z][a-z]* [A-Z][a-z]* Services',' [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* Services', '[A-Z][a-z]* Ltd','[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* Services',' [A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]* Limited','[A-Z]* [A-Z][a-z]* Pvt. Ltd.'
                ]
pattern = '({})'.format('|'.join(sub_patterns))
Exp = re.findall(pattern, text)
extracted_text["Organization"] = Exp


sub_patterns = ['Time Period[\n]+[^\r\n]+','Previous \W+[A-z]* [0-9]* \W+[A-z]* [0-9]*\W+','Current \W+[A-Z-a-z]* [0-9]*\W+[A-Z-a-z]*\W+','Duration: .*','Duration[\n]+[^\r\n]+','DURATION: .*','Duration\t+:.*','Duration\W+.*','from [ a-zA-Z0-9]* now','[A-Z][a-z]* [0-9]* to till date']
pattern = '({})'.format('|'.join(sub_patterns))
duration = re.findall(pattern, text)
extracted_text["DURATION"] = duration


#df = pd.DataFrame(zip(email, Exp, client, role, duration), columns=['email', 'EXp', 'client', 'role', 'duration'])
#st.write(df)

st.write(extracted_text)

