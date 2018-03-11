
from __future__ import print_function
import httplib2
import os
import base64

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    
    test     = service.users().messages().list(userId='me').execute()
    currEmails = test.get('messages',[])
    
    getting     = service.users().messages().get(userId='me',id='162133ca343e1a94').execute()
    getMsg = getting.get('payload',[])
#    getMsg = getMsg['body']
#    getMsg = getMsg.get('data')
#    getMsg = getMsg['data']

    
#    print(type(getMsg['parts']))
    listTest = getMsg['parts']
    listTest = listTest[0]
    listTest = listTest['body']
    print(base64.urlsafe_b64decode(temp['data']))
#    for data in getMsg['parts']:
#        temp = (data['body'])
##        print(temp['data'])
#        print(base64.urlsafe_b64decode(temp['data']))
#    now the issue with the previous line is that this "JSON" object data from the web request
#   gets stored in a dictionary so we can access a "KEY" in the dictionary usually a string
#   something like getMsg['pay']


if __name__ == '__main__':
    main()