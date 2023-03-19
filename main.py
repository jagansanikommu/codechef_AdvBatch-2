import requests
from bs4 import BeautifulSoup
def count(user):
    url = "https://www.codechef.com/users/"+user
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    w = soup.find("h5")
    if w==None:
        return "Invalid Id"
    w1= w.text.split()
    number = w1[-1]
    return (number[1:-1])
l=["vits21985a0410","Vitsh_26","Saikiran_999","Vits21895a0411","harinireddy19","Pranav_59","Vits20891a6604","maleVidyanjali","vits20891a0478","namithareddy17","rohitkumar5a9","boga.bhuvaneshwari13042002@gmail.com","charancherry4","rahulgantla","jagans_7","Manish9912","nagaraju_6653","vits20891a0406","jayanthpwr","p_jcr","siddanirohith","20891A05E7_Nishanth","Vits20891a6649","vits20891a0425","mohdamer513","vardhan16","ashrith23","nikhilgoud143","badetijyothi55@gmail.com","sanjay106","sabavathanveen","abilash_yadav","Supriya0501","saiteja@5","Vitsh_14","Vits20891A0480","Sana323","vits20891a05h3","ashokgoudkavali@gmail.com","balu_06","shiva0219","Vits20891a0435","nikhilalpatla6","vivek452","vits20891a0588","mahathi_1230","vits20891a0441","vits20891a04e5","vighnesh_2002","Vishnusaimatta186","fayazuddin786a","karthiiik666","Vits20891a04e5","Sri_60","Nikitha_2012","nikhilalpatla6","saikiranbanda0","vits20891a1208","jayasimha_30","akshithamodepu"]
data=[]

for i in l:
    data.append(count(i))

for i in range(len(l)):
    print(data[i])
for i in range(len(l)):
    print(l[i])



