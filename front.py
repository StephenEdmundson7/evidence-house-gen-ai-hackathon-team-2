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
from cachetools import cached

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = "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"
#openai.organisation = "org-AEPp1joUbsaKuRIqN0X9eUaI"


# gpt functions
# @cached(cache={})
def get_completion(prompt, temperature, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


def create_applicants(text):
    first_prompt = f"""Give us 10 examples of applications for the job description in {text}. \
        For each applicant write a response in the folowin format:
        current job role 

        previous job roles. In each role give a short description of the experience in the role. 

        level of (undergarduate, master, PhD)

        number of years of experience of each applicant \

        Include specific examples where candidate have demonstrated the ability to deliver at pace, leadership, communication and managing services in a previous role.

        Please do not use names but refer to them as applicant 1,2,..
        """
    applicants_response = get_completion(first_prompt, temperature=0.9)
    return applicants_response


def get_skills_summary(text):
    second_prompt = f"""For the applicants data in {text} \
        please extract all the relevant technical skills shown by the applicants, how many applicants show each skill and the average proficiency score across all applicants of either 1 (basic), 2 (intermediate) or 3 (advanced). \
        Please provide the answer in json format e.g. {{"skill": ["skill 1", "skill 2"], "number_of_candidates_with_skill": [1, 3], "average_proficiency_score": [3, 1]}}"""
    # second_prompt = f"""Imagine you are a recruiter. Return a json file with the following keys for the applicant data in {text}. 1) Key skills: the relevant skills shown by the candidate with an associated proficiency score of either 1 (basic), 2 (intermediate) or 3 (advanced). Each item in the json is a different skill"""
    # second_prompt= f"""Imagine you are a recruiter. Categorise each candidate with their relevant skills, level of education and years of experience. Rank the applicants and give a one short summary reasoning of the ranking. Format the output as a python dictionary without any line breaks with the following keys: skills (Please list the relevant skills demonstrated by each applicant and give them a proficiency level from 1 (basic), 2 (intermediate) or 3 (advanced)), years of work experience (integer of how many years an applicant has been working for), highest level of education (e.g. Bachelors degree, masters degree or PhD), ranking (reasoning of ranking).

    # applicant data:```{text}```
    # """
    skills_summary = get_completion(second_prompt, temperature=0.2)
    return skills_summary


def get_experience_summary(text):
    third_prompt = f"""For the applicants data in {text} \
        please extract the number of years experience for each applicant as a list of integers i.e. in the json format \
        {{"number_of_years_experience": [integer_years_applicant1, integer_years_applicant2, integer_years_applicant3]}}"""
    experience_summary = get_completion(third_prompt, temperature=0.2)
    return experience_summary


# build the app itself
st.title('Recruitment co-pilot')

# Create a text area for the user to paste text
input_text = st.text_area('Insert job description here')

# Create a button
# When the button is pressed, run certain actions
if st.button('Generate applicants'):
    # get synthetic applicant data
    applicants = create_applicants(input_text)

    # get a summary of the applicants skills and plot
    skills_summary = get_skills_summary(applicants)
    skills_summary = pd.DataFrame(ast.literal_eval(skills_summary)).sort_values(by="number_of_candidates_with_skill",
                                                                                ascending=False).reset_index()
    fig = px.bar(skills_summary, x="number_of_candidates_with_skill", y="skill", title="Candidate skills")
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    # get a summary of the applicants' level of experiece and create a plot
    experience_summary = get_experience_summary(applicants)
    experience =  pd.DataFrame(ast.literal_eval(experience_summary))
    experience = experience["number_of_years_experience"].value_counts().reset_index()
    fig2 = px.bar(experience, x="number_of_years_experience", y="count", range_x=[0,20],title="Candidate experience level")
    fig2.update_xaxes(showgrid=False)
    fig2.update_yaxes(showgrid=False)

    # render the outputs in streamlit
    with st.expander("Click to see example applicants",expanded=False):
        st.write(applicants)
    fig
    fig2