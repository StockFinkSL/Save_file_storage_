# +
# #!pip install azure-storage-blob
# -

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connect_str = "DefaultEndpointsProtocol=https;AccountName=stockcard;AccountKey=19xGGa3YNRKzwBMJUdsUdkQ547OkjxJelp0DzDl6DXa/zznYosZDR7f+AmkIxJISSVgub2mPy4bH+ASt0A3Nuw==;EndpointSuffix=core.windows.net"

blob_service_client = BlobServiceClient.from_connection_string(connect_str)

container_name = "output"

# +
file_name = "archivo.txt"

with open(file_name, "w") as file:
    file.write("Hola Demo")
# -

blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

# +
import os

current_path = os.getcwd()
file_path = os.path.join(current_path, file_name)

print(file_path)
# -

with open(file=file_path, mode="rb") as data:
    blob_client.upload_blob(data)














