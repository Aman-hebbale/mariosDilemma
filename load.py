import json
import os

TRANSFORMED_DATA_FILE = 'transformed_posts.json'
FINAL_OUTPUT_FILE = 'final_api_data.json' # Renaming for final output clarity
INPUT_DIR = os.getenv('WORKSPACE', '.') # Jenkins workspace
OUTPUT_DIR = os.getenv('WORKSPACE', '.') # Jenkins workspace (same dir for this example)

# input_path = os.path.join(INPUT_DIR, TRANSFORMED_DATA_FILE)
# output_path = os.path.join(OUTPUT_DIR, FINAL_OUTPUT_FILE)

print(f"--- Load Stage ---")
# print(f"Loading data from: {input_path}")

try:
    with open(f"./jsonData/{TRANSFORMED_DATA_FILE}", 'r') as f:
        data_to_load = json.load(f)

    # --- L: Load Logic ---
    # For this simple example, loading means writing to another JSON file.
    # In a real ETL, this could be:
    # - Inserting into a database (PostgreSQL, MySQL, etc.)
    # - Uploading to a cloud storage (S3, GCS)
    # - Sending to a data warehouse (Snowflake, BigQuery)
    # - Pushing to a message queue

    with open(f"./jsonData/{FINAL_OUTPUT_FILE}", 'w') as f:
        json.dump(data_to_load, f, indent=4)

    print(f"Successfully loaded {len(data_to_load)} records to {FINAL_OUTPUT_FILE} at output_path")
    print(f"Content of {FINAL_OUTPUT_FILE} (first 20 lines):")
    # This block won't run directly in python but gives an idea for shell command
    # with open(output_path, 'r') as f_out:
    #     for i, line in enumerate(f_out):
    #         if i >= 20: break
    #         print(line.strip())

except FileNotFoundError:
    print(f"Error: Transformed data file '{TRANSFORMED_DATA_FILE}' not found at 'input_path'. Ensure Transform stage ran successfully.")
    exit(1)
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from transformed data file.")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred during loading: {e}")
    exit(1)