import os
import requests
import mimetypes
from azure.storage.blob import ContentSettings
from urllib.parse import urlparse
import glob  # For easier subdirectory handling

directory = '/root/utilities/hpcBocconiTools/datalake/data_post_generated/'  # Replace with the actual directory path
 
def upload_using_sas(sas_url , file_name_full_path):
    """
    Upload File using Azure SAS url.
    This function uploads file to Azure blob container
    :param sas_url:  Azure sas url with write access on a blob storage
    :param file_name_full_path:  File name with fill path
    :return:  HTTP response status of file upload
    """
    o = urlparse(sas_url)
    # Remove first / from path
    if o.path[0] == '/':
        blob_storage_path = o.path[1:]
    else:
        blob_storage_path = o.path
 
    storage_account = o.scheme + "://" + o.netloc + "/"
    file_name_only = os.path.basename(file_name_full_path)
    response_status = put_blob(storage_account,blob_storage_path,file_name_only,o.query,file_name_full_path)
    return response_status
 
 
def put_blob(storage_url,container_name, blob_name,qry_string,file_name_full_path):
    file_name_only = os.path.basename(file_name_full_path)
    try:
        file_ext = '.' + file_name_only.split('.')[1]
    except IndexError:
        file_ext = None
    # Set content Type
    if file_ext is not None:
        mimetypes.add_type('application/octet-stream', '.parquet')
        content_type_string = ContentSettings(content_type=mimetypes.types_map[file_ext])
    else:
        content_type_string = None
 
    with open(file_name_full_path , 'rb') as fh:
        response = requests.put(storage_url+container_name + '/' + blob_name+'?'+qry_string,
                                data=fh,
                                headers={
                                            'content-type': content_type_string.content_type,
                                            'x-ms-blob-type': 'BlockBlob'
                                        },
                                params={'file': file_name_full_path}
                                )
        return response
   



def main():
    """
    Iterates through parquet files in a directory, send them to datalake, and renames them when done.
    """

    directory = '/root/utilities/hpcBocconiTools/datalake/data_post_generated/'  # Replace with the actual directory path

    # Use glob to recursively find all Parquet files in subdirectories
    for parquet_path in glob.glob(os.path.join(directory, "**/*.parquet")):
        filename = os.path.basename(parquet_path)
        subdirectory = os.path.dirname(parquet_path) # Extract subdirectory
        
        sas_url_for_upload_resources_usage = ( "https://reportingbidlsaccount.blob.core.windows.net/reportingbidlsfs/HPC/resources_usage/"+subdirectory+"/?sv=2020-02-10&st=2025-02-06T08%3A25%3A00Z&se=2099-02-07T10%3A25%3A00Z&sip=193.205.30.60&sr=d&sp=racwlme&sig=7nAHO0BFLizJKhd76v54%2BnYcn0fttstIRUS0xg2nR%2FM%3D&sdd=1")
        sas_url_for_upload_users_accounts = ( "https://reportingbidlsaccount.blob.core.windows.net/reportingbidlsfs/HPC/users_accounts/"+subdirectory+"/?sv=2020-02-10&st=2025-02-06T08%3A25%3A00Z&se=2099-02-07T10%3A25%3A00Z&sip=193.205.30.60&sr=d&sp=racwlme&sig=7nAHO0BFLizJKhd76v54%2BnYcn0fttstIRUS0xg2nR%2FM%3D&sdd=1")
 

        print("Uploading file: " + parquet_path)

        if filename.startswith("users"):
            response = upload_using_sas(sas_url_for_upload_users_accounts, parquet_path)
        elif filename.startswith("resources"):
            response = upload_using_sas(sas_url_for_upload_resources_usage, parquet_path)
        else:
            print("Warning: no upload will be performed for unexpected filename: " + filename)
            response = None # Set response to None for consistency

        if response: # Check if the upload was successful before renaming
            done_path = parquet_path + ".done"
            try:
                os.rename(parquet_path, done_path)
                print(f"Renamed {parquet_path} to {done_path}")
                print("Response code:", response.status_code) # Access status code
                print(response.text) # Access the response body
            except OSError as e:
                print(f"Error renaming {parquet_path}: {e}")
        else:
            print("Upload failed, not renaming file.")

if __name__ == "__main__":
    main()