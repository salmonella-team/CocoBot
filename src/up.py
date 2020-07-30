from requests.models import Response
from webdav3.client import Client as NCClient
import requests
import settings
import xmltodict

options = {
    'webdav_hostname': settings.NC_URL,
    'webdav_login': settings.NC_NAME,
    'webdav_password': settings.NC_PASS
}


client = NCClient(options)
client.verify = False


def uploadFile(file_name):
    file_path = "youtube_dl/test/" + file_name
    file_local_path = "./src/" + file_name
    client.upload_sync(remote_path=file_path, local_path=file_local_path)

def changeShareFile(file_name: str) -> str:
    file_path = "youtube_dl/test/" + file_name
    url = "https://owncloud.s4m0r1.me/ocs/v2.php/apps/files_sharing/api/v1/shares?path=" + file_path + "&shareType=3"
    r = requests.request(
        method="POST",
        url=url,
        auth=(settings.NC_NAME,settings.NC_PASS),
        headers={"OCS-APIRequest":"true"},
    )

    r = xmltodict.parse(r.text)
    return r["ocs"]["data"]['url']