""" Build an app """

# imports and set up
import streamlit as st
import os
import ast
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SequentialChain
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = "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"
openai.organisation = "org-AEPp1joUbsaKuRIqN0X9eUaI"

# gpt functions
def get_completion(prompt, temperature, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


def create_applicants(text):
    first_prompt= f"""Give us three examples of applications for the job description in {text}. List their current job role and previous job roles and experience. Include their level of education. Make sure it includes the applicant's top 3 most relevant technical skills, the applicant's number of years of experience and their relevant qualifications. Include specific examples where candidate has demonstrated the ability to deliver at pace, leadership, communication and managing services in a previous role.

    Please do not use names but refer to them as applicant 1,2,..
    """
    applicants_response = get_completion(first_prompt, temperature=0.9)
    return applicants_response

def get_skills_summary(text):
    second_prompt = f"""For the applicants data in {text} please provide extract all the relevant technical skills shown by the applicants, how many applicants show each skill and the average proficiency score across all applicants of either 1 (basic), 2 (intermediate) or 3 (advanced). Please provide the answer in json format e.g. {{"skill": ["skill 1", "skill 2"], "number_of_candidates_with_skill": [1, 3], "average_proficiency_score": [3, 1]}}"""
    # second_prompt = f"""Imagine you are a recruiter. Return a json file with the following keys for the applicant data in {text}. 1) Key skills: the relevant skills shown by the candidate with an associated proficiency score of either 1 (basic), 2 (intermediate) or 3 (advanced). Each item in the json is a different skill"""
    # second_prompt= f"""Imagine you are a recruiter. Categorise each candidate with their relevant skills, level of education and years of experience. Rank the applicants and give a one short summary reasoning of the ranking. Format the output as a python dictionary without any line breaks with the following keys: skills (Please list the relevant skills demonstrated by each applicant and give them a proficiency level from 1 (basic), 2 (intermediate) or 3 (advanced)), years of work experience (integer of how many years an applicant has been working for), highest level of education (e.g. Bachelors degree, masters degree or PhD), ranking (reasoning of ranking).
        
        # applicant data:```{text}```
        # """
    skills_summary = get_completion(second_prompt, temperature=0)
    return skills_summary


def get_experience_summary(text):
    third_prompt = f"""For the applicants data in {text} please extract the number of years experience for each applicant as a list of integers i.e. in the format [integer_years_1, integer_years_2, integer_years_3]"""
    experience_summary = get_completion(third_prompt, temperature=0)
    return experience_summary

def get_skills(summary):
    skills_lists = [x["skills"].split(",") for x in summary]
    skills = [s for sublist in skills_lists for s in sublist]
    skills_counts = pd.Series(skills).value_counts().reset_index()
    skills_counts.columns = ["skill", "n_candidates"]
    return skills_counts


def get_experience(experience_list):
    data = pd.Series(experience_list, name="experience")
    fig = plt.hist(data)
    plt.title('Applicant experience')
    plt.xlabel("Years")
    return fig

# define app
st.title('Recruitment co-pilot')

# Create a text area for the user to paste text
input_text = st.text_area('Insert job description here')

# Create a button
if st.button('Generate applicants'):
    # When the button is clicked, call the process_text function with the input text
    applicants = create_applicants(input_text)
    skills_summary = get_skills_summary(applicants)
    skills_summary = pd.DataFrame(ast.literal_eval(skills_summary)).sort_values(by="number_of_candidates_with_skill", ascending=False).reset_index()
    fig = px.bar(skills_summary, x="number_of_candidates_with_skill", y="skill", title="Candidate skills")  
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    
    st.write(applicants)
    st.dataframe(skills_summary)
    fig
    
    experience = get_experience_summary(applicants)
    experience = pd.DataFrame({"number_of_years_experience": ast.literal_eval(experience)}).reset_index()
    experience = experience["number_of_years_experience"].value_counts().reset_index()
    fig2 = px.bar(experience, x="number_of_years_experience", y="count", title="Candidate experience level")
    fig2.update_xaxes(showgrid=False)
    fig2.update_yaxes(showgrid=False)
    fig2