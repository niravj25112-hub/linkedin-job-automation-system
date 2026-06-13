from app.core.config import settings


class JobSearchService:
    def get_keyword_filters(self) -> list[str]:
        return settings.keyword_filters

    def search_recent_jobs(self) -> list[dict[str, str]]:
        # LinkedIn/search-provider integration will be implemented here.
        return []

