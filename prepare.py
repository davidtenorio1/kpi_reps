# Set up environment
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re


reps = pd.read_excel('2020 project english.xlsx')
reps.head()

def rename_columns(df):

    df = df.rename(columns={"Report Period": "reporting_period", 
                            "Group Name": "group_name", 
                            "Agent Name": "agent_name",
                            "Attuid": "attuid",
                            "Percent Calls Noted": "percent_calls_noted",
                            "Convenience Fee Waivers": "convenience_fee_waivers",
                            "Scheduled Open Hours": "scheduled_open_hours",
                            "Schedule Adherence": "schedule_adherence",
                            "Availability": "availability",
                            "Total Vs Total - eTRACS": "total_vs_total_etracs",
                            "Immediate Vs Total - eTRACS": "immediate_vs_total_etracs",
                            "Transfers": "transfers",
                            "Inbound AHT - ENG": "inbound_aht_eng",
                            "Calls Answered - ENG": "calls_answered_eng",
                            "Calls Answered - SPA": "calls_answered_spanish",
                            "Inbound AHT - SPA": "inbound_aht_spanish",
                            "Inbound AHT": "inbound_aht",
                            "Call Tracker Compliance": "call_tracker_compliance",
                            "PCF Work Review": "pcf_work_review",
                            "Cust Exp - Call Observations": "customer_experience_call_observations",
                            "Cust Exp - Net Rep Sat": "customer_experience_net_rep_sat",
                            "Conformance": "conformance"             
                            })


    return df


def remove_columns(df):
    df = df.drop(columns={'reporting_period', 'group_name','agent_name'})
    return df

def open_hours(df):
    # remove minutes and seconds from open hours column and convert to 
    df['scheduled_open_hours'] = [re.sub(r':.+','', str(i)) for i in df['scheduled_open_hours']]
    return df
