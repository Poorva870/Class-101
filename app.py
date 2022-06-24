import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f=open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token='sl.BKLXSbxKtjcaParvilEjWRxir_DWcBI76-JL966p64PAH3SEEAs-LoB9y9y83rv-rxa1__9mhyUB8QYaLsZgauqo1sSt-_qbhhdUJMWVszD-WbYijWfV5wajzH5scC49T7dsvOtDXaA'
    transferData=TransferData(access_token)

    file_from=input('Enter the file path to transfer')
    file_to=input('Enter the full path to upload to the dropbox')

    transferData.upload_file(file_from, file_to)
    print('the file has been moved')

main()