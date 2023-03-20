import os
import requests
import logging

logging.basicConfig(level=logging.INFO)

versions_meta = requests.get("https://piston-meta.mojang.com/mc/game/version_manifest_v2.json").json()

def get_latest_version_code():
    return versions_meta['latest']['release']

def get_version_info(version_code: str) -> dict:
    versions = versions_meta['versions']

    for version in versions:
        if version['id'] == version_code:
            break
    else:
        raise ValueError("Unable to find the specified version")
    
    version_meta_url = version['url']

    return requests.get(version_meta_url).json()

def download_server(version_info: dict, path: str = 'server.jar'):
    version_server_download_url = version_info['downloads']['server']['url']

    with open(path, 'bw') as server_jar:
        server_jar.write(requests.get(version_server_download_url).content)

def download_latest_server(path: str = 'server.jar'):
    latest_info = get_version_info(
        get_latest_version_code(),
    )

    download_server(latest_info, path)

def agree_eula(folder: str = "."):
    with open(os.path.join(folder, "eula.txt"), 'w', encoding='utf-8') as eula_file:
        eula_file.write("eula=true")

if __name__ == "__main__":
    logging.info("Downloading server...")
    #download_latest_server()
    logging.info("Server downloaded")

    agree_eula()
    logging.info("Agreed to EULA")
