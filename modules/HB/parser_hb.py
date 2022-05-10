import requests
import bs4

def request(page, cookies = None):
    return requests.get(page, cookies = cookies) if cookies else requests.get(page)

def get_infos_for(user, cookies, nb_cellules_per_user = 13):
    soup = bs4.BeautifulSoup(request(f"https://www.herobrine.fr/index.php?p=members&search={user}", cookies).text, "html5lib")
    temp = soup.find(id="main").find_all("td")
    for i in range(len(temp) // nb_cellules_per_user):
        if temp[nb_cellules_per_user*(i-1)].a.text.strip() == user:
            ampoules = [0, 0, 0]
            for img in temp[nb_cellules_per_user*(i-1) + 11].find_all("img"):
                if "lamp1" in img["src"]:
                    ampoules[0] += 1
                elif "lamp0" in img["src"]:
                    ampoules[1] += 1
                elif "lampnull" in img["src"]:
                    ampoules[2] += 1
            return [
                temp[nb_cellules_per_user*(i-1)].a.text.strip(), 
                temp[nb_cellules_per_user*(i-1)].a["title"].split(" ")[-1].strip(),
                temp[nb_cellules_per_user*(i-1)].a["href"].split("=")[-1].strip(),
                temp[nb_cellules_per_user*(i-1) +1].text.strip(),
                temp[nb_cellules_per_user*(i-1) +2].img["title"].strip(), 
                "Pas de BG" if temp[nb_cellules_per_user*(i-1) +3].img is None else temp[nb_cellules_per_user*(i-1) +3].img["title"].strip(), 
                temp[nb_cellules_per_user*(i-1) +4].text.strip(), 
                temp[nb_cellules_per_user*(i-1) +5].text.strip(),
                temp[nb_cellules_per_user*(i-1) +6].text.strip(), 
                "0" if temp[nb_cellules_per_user*(i-1) +7].text == "" else temp[nb_cellules_per_user*(i-1) +7].text.strip(),
                temp[nb_cellules_per_user*(i-1) +10].img["title"].strip(), 
                sum(ampoules), 
                *ampoules
                , temp[nb_cellules_per_user*(i-1)].a["href"].split("=")[-1].strip(),
            ]

def connection(email, mdp):
    payload = {'email': email, 'pass': mdp, 'login': '1'}
    return requests.post("https://www.herobrine.fr/index.php?p=login", data=payload)
