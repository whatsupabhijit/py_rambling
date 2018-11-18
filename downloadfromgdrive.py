import requests
import sys

def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None


    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:
                    f.write(chunk)



    URL = "https://drive.google.com/uc?id=1dmstpGhmgYINQlZVPIZM_72dZtgsIeJT"

    session = requests.session()

    response = session.get(URL, params = {'id':id}, stream = True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream = True)

    save_response_content(response, destination)



if __name__ == '__main__':
    print (len(sys.argv))
    if len(sys.argv) is not 3:
       print ("Usage : python <<this file.py>> <<file_id>> <<destination_file_path>>")

    else:
       file_id = sys.argv[1]
       destination = sys.argv[2]
       download_file_from_google_drive(file_id, destination)

