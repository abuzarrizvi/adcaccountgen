#import webbrowser
import subprocess

#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
email = input("email: ")
password = input("password: ")

url = 'https://cp.adidas.com/idp/startSSO.ping?username={}&password={}&signinSubmit=Sign+in&IdpAdapterId=adidasIdP10&SpSessionAuthnAdapterId=https%3A%2F%2Fcp.adidas.com%2Fweb%2F&PartnerSpId=sp%3Ademandware&validator_id=adieComDWgb&TargetResource=https%3A%2F%2Fwww.adidas.com%2Fon%2Fdemandware.store%2FSites-adidas-US-Site%2Fen_US%2FMyAccount-ResumeLogin&target=account&InErrorResource=https%3A%2F%2Fwww.adidas.com%2Fon%2Fdemandware.store%2FSites-adidas-US-Site%2Fen_US%2Fnull&loginUrl=https%3A%2F%2Fcp.adidas.com%2Fweb%2FeCom%2Fen_US%2Floadsignin&cd=eCom%7Cen_US%7Ccp.adidas.com%7Cnull&remembermeParam=&app=eCom&locale=US&domain=cp.adidas.com&pfRedirectBaseURL_test=https%3A%2F%2Fcp.adidas.com&pfStartSSOURL_test=https%3A%2F%2Fcp.adidas.com%2Fidp%2FstartSSO.ping%3F&resumeURL_test=&FromFinishRegistraion=&CSRFToken=null'.format(email, password)

subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "-incognito", url])

#webbrowser.open_new(url)
