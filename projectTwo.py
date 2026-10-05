from pydantic import BaseModel
from typing import List, Optional

class Education(BaseModel):
    degree:str
    institution:str
    graduation_year : Optional[int]

class ContactInfo(BaseModel):
    phno:int
    work_email:str
    personal_email: Optional[str]

class WorkExperience(BaseModel):
    job_titles:str
    job_exp_years:Optional[int]
    job_location:str

class Skills(BaseModel):
    hardskills:list[str]
    softskills:list[str]

class CandidateResume(BaseModel):
    fullname:str
    education:list[Education]
    contactInfo:list[ContactInfo]
    work_exp:list[WorkExperience]
    primary_skills:list[Skills]


resume_object = CandidateResume(
    fullname="Alex Mercer",
    education=[
        Education(
            degree="Bachelor of Science in Computer Science",
            institution="State University",
            graduation_year=2022
        ),
        Education(
            degree="Data Science Certificate",
            institution="Tech Academy",
            graduation_year=2023
        )
    ],
    contactInfo=[
        ContactInfo(
            phno=15550199,
            work_email="alex.mercer@techcorp.com",
            personal_email="alex.mercer.dev@email.com"
        )
    ],
    work_exp=[
        WorkExperience(
            job_titles="Software Engineer II",
            job_exp_years=3,
            job_location="San Francisco, CA"
        ),
        WorkExperience(
            job_titles="Junior Web Developer",
            job_exp_years=1,
            job_location="Remote"
        )
    ],
    primary_skills=[
        Skills(
            hardskills=["Python", "SQL", "Pydantic", "Docker"],
            softskills=["Problem Solving", "Team Collaboration"]
        )
    ]
)

print(resume_object.model_dump_json(indent=2))


