import os
import requests
import mimetypes
from azure.storage.blob import ContentSettings
from urllib.parse import urlparse
 
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
        return response.status_code
   
sas_url_for_upload = ( "https://reportingbidlsaccount.blob.core.windows.net/reportingbidlsfs/HPC?"
                      "sv=2020-02-10&st=2024-12-06T12%3A52%3A47Z&se=2024-12-07T12%3A52%3A47Z&sip=10.1.61.30-10.1.61.132&sr=d&sp=racwlm&sig=kdouJe1GZLhzbZHD0D6zqaeJqcOUmw9AZbrQkqBoVUg%3D&sdd=1"
)
 
file_to_upload =  r'/root/utilities/hpcBocconiTools/dataToReport/test_table_0.txt'
 
r= upload_using_sas(sas_url_for_upload, file_to_upload)
 
print ("Upload Status :" + str(r))
