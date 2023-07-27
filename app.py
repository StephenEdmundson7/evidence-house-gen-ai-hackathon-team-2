""" Build an app """

# imports and set up
import streamlit as st
import os
import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SequentialChain
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = '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' #os.environ['OPENAI_API_KEY']

# gpt functions
def get_completion(prompt, model="gpt-3.5-turbo"):
    openai.api_key = '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' #os.environ['OPENAI_API_KEY']
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.9,
    )
    return response.choices[0].message["content"]


def create_applicants(text):
      first_prompt= f"""Give us three examples of applications suitable to the above job description and give specific examples where each applicant has demonstrated Civil service behaviours based on the file here:https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/717275/CS_Behaviours_2018.pdf  \
    that could be suitable for the text that is delimited by triple backticks .\
    Include specific examples where candidate has demonstrated the civil service behavior in a previous role , relevent skills , years of experience,
    qualification.

    Please do not use names but refer to them as applicant 1,2,..

    text:```{text}```

    Format the output as JSON with the following keys:
    applicant
    """
    applicants_response = get_completion(first_prompt)
    return applicants_response

def get_summary(text):
    second_prompt= f"""write a summary of each applicant with categories:
        skills, years of experience.  \
        and rank the applicants and give a one short summary reasoning of the ranking.

        text:```{text}```

        Format the output as JSON with the following keys:
        skills
        years of experinece
        ranking
        reasoning of ranking
        """
    applicants_response = get_completion(second_prompt)
    return applicants_response


def get_skills(skills_lists):
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

""" Build app """

def process_text(text):
    # This function takes in text as an argument and returns some other text
    # You can modify this function to do whatever you want with the input text
    return text.upper()

st.title('Recruitment co-pilot')

# Create a text area for the user to paste text
input_text = st.text_area('Insert job description here')

# Create a button
if st.button('Generate applicants'):
    # When the button is clicked, call the process_text function with the input text
    applicants = create_applicants(input_text)
    summary = get_summary(applicants)
    # output_text = process_text(input_text)

    # Display the output text on the second screen
    st.write(summary)