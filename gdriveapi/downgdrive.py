file_id = '1dmstpGhmgYINQlZVPIZM_72dZtgsIeJT'


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
http = credentials.authorize(httplib2.Http())        
drive_service = discovery.build('drive', 'v3', http=http)






request = drive_service.files().get_media(fileId=file_id)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print ("Download %d%%." % int(status.progress() * 100))
