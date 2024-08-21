from serpapi import GoogleSearch
from config import config

def get_academic_info(prof_name, university, N):
    keywords = f"{prof_name} {university}"
    params = {
        "api_key": config.SERP_API_KEY,
        "engine": "google_scholar",
        "q": keywords,
        "hl": "en"
    }
    result = GoogleSearch(params).get_dict()
    organic_results = result.get('organic_results', [])[:N]

    combined_results = ""

    for organic_result in organic_results:
        title = organic_result.get('title', 'No title')
        snippet = organic_result.get('snippet', 'No snippet')
        publication_info = organic_result.get('publication_info', {}).get('summary', 'No publication info')
        combined_results += f"Title: {title}\nSnippet: {snippet}\nPublication Summary: {publication_info}\n\n"

    return combined_results
