import serpapi
from config import config

def get_academic_info(prof_name, university, N):
    # Prepare search keywords
    keywords = f"{prof_name} {university}"

    # Set up SerpAPI search parameters
    params = {
        "api_key": config.SERP_API_KEY,  # API key from config
        "engine": "google_scholar",  # Use Google Scholar engine
        "q": keywords,  # Query using professor name and university
        "hl": "en"  # Set language to English
    }

    # Execute search and retrieve results
    search = serpapi.search(params)
    result = search.as_dict()

    # Get the top N organic results
    organic_results = result.get('organic_results', [])[:N]

    # Combine results into a formatted string
    combined_results = ""
    for organic_result in organic_results:
        title = organic_result.get('title', 'No title')
        snippet = organic_result.get('snippet', 'No snippet')
        publication_info = organic_result.get('publication_info', {}).get('summary', 'No publication info')
        combined_results += f"Title: {title}\nSnippet: {snippet}\nPublication Summary: {publication_info}\n\n"

    return combined_results
