from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal
import re
import json
import streamlit as st

st.title('Information Extraction from PDF Table using Regex')
st.header('Upload your Document:')
document = st.file_uploader("Upload the Document")

#document = open('567020-DELIVERY ORDER.pdf', 'rb')
#document = open('doc1 .pdf', 'rb')
#button = st.button("Get the Information")
#Create resource manager

rsrcmgr = PDFResourceManager()
# Set parameters for analysis.
laparams = LAParams()
mylist =[]
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
for page in PDFPage.get_pages(document):
    interpreter.process_page(page)
    # receive the LTPage object for the page.
    layout = device.get_result()
    x0 = y0 = x1 = y1 = 0
    tableColumns = []
    for element in layout:
        if isinstance(element, LTTextBoxHorizontal):
            #print(x0, y0, x1, y1)
            if(y0==element.bbox[1] and y1==element.bbox[3]):
                if(len(tableColumns)==0):
                    tableColumns.append(x0)
                tableColumns.append(element.bbox[0])

            elif(x0 not in tableColumns):
                if(len(tableColumns)!=0):
                    tableColumns.clear()
                #print('>>>>',element.bbox[0], element.bbox[1])
                #print('->',element.get_text()) 
                mylist.append(element.get_text())
            #x0,y0,x1,y1=element.bbox     
result_1 = [item.split('\n') for item in mylist]


jsonString = json.dumps(result_1)
res = [','.join(ele) for ele in result_1]
result_1 = [item.split(',') for item in res]
def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1
 
 
# Driver code
#s = ['Geeks', 'for', 'Geeks']
res1 =listToString(res)


reg= r'TRUCKER,[A-Z]*'

TRUCKER = re.findall(reg, res1)
TRUCKER = TRUCKER [0].split(',')


reg= r'HBL No.,[A-Z-0-9]*'

HBL_No = re.findall(reg, res1)
HBLNo = HBL_No[0].split(',')

reg= r'MBL No.,[A-Z-0-9]*'

MBL_No = re.findall(reg, res1)
MBLNo = MBL_No[0].split(',')



reg= r'AMS BL No.,[A-Z-0-9]*'

AMSBL_No = re.findall(reg, res1)
AMSBL_No = AMSBL_No[0].split(',')

reg= r'OUR REF. No.,[A-Z-0-9]*'

OURREF_No = re.findall(reg, res1)
OURREF_No = OURREF_No[0].split(',')


reg= r'REFERENCE No. :,[A-Z]*-[A-Z-0-9]*'

REF_No = re.findall(reg, res1)
REF_No= REF_No[0].split(',')



reg= r'COMMODITY,[A-Z]* [A-Z]* [A-Z]*'

COMMODITY = re.findall(reg, res1)
COMMODITY = COMMODITY[0].split(',')

reg= r'CARRIER,[A-Z]*[A-Z]* [A-Z]* [A-Z]* [A-Z]*., [LTD]*'

CARRIER = re.findall(reg, res1)
CARRIER = CARRIER[0].split(',')



reg= r'PORT OF LOADING,[A-Z]*, [A-Z]*'

RECEIPT_PORT_OF_LOADING = re.findall(reg, res1)
RECEIPT_PORT_OF_LOADING = RECEIPT_PORT_OF_LOADING[0].split(',')


reg= r'PORT OF DISCHARGE,[A-Z]* [A-Z]*, [A-Z]*'

PORT_OF_DISCHARGE = re.findall(reg, res1)
PORT_OF_DISCHARGE  = PORT_OF_DISCHARGE [0].split(',')


reg = r'DELIVERY,\w+. [A-Z]* [A-Z]* [A-Z]* [A-Z]*,[0-9]* [A-Z]* [A-Z]* [A-Z]*,[A-Z]*,[A-Z]* [A-Z]* [0-9]*,[A-Z]* : [A-Z]*\w+.[A-Z]*.[0-9]*,[A-Z]* : [0-9]*-[0-9]*-[0-9]*'
DELIVERY = re.findall(reg, res1)
DELIVERY_Address = DELIVERY [0].split(',')
DELIVERY_Address



reg = r'PICKUP,[A-Z]* [A-Z]*-[A-Z]* [0-9]*\W+[A-Z0-9]*\W+[A-Z]* [A-Z]*,[A-Z]*, [A-Z]* [0-9]*'
PICKUP = re.findall(reg,res1)
PICKUP = PICKUP [0].split(',')


reg = r'BILL TO,[A-Z]* [A-Z]* [A-Z]*. [A-Z]* [A-Z]*,[0-9]* [A-Z]* [A-Z]*. [A-Z]* # [0-9]*,[A-Z]* [A-Z]*, [A-Z]* [0-9]*'
BILL_TO = re.findall(reg,res1)
BILL_TO = BILL_TO  [0].split(',')


newlist = [TRUCKER,HBLNo,MBLNo,AMSBL_No,OURREF_No,REF_No,COMMODITY,CARRIER,RECEIPT_PORT_OF_LOADING,PORT_OF_DISCHARGE,BILL_TO,PICKUP,DELIVERY_Address]
st.header('The Extracted Information is:')

import pandas as pd
df = pd.DataFrame(newlist, columns = ['Atributes','value1','value2','value3','value4','value5','value6'])
df