import requests as req
import argparse
from termcolor import colored
from os import getcwd

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--domain", dest="domain",
                    help="Example : python madpi.py -d https://api.target.com")
parser.add_argument("-w", "--wordlists", dest="wordlists",
                    help="Example : python madpi.py -d https://api.target.com -w /usr/share/wordlists/api_seen_in_wild.txt")

args = parser.parse_args()

domain = args.domain
wordlists = args.wordlists

text = colored("Api Enumeration By MrMad", "yellow")
print("""
  /\/\   __ _  __| |_ __ (_)
 /    \ / _` |/ _` | '_ \| |
/ /\/\ \ (_| | (_| | |_) | |
\/    \/\__,_|\__,_| .__/|_|
                   |_|      v.1
    {}
""".format(text))

if args.domain == None:
    print("Example : python madpi.py -d api.target.com -w /usr/share/wordlists/api.txt")
elif args.wordlists == None:
    with open("{}/wordlists/common_paths.txt".format(getcwd()), "r") as api:
        read = api.read()
        expl = read.split("\n")
        count = len(expl)
        Note = colored("[+] Domain must be using https/http", "green")
        print(Note)
        for i in range(0, count):
            dataApi = "{}/{}".format(domain, expl[i])
            r = req.get(dataApi)
            if r.status_code == 200:
                print("{} [{}]".format(
                    dataApi, colored(r.status_code, "green")))
            else:
                print("{} [{}]".format(
                    dataApi, colored(r.status_code, "yellow")))
elif args.domain and args.wordlists:
    with open(wordlists, "r") as pi:
        read = pi.read()
        xpl = read.split("\n")
        hitung = len(xpl)
        struck = """
Domain      : {}
Wordlists   : {}
Total List  : {}
""".format(domain, wordlists, hitung)
        Notes = colored("[+] Domain must be using https/http", "green")
        print(Notes)
        print(struck)
        for i in range(0, hitung):
            ApiData = "{}/{}".format(domain, xpl[i])
            r = req.get(ApiData)
            if r.status_code == 200:
                print("{} [{}]".format(
                    ApiData, colored(r.status_code, "green")))
            else:
                print("{} [{}]".format(
                    ApiData, colored(r.status_code, "yellow")))
