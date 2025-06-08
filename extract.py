import requests
import json
import os

API_URL = "https://jsonplaceholder.typicode.com/posts"
RAW_DATA_FILE = 'raw_posts.json'

print(f"--- Extract Stage ---")
print(f"Fetching data from API: {API_URL}")

try:
    response = requests.get(API_URL)
    response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
    api_data = response.json()

    with open(f"./jsonData/{RAW_DATA_FILE}", 'w') as f:
        json.dump(api_data, f, indent=4)

    print(f"Successfully extracted {len(api_data)} records to {RAW_DATA_FILE}")

except requests.exceptions.RequestException as e:
    print(f"Error during API extraction: {e}")
    exit(1)
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from API response. Response was: {response.text[:200]}...")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred during extraction: {e}")
    exit(1)