import streamlit as st

import pandas as pd
import openai
import numpy as np
import pickle

COMPLETIONS_MODEL = "code-davinci-002"
openai.api_key = "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"


st.title('The Input Resume is:')
context = """
Rathnakar Reddy Kasireddy Email: rathnakarreddykasireddy@gmail.com Mobile : 9949490015

Profile Summary

v Around 10 years of work experience in analysis, design, and development of various Integration Projects using Dell Boomi, SAP PI/PO, APIGEE, and WSO2.

v Expertise in requirement analysis, estimations, development, testing, reviews, leading the team, work assignments and tracking the status of the team members.

v Working experience in both development & maintenance support projects.

v Expertise in API management tools APIGEE and WSO2. Published APIs to external consumers by applying various security mechanisms.

v Expertise in dell Boomi platform setup, installed atom and molecules in both on premise and Azure platform.

v Created ARM templates with scripts in Azure to create azure resources and install dell boomi molecule in automated way to ramp up and ramp down molecule nodes using Azure Devops.

v Installed syslog agent and Wakaru in Boomi for log management and Boomi server metrics monitoring.

v Worked on Java upgrades and monthly atom sphere upgrades.

v Worked on various molecule cluster issues and supported platform side activities.

v Worked on Connectors like HTTP Client, Web Service SOAP Client, JMS, Workday, Disk, Mail, FTP, SFTP, Data lake, Kafka, Database, Microsoft Azure Blob Storage and Atom Queue.

v Working experience in different data formats, such as XML, CSV and JSON.

v Expertise on creating Trading Partners configurations for various communication protocols like FTP, FTPS, SFTP, AS2 for B2B integration

v Worked on documentation for defining naming standards, guidelines based on organizations application architecture.

v Experience in AMS to support Boomi access related issues and user management activities.

v Worked on A2A and B2B scenarios in Dell Boomi and SAP PO.

v Certified Dell Boomi Admin and Professional Developer.

Work / Organizational Experience

v Currently working at Infosys Hyderabad as “Senior Consultant” from July 2016 to till date.

v Worked at Wipro as “Associate Consultant” from Jan 2015 to July 2016.

v Worked at SEAL INFOTECH as “Associate Consultant” from Sep-2010 to Jan-2015.

Onsite Experience

v Worked in Client location as Onsite Lead/Integration Consultant in Helsinki, Finland for 1 year for Dell Boomi platform setup, installed atom and molecules in on premise servers and Azure.

Academic Background

v Master of computer Applications from JBIET/JNTU in 2009.

Project #1

Client : Posti

Project : Dell Boomi platform setup and integration project

Tool : Dell Boomi

Duration : April 2019 to till now

Description:

Dell Boomi platform setup for on premise and Azure platform, supporting platform side activities. Integration project lead from onsite Finland.

Responsibilities:

· Worked as On-site lead for Dell Boomi integration from client location.

· Installed Molecule in on premise and Azure platforms. Supporting platform side activates like upgrades, fixing cluster issues, Access management, load testing, project reviews, and housekeeping activities.

· Created ARM templates in Azure to deploy Azure resources like VM, Network Interface, NSG, Disk etc. Incorporated scripts in ARM templates to install Boomi and post installation configurations.

· Installed syslog agent for log management and wakaru for server metrics (memory, disk space, threads, inodes, open files etc.) monitoring.

· Implemented logging and error handling mechanisms

· Requirement gathering, analysis and design of Integration flows.

· Defined naming standards, developer guidelines based on allocation architecture.

· Design steps of Production movement and support across the project after go-live

· Coordinated with multiple vendors from geographically distributed teams for a successful development, testing and deployment of project.

Project #2

Client : Procter & Gamble (P&G)

Tool : Dell Boomi

Duration : July 2016 to March 2019

Description:

Implementing ERP Integration project. This Project includes Order Management, Banking, and Payments integration between multiple systems.

Responsibilities:

· Requirement gathering, analysis and design of Integration flows. Coordinating with all level of management, Customers, account managers, onsite team, developers, vendors

· Implemented best error handling mechanisms and unit testing.

· Created TP setups for different communication protocols (FTP, SFTP, AS2).

· Participated in code and design reviews and included in performance tuning design approach across project.

· Design steps of Production movement and support across the project after go-live

· Coordinated with onshore/offshore team during the Built, UAT and Business Go-Lives.

· Created Proxies in APIGEE and CA APIM implementing policies based on information security needs to publish internal services to App developers.

Project #3

Client : Cairn India

Tool : SAP PI

Duration : Jan 2015 to Jun 2016

Description: Cairn India is an oil and gas exploration and production company, headquartered in Gurgaon, India. It is a subsidiary of Vedanta Resources. Cairn India is one of the largest independent oil and gas exploration and production companies in India.

Responsibilities:

· Developed interfaces to capture daily production values of all assets of cairn from DO data base and updated in SAP.

· Integrated SAP with Ariba using Ariba Network Adapter to send RFQ from SAP to Ariba and updating Quotation details in SAP.

· Scheduled the availability time planning for interfaces.

· Monitoring and quick troubleshoot for message backlog through RWB.

· Configured the SLD (System Landscape Directory) Objects as Technical System as well as Business System based on the Requirement.

· Configured the RFC destinations for establishing the connection between ECC and PI systems.

· Created Alert to generate E-mail if any error.

Project #4

Client : Jockey

Tool : SAP PI

Duration : Jun 2014 to Dec 2015

Description: Jockey International, Inc. is a manufacturer, distributor and retailer ofunderwear, sleepwear for men, women, and children.

Responsibilities:

· Developed outbound synchronous interfaces to capture customer, order and invoice details from E-Commerce, updating the same in SAP and sending back response to E-Commerce.

· Developed inbound synchronous interfaces to capture stock details from SAP, sending to E-Commerce, and updating response in SAP.

· Developed Data Types, Message Types, Interfaces.

· Developed and configured Interface Mappings and Message Mappings.

· Configured the adapters as per the client specifications.

· Designed the Receiver/Interface Determinations and Sender/Receiver Agreements.

· Configured the Alerts for each and every interface.

Project #5

Client : Dmart

Tool : SAP PI

Duration : Jan 2011 to May 2014

Description:

Avenue Super Marts Pvt Ltd owns and operates hypermarkets and supermarkets by the store name D-Mart. D-Mart seeks to provide a one-stop shopping experience for the entire family, meeting all their daily household needs.

Responsibilities:

· Developed interfaces for reading the bank acknowledgement for each payment and updating the SAP R/3 system with the corresponding UTR number and the payment status.

· Developed and implemented inbound interfaces to SAP R/3 which will send the store Sales & Payments data files from POS system by converting them into IDOCs in PI.

· Scheduled the availability time planning for sales inbound interfaces.

· Monitoring and quick troubleshoot for message backlog through RWB.

· Configured the SLD (System Landscape Directory) Objects like Technical System as well as Business System based on the Requirement.

· Configured the RFC destinations for establishing the connection between ECC and PI systems.

· Worked on disaster recovery activity

· Created Alert to gener
"""

st.write(context)




openai_prompt = context
openai_prompt += '''

Answer the following questions:
 - Email?

 - Client names?
 
 -Client industry?

 - Roles?

 - Durations?

Answers: 
'''


Client_names = openai.Completion.create(
    prompt=openai_prompt,
    temperature=0,
    max_tokens=200,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    model=COMPLETIONS_MODEL
)["choices"][0]["text"].strip(" \n")


st.title('The extracted information is:')
st.write(Client_names)