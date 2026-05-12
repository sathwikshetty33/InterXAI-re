from pydantic import BaseModel, Field

# Resume Evaluator


class ResumeEvaluatorRequest(BaseModel):
    resume_text: str = Field(description="The full text of the candidate's resume")
    job_title: str = Field(description="The title of the job applied for")
    job_description: str = Field(description="The description of the job")
    experience: str = Field(description="The required years of experience")


class ResumeEvaluatorResponse(BaseModel):
    extracted_standardized_resume: str = Field(
        description="The standardized resume extracted from the resume text"
    )
    score: float = Field(
        description="The score of the extracted resume based on the job description"
    )
    shortlisting_decision: bool = Field(
        description="Decision on whether to shortlist the candidate based on the extracted resume"
    )
    feedback: str = Field(description="Feedback on the extracted resume")


# Answer Evaluator


class EvaluationRequest(BaseModel):
    position: str = Field(description="The job position being interviewed for")
    experience: str = Field(description="The required experience level")
    conversation_context: str = Field(description="The full conversation history so far")
    question: str = Field(
        description="The main question asked to the candidate; subsequent questions in the "
        "conversation history are follow-ups"
    )
    expected_answer: str = Field(description="The expected answer for the question")


class EvaluationResponse(BaseModel):
    score: float = Field(description="Score from 1.0 to 10.0")
    feedback: str = Field(description="Constructive feedback on the answer")
    reasoning: str = Field(description="Reasoning behind the assigned score")


# Follow-Up Decider


class FollowUpDeciderRequest(BaseModel):
    position: str = Field(description="The job position being interviewed for")
    experience: str = Field(description="The required experience level")
    conversation_context: str = Field(description="The full conversation history so far")
    expected_answer: str = Field(description="The expected answer for the question")


class FollowUpDeciderResponse(BaseModel):
    needs_followup: bool = Field(description="Whether a follow-up question is needed")
    followup_question: str | None = Field(
        default=None, description="The follow-up question to ask, if any"
    )


# Final Evaluator


class FinalEvaluationRequest(BaseModel):
    position: str = Field(description="The job position being interviewed for")
    experience: str = Field(description="The required experience level")
    interview_history: str = Field(
        description="JSON-serialized interview history with scores and feedback per question"
    )


class FinalEvaluationResponse(BaseModel):
    overall_score: float = Field(description="Overall score from 1.0 to 10.0")
    overall_feedback: str = Field(description="Critical assessment of the full interview")
    strengths: str = Field(description="Summary of key strengths observed")
    recommendation: str = Field(description="HIRE, REJECT, or FURTHER_EVALUATION")


# Resume Question Generator


class ResumeQuestionRequest(BaseModel):
    extracted_standardized_resume: str = Field(
        description="The standardized resume extracted from the resume text"
    )
    job_title: str = Field(description="The job title for the position")
    job_description: str = Field(description="The job description for the position")
    experience: str = Field(description="The required years of experience")


class ResumeQuestionResponse(BaseModel):
    extracted_q_and_a: list[str] = Field(
        description="List containing alternating questions and answers [Q1, A1, Q2, A2]"
    )
