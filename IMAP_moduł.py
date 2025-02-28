from imapclient import IMAPClient
import getpass
imapObj = IMAPClient('imap.outlook.com',ssl=True) #nawiązywanie połączenia z serwerem IMAP
hasło = getpass.getpass("Podaj hasło: ")
imapObj.login('pythontest26@outlook.com',hasło)#logowanie w serwerze IMA

all_folders = imapObj.list_sub_folders()
s_folder = imapObj.select_folder('inbox')
print('%d messages in INBOX' % s_folder[b'EXISTS'])
tr = imapObj.search(['FROM' ,'karrokgamer21@gmail.com'])

print(f"%d messages from sb "% len(tr))
data = imapObj.search(['SUBJECT raz'])
print(f"{data}")
