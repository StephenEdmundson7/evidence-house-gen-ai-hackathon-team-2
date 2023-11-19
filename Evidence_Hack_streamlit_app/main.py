import os
import openai
import pandas as pd
openai.api_key = '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' #os.environ['OPENAI_API_KEY']


def get_completion(prompt, model="gpt-3.5-turbo"):
    openai.api_key = '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'  # os.environ['OPENAI_API_KEY']
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.9,
    )
    return response.choices[0].message["content"]

x=get_completion("""
Read each of the following:

Data job family
https://www.gov.uk/guidance/data-analyst
https://www.gov.uk/guidance/data-architect
https://www.gov.uk/guidance/data-engineer
https://www.gov.uk/guidance/data-ethicist
https://www.gov.uk/guidance/data-governance-manager
https://www.gov.uk/guidance/data-scientist
https://www.gov.uk/guidance/performance-analyst

IT operations
https://www.gov.uk/guidance/application-operations-engineer
https://www.gov.uk/guidance/business-relationship-manager
https://www.gov.uk/guidance/change-and-release-manager
https://www.gov.uk/guidance/command-and-control-centre-manager
https://www.gov.uk/guidance/end-user-computing-engineer
https://www.gov.uk/guidance/incident-manager
https://www.gov.uk/guidance/infrastructure-operations-engineer
https://www.gov.uk/guidance/infrastructure-operations-engineer
https://www.gov.uk/guidance/it-service-manager
https://www.gov.uk/guidance/problem-manager
https://www.gov.uk/guidance/service-desk-manager
https://www.gov.uk/guidance/service-desk-manager
https://www.gov.uk/guidance/service-transition-manager

https://www.gov.uk/guidance/business-analyst--2
https://www.gov.uk/guidance/delivery-manager
https://www.gov.uk/guidance/product-manager
https://www.gov.uk/guidance/programme-delivery-manager
https://www.gov.uk/guidance/service-owner

https://www.gov.uk/guidance/quality-assurance-testing-qat-analyst
https://www.gov.uk/guidance/test-engineer
https://www.gov.uk/guidance/test-manager

https://www.gov.uk/guidance/development-operations-devops-engineer
https://www.gov.uk/guidance/enterprise-architect
https://www.gov.uk/guidance/frontend-developer
https://www.gov.uk/guidance/infrastructure-engineer
https://www.gov.uk/guidance/network-architect
https://www.gov.uk/guidance/security-architect
https://www.gov.uk/guidance/software-developer
https://www.gov.uk/guidance/specialist-infrastructure-engineer
https://www.gov.uk/guidance/technical-architect
https://www.gov.uk/guidance/technical-specialist-architect

https://www.gov.uk/guidance/accessibility-specialist
https://www.gov.uk/guidance/content-designer
https://www.gov.uk/guidance/content-strategist
https://www.gov.uk/guidance/graphic-designer
https://www.gov.uk/guidance/user-researcher


Generic

https://sfia-online.org/en/sfia-8/skills/benefits-management
https://sfia-online.org/en/sfia-8/skills/audit
https://sfia-online.org/en/sfia-8/skills/project-management
https://sfia-online.org/en/sfia-8/skills/research 
https://sfia-online.org/en/sfia-8/skills/strategic-planning
https://sfia-online.org/en/sfia-8/skills/workforce-planning
https://sfia-online.org/en/sfia-8/skills/scientific-modelling
https://sfia-online.org/en/sfia-8/skills/business-situation-analysis
https://sfia-online.org/en/sfia-8/skills/change-control
The part after https://www.gov.uk/guidance/ or https://sfia-online.org/en/sfia-8/skills/ is the job skill in question. 
https://sfia-online.org/en/sfia-8/skills/consultancy


Read each link to understand how each skill is classified and save the information in a table 
format with two columns: Skill, Requirements. Each row should have one skill and a list of requirements (comma-separated)

There might be some overlap so do make your own taxonomy. 



""")

print(x)

#x.to_csv("x.csv",sep="\t")
job_desc="""
Build and support a diverse team, providing leadership and management to the Customs Debt, Enforcement and Customs Law Teams including direct line management of 3 Grade 7s.  Provide high quality policy advice and briefing to Ministers, senior HM Treasury and HMRC stakeholders on the range of policy and enforcement responsibilities within the team.  
Work closely with HMRC Solicitors office, analysts, HMT Policy Partners, cross-Whitehall Enforcement Community and Operational colleagues as appropriate to develop and deliver appropriate handling strategies across the Teams responsibilities.   Lead the full range of customs debt policy, to ensure traders pay the right amount of import duty, including notification of the debt, voluntary disclosure, interest charged on overdue customs debt, liability and representation. 
Provide guidance and support to operational teams so they can carry out compliance activity and collect the right amount of duty owed within the correct timeframes, providing a level playing field for traders and encouraging compliance with debt collection policy.  Lead the full range of policy issues on the UKs customs powers and regulatory framework as set out by UK legislation, including powers to search, enquire, seize and detain and use of civil penalties; including any legislative amendments to those powers, and ensure we are monitoring data and performance to provide policy assurance.  
Deliver customs compliance and enforcement policy for non-fiscal prohibitions and restrictions (P&R); monitor across operations and improve performance at the border through use of data and intelligence; promote compliance with P&R controls through education and awareness; and respond to repeated non-compliance with robust and proportionate enforcement.  Contribute to the wider work and leadership of the Customs Audit and Law Division and to Customs & Borders Design as a senior leader.  As part of the leadership team, you will play a key role in building a culture that encourages diversity and values difference We are looking for an individual with excellent policy and analytical skills, who is able to develop comprehensive policy proposals across a range of complex, technical and inter-related international trade areas, analyse policy options and make recommendations.   Candidates should also be able to demonstrate strong stakeholder management skills, across a range of stakeholders, as well as visible and proactive team leadership through application of the Civil Service Leadership Statement.   Candidates would preferably, but not essentially, have policy experience in the Customs/International trade area.  If the candidate has no knowledge of customs they should be prepared to undertake relevant training.
"""



y=get_completion(f"""

With '{x}' in mind as the skill and the requirments of the skill in a table format
Apply a score 1 (low) to 10 (high) of how closely related the following advert in single quotes is to each of profession.  

Output a table of the different skills and the corresponding score as a table with the reason. The table will have three columns: skill, score, and reason.
The advert is as follows '{job_desc}'

After your scores. Output a sentance saying if the role requires any subject or topic specific knowledge. Some examples of topic or subject knowledge could be econometrics, geography or history. For any skills, list them as a bullet points

""")




print(y)


