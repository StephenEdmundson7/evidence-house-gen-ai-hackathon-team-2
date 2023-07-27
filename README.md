# Recruitment co-pilot

An application that uses LLMs to assist in job description drafting and recruitment.

## Workflow

1. Draft a job description
2. Check the expected pool of applicants it will return and their skills / experience profile.
3. Adjust the job description and see how the expected applicant pool changes.

## How it works (for the hackathon)

* Prompt gpt3.5 to generate a synthetic pool of applicants from a job description
      - gpt3.5 is given examples of real applications to learn from
* Extract key information from the synthetic application using gpt3.5
      - experience level of candidates
      - highest level of education, etc  

## Future state

* Instead of using gpt for step 1, use a fine-tuned LLM on a real dataset of many 1,000s of real job description: application pairs.
