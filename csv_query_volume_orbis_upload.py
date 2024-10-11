import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path='.env', override=True)

# Get environment variables
CONTEXT_ID = os.getenv("CONTEXT_ID")
TABLE_ID = os.getenv("TABLE_ID")

# CSV file path
csv_file_path = 'hourly_query_volume_20241011_04.csv'

# Get upload url
upload_url = os.getenv("ORBIS_UPLOAD_ENDPOINT")

def upload_csv():
    # Open the CSV file
    with open(csv_file_path, 'rb') as csv_file:
        # Prepare the files for the request
        files = {'file': ('hourly_query_volume_20241011_04.csv', csv_file, 'text/csv')}
        
        # Make the POST request to upload the CSV
        response = requests.post(upload_url, files=files)
        
        # Check the response
        if response.status_code == 200:
            print("CSV uploaded successfully!")
            print("Response:", response.json())
        else:
            print(f"Error uploading CSV. Status code: {response.status_code}")
            print("Response:", response.text)

if __name__ == "__main__":
    upload_csv()
