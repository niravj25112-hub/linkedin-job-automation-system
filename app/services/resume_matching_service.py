class ResumeMatchingService:
    def calculate_match_score(self, job_description: str, resume_text: str) -> float:
        if not job_description or not resume_text:
            return 0.0
        job_terms = set(job_description.lower().split())
        resume_terms = set(resume_text.lower().split())
        if not job_terms:
            return 0.0
        return round(len(job_terms & resume_terms) / len(job_terms), 4)

