import requests


def dowload_file():
    file_id = '1xGE_3R6hgND2XoeXz5xhsMhid11HExNK'
    url = 'https://drive.google.com/uc?export=download&id=' + file_id
    file_name = 'file.csv'

    session = requests.Session()
    response = session.get(url, stream=True)

    token = None
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            token = value
            break

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(url, params=params, stream=True)

    with open(file_name, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return file_name


