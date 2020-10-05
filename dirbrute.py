import requests
import argparse


parcer = argparse.ArgumentParser()
parcer = argparse.ArgumentParser()
parcer.add_argument("url", help="complete url of website including http or https")
parcer.add_argument("wordlist", help="path of wordlist")
parcer.add_argument("output", help="output file name")

G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'  # white

print("""%s
 _ _
|    \     _                _ _ _ _     _ _ _     _        _    _ _ _ _ _ _ _ _    _ _ _ _ _
|  _  \  ( _ )  __ _ _ _   |  _ _  \  /  _   \   |  |     |  | |                | |   _ _ _ |
| | |  \ |   | |  ' _ _ |  | |_ _| | |  |  \  \  |  |     |  | |_ _ _      _ _ _| |  |
| | |  / |   | |  |        |_ _ _ _/ |  |_ /  /  |  |     |  |        |   |       |   \_ _ _
| |_| /  |   | |  |        |  _ _ \  |_ _ _ _/   |  |     |  |        |   |       |    _ _ _|
|    /   |   | |  |        | |   | | |   _  \    |  |_ _ _|  |        |   |       |   /
|   /    |   | |  |        | |_ _| / |  | \  \   \           /        |   |       |   |_ _ _
|__/     |___| |__|        |_ _ _ /  | _|  \ _\   \_ _ _ _ _/         |_ _|       |_ _ _ _ _|%s%s
            # Coded By AKSHAT SINGHAL - @HONEYAKSHAT999
""" % (B, W, R))
args = parcer.parse_args()
url = args.url
wordlist = args.wordlist
outputfile= args.output
a= ""
number = 1
fileobj = open(wordlist,"r")
outfile = open(outputfile , "w+")



#function for get requests
def requesting(uris):


    c = url+"/"+ uris
    b = requests.get(c)
    d = b.status_code
    ak = uris.strip("\n")
    outfile.write("/%s   %s\n" % (ak,d))


#loop for printing the output
for i in fileobj:
    requesting(i)


