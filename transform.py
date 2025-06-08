import pandas as pd
import json
import os

RAW_DATA_FILE = 'raw_posts.json'
TRANSFORMED_DATA_FILE = 'transformed_posts.json'
INPUT_DIR = os.getenv('WORKSPACE', '.') # Jenkins workspace
OUTPUT_DIR = os.getenv('WORKSPACE', '.') # Jenkins workspace

# input_path = os.path.join(INPUT_DIR, RAW_DATA_FILE)
# output_path = os.path.join(OUTPUT_DIR, TRANSFORMED_DATA_FILE)

print(f"--- Transform Stage ---")
# print(f"Reading raw data from: {input_path}")

try:
    with open(f"./jsonData/{RAW_DATA_FILE}", 'r') as f:
        raw_data = json.load(f)

    df = pd.DataFrame(raw_data)

    # Example 1: Rename columns for clarity
    df.rename(columns={'userId': 'author_id', 'id': 'post_id'}, inplace=True)

    # Example 2: Create a new 'title_length' column
    df['title_length'] = df['title'].apply(lambda x: len(x) if isinstance(x, str) else 0)

    # Example 3: Select and reorder relevant columns
    df_transformed = df[['post_id', 'author_id', 'title', 'title_length', 'body']]
    print(f"Transformed data (first 5 rows):\n{df_transformed.head()}")

    # Convert DataFrame to a list of dictionaries (suitable for JSON output)
    transformed_data = df_transformed.to_dict(orient='records')

    with open(f"./jsonData/{RAW_DATA_FILE}", 'w') as f:
        json.dump(transformed_data, f, indent=4)

    print(f"Successfully transformed data and saved to {TRANSFORMED_DATA_FILE}")

except FileNotFoundError:
    print(f"Error: Raw data file '{RAW_DATA_FILE}' not found at 'input_path'. Ensure Extract stage ran successfully.")
    exit(1)
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from raw data file.")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred during transformation: {e}")
    exit(1)