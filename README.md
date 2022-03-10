# Brutus - Simple login form dictionary attack tool

## Usage
`brutus.py -u <url> -l <login name from html form> -p <password name from html form> -w <wordlist>`

- -u  : URL of page with login form
- -l   :  login "name" form form (for example in wordpress it is usually *log* )
- -p  :  password "name" form form (for example in wordpress it is usually *pwd* )
- -w :	path to wordlist 

ACHTUNG: Replace line 47 with: wordlist = open(options.wordlist, "r", errors='replace').readlines()
I am too lazy to commit changes
