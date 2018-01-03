# Adidas Account Generator

## Description
Python account generator for adidas.com. Uses gmail "." trick to make 2^(n-1) accounts per gmail address. Solved captchas manually. 

## Requirements
- Python 3+
- `requests`
- `bs4`
- `flask`
- `colorama`
- `termcolor`

## Installation and Usage
- You need to add the below line to your hosts file (google how to do this if you do not know)
- `127.0.0.1 fuckrsvpkingz.adidas.co.uk`
- Make sure you have installed all of the modules listed above, using `pip install` (or `pip3 install` if you have python2 too) to do so
- Edit `config.json` with a suitable editor e.g. sublime or atom (NOT NOTEPAD)
- `cd` into the directory location
- `python main.py` or `python3 main.py` if you also have python2 installed and added to path
- You must SOLVE CAPTCHAS MANUALLY (one per account you want to create)

## To-Do List
- [X] Add captcha support
- [X] Catch-all domain support
- [X] Random password generation
- [ ] 2captcha support
- [X] Gmail tricks support
- [ ] Multi-threading
- [ ] Custom password usage
- [ ] No captcha site. (might make private)


## Notes
- If you choose 100 accounts, be prepared to solve 100 captchas. If you exit the script before all accounts have been created they will NOT be saved
- Credit to Ryan9918 for the original script.
