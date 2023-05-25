import requests
from bs4 import BeautifulSoup
def process(user):
    url = "https://www.codechef.com/users/"+user
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    w = soup.find("h5")
    if w==None:
        return 0
    w1= w.text.split()
    number = w1[-1]
    return (number[1:-1])

def count(l):
    data=[]
    for i in l:
        i=str(i)[2:-3]
        data.append(process(i))
    return data





