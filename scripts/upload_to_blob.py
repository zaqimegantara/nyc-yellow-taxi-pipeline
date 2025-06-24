import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv("config/.env")

AZURE_CONNECTION_STRING=os.getenv("AZURE_STORAGE_CONNECTION")
CONTAINER_NAME = "raw-data"

# File path to the local Parquet file
local_file_path = "data/yellow_tripdata_2025-01.parquet"
blob_name = os.path.basename(local_file_path)

def upload_to_blob():
    try :
        # Initialize blob client
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)

        # Upload the file
        with open(local_file_path, "rb") as data :
            blob_client.upload_blob(data, overwrite=True)

        print(f"Uploaded '{blob_name}' to container '{CONTAINER_NAME} succesfully.")

    except Exception as e :
        print(f"Error: {e}")

if __name__ == '__main__' :
    upload_to_blob()

    https://sangkurianggas.blob.core.windows.net/raw-data?sp=r&st=2025-06-06T12:01:31Z&se=2025-06-07T12:01:31Z&spr=https&sv=2024-11-04&sr=c&sig=pu4OChSBbC3ua27yzTHyO2xhZbQunptFGEHRR7xK6XM%3D