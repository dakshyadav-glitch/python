import requests
from logger import logger

API_URL = "https://jsonplaceholder.typicode.com/users"

def extract_users():
    try:
        response = requests.get(API_URL, timeout=20)
        response.raise_for_status()
        logger.info("Successfully extracted data from API")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"API extraction failed: {e}")
        return []
