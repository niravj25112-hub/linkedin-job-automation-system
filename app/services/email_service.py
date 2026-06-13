class EmailService:
    def generate_recruiter_email(
        self, candidate_name: str, job_title: str, company: str | None
    ) -> tuple[str, str]:
        company_text = company or "your client"
        subject = f"{candidate_name} for {job_title}"
        body = (
            f"Hello,\n\n"
            f"I hope you are doing well. I am sharing {candidate_name} for the "
            f"{job_title} opportunity with {company_text}.\n\n"
            "Please let me know if this profile is a fit.\n\n"
            "Best regards"
        )
        return subject, body

    def send_via_gmail(self, recipient_email: str, subject: str, body: str) -> str:
        # Gmail API integration will be implemented here.
        return f"queued:{recipient_email}:{subject}:{len(body)}"

