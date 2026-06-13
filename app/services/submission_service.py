class SubmissionService:
    def normalize_status(self, status: str) -> str:
        return status.strip().lower().replace(" ", "_")

