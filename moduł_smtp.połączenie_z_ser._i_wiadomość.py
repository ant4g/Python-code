import smtplib
import getpass
port = 587

hasło = getpass.getpass("Podaj hasło: ")

nadawca = 'pythontest26@outlook.com'
adresat = 'yixobac128@regapts.com'
treść = """Subject: Mail send using python
Hi,

This is a test email.

Thanks,
Test Account"""

smtpObj = smtplib.SMTP('smtp-mail.outlook.com',port) # tworzenie obiektu smtp
smtpObj.ehlo() #nawiązanie komunikacji serwerem pocztowym, sprawdzenie czy działa
# print(f"[*]Echoing the server: {status_code}{response}")


smtpObj.starttls()#szyfrowanie
# print(f"[*] Starting TLS connection: {status_code}{response}") #wyświetlenie odpowiedzi serwera jak przy echo

smtpObj.login(nadawca,hasło)#logowanie
# print(f"[*] Logging in: {status_code}{response}")


smtpObj.sendmail(nadawca,adresat,treść)#wysyłanie maila

smtpObj.quit() #zakończenie