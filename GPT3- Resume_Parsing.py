#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install openai')


# In[8]:


import pandas as pd
import openai
import numpy as np
import pickle

COMPLETIONS_MODEL = "code-davinci-002"


# In[9]:


# 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


# In[10]:


openai.api_key = "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"


# In[69]:


context = """
Rakesh

Summary:

· Have 4 years of IT Experience with 3.4 years of experience in Dell Boomi.

· Certified Dell Boomi Professional Developer, API Design & Management, Production Administrator.

· Designed and developed integrations through Dell Boomi for Salesforce, MySQL Workbench, Filezilla, Web Services like SOAP and REST.

· Worked on different Dell Boomi connectors like Disk, FTP, Mail, Salesforce, Database, Webservices SOAP Client, HTTP Client, Webservices Server (Listener), Atom Queue.

· Successfully completed Full life cycle implementation and integration on Webservices using Dell Boomi.

· End to End project life cycle experience: System Documentation, Requirement gathering, Realization, Process mapping, Testing, Debugging, Interface Management, Post Implementation Support and Trouble shooting.

· Worked for different formats like XML, CSV, Database and JSON.

· Successfully designed and delivered Dell Boomi integrations.

· Able to write custom script using Java/Groovy Script.

· Good understanding on Webservices, worked with Queue management.

· Experience on complete SDLC for Dell Boomi Projects.

· Able to design, develop and deploy the project using Dell Boomi.

· Experience in reviewing functional specifications and providing business solutions for various requirements.

· Experience with Designing and implementing error handling and reporting.

· Experience developing using SOA integration methodologies and protocols: APIs, REST, SOAP, XML, JSON, Publish-Subscribe, messaging.

· Experience working with and manipulating XML/JSON, and flat file documents using JavaScript and/or Groovy.

· Knowledge in building different map functions using standard functions and custom function using JavaScript and Groovy.

· Expertise in agile based development and integration of services and components.

· Managing team day to day activities (daily status updates, preparing minutes of meetings, etc.).

Technical Skills:

Integration / Middleware Tool: Dell Boomi

Applications: MySQL Workbench, FileZilla Client, Salesforce

Scripts: JavaScript, Groovy

Data Formats: XML, CSV, Database, Json

Connectors: Disk, FTP, Mail, Salesforce, Database, Web Services, SOAP Client, HTTP Client, Web Services Server

Project Experience:

Project 1

Client: Cargill

Role: Integration Developer

Duration: June 2019 – Feb 2020

Description:

This project is to align all the Sales Order entries of Brazil to Global Process for specific needs of Global Model of Food Industry and to interface all the available Clients from Salesforce to MySQL Workbench according to the requirement.

Technologies: Dell Boomi, Salesforce, MySQL Workbench

Responsibilities:

· End to end development of interfaces and provide Unit Integration Testing (UIT), User Acceptance Testing (UAT) and Go Live support.
Project 2

Client: Specsavers

Role: Integration Developer

Duration: Nov 2018 – June 2019

Description:

This project is to update the Database of the client on monthly basis with the last month transaction information.

Pulling the records from Salesforce from Account Object based on the Created Date and last Updated Date and send it to FTP on Scheduled Basis. From FTP, Business Team will route this data to their End System.

Technologies: Dell Boomi, Salesforce, FTP, Mail

Responsibilities:

· Integration between Salesforce and FTP.

· Responsible for development of entire use case (end to end).

· Involved in developing JavaScript, Processes, Maps and Connectors, etc.

· Co-ordination with the onsite team to gather the accurate requirement.

· Conducted the unit and system testing for Processes, Maps and Connectors.

· Responsible for preparing technical design document.

· Understanding the Agile development techniques.

· Learn, suggest and implement new technologies/techniques.

Project 3

Client: Jabill

Role: Integration Developer

Duration: Jan 2018 – Nov 2018

Description:

Client Salesforce was integrated with MySQL database, client wanted to sync its salesforce system with its MySQL database.

Objects in salesforce like Accounts, Contract, Opp, Leads Data were sync with the Database.

Technologies: Dell Boomi, Salesforce, MySQL, Mail

Responsibilities:

· Attending client meetings to understand the business requirement.

· Design the architecture of the Integrations.

· Preparing the mapping sheets by collaborating with different teams.

· Involved in requirement gathering for Profiles, Maps and Process level designing.

· Worked on Salesforce, database FTP and Disk connectors.

· Integrated Salesforce with database.

· Involved in Development for Various XML, JSON, and Flat file profiles.

· Developing Various Maps based on their requirement using JavaScript.

· Executed the test cases as per schedule, reported bugs updating the status.

· Deployment and scheduling the Batch Process as per client Requirement.

Project 4

Client: Ariba, Inc.

Project: Dell Boomi interfacing with Salesforce
Role: Dell Boomi Integration Developer

Duration: Feb 2017 – Oct 2017

Description:

It is basically Accounts & Opportunity update on Salesforce & Database.

This gets the data from accounts object sending the data to database and updating the status.

Technologies: Dell Boomi

Responsibilities:

· Requirements gathering with the help of on-site co-ordination team.

· Responsible for implementing end to end application.

· Involved in unit testing process.

· Responsible for debugging the errors and warnings.

Project 5

Client: Ariba, Inc.

Project: Dell Boomi interfacing with Salesforce

Role: Dell Boomi integration Support Engineer

Duration: July 2016 – Jan 2017

Description:

Data is fetched from Salesforce.

Involved as a support engineer for this project as the development was done.

Technologies: Dell Boomi

Responsibilities:

· Analyzing of complicated business rules and exception handling problems.

· Support integration processes and maintenance.

Qualifications:

Certifications:

· Integration: Associate Developer, Professional Developer

· API Management: Professional API Design, Professional API Management

· Administrator: Production Administrator

Education:

· B. Tech in Computer Science Engineering with an aggregate of 70% from JNT University, Kakinada, India – 2015

"""

questions = "Client names?"

prompt =  context + "\nQ: " + question + "\n" + "A: "


# In[70]:


print(prompt)


# In[71]:


Client_names=openai.Completion.create(
    prompt=prompt,
    temperature=0,
    max_tokens=80,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    model=COMPLETIONS_MODEL
)["choices"][0]["text"].strip(" \n")


# In[72]:


Client_names.split('\n')[0]


# In[84]:


openai_prompt = context
openai_prompt += '''

Answer the following questions:

1 - Client names?

2 - Roles?

3 - Durations?

Answers: 
'''


# In[85]:


openai_prompt 


# In[101]:


Client_names = openai.Completion.create(
    prompt=openai_prompt,
    temperature=0,
    max_tokens=80,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    model=COMPLETIONS_MODEL
)["choices"][0]["text"].strip(" \n")


# In[102]:


Client_names.split('\n\n')


# In[112]:


Client_names.split('\n')[0]


# In[110]:


Client_names.split('\n')[2]


# In[108]:


Client_names.split('\n')[4]


# In[ ]:




