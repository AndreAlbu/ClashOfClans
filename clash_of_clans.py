import requests
import json, urllib.parse

headers = {
    "Content-type": "application/json",
    "Authorization": "Bearer }


def urlEncode(tag):
    return urllib.parse.quote(tag)


def cla_informacoes(headers, tag):
    url_clan = "https://api.clashofclans.com/v1/clans/" + tag

    response = requests.get(url=url_clan, headers=headers)

    if response.status_code == 200:
        item_obj = json.loads(response.text)

        print("Nome do Cla: " + item_obj["name"])
        print("Tag: " + item_obj["tag"])
        print("Descricao: " + item_obj["description"].replace("     ", " "))
        print("Liga do Cla: " + item_obj["warLeague"]["name"])
        print("Nivel do Cla: " + str(item_obj["clanLevel"]))
        print("Pontos do Cla: " + str(item_obj["clanPoints"]))
        print("Pontos da Capital Cla: " + str(item_obj["clanCapitalPoints"]))
        print("Quantidade Membros: " + str(item_obj["members"]))
        print("Guerras vencidas: " + str(item_obj["warWins"]))
        print("Guerras empatadas: " + str(item_obj["warTies"]))
        print("Guerras perdidas: " + str(item_obj["warLosses"]))
        print("Language: " + str(item_obj["chatLanguage"]["name"]))
        print("Pais: " + item_obj["location"]["name"])
        print("Logo Cla: " + item_obj["badgeUrls"]["medium"])


def cla_membros(headers, tag):
    url_clan_membros = "https://api.clashofclans.com/v1/clans/" + tag + "/members"

    response = requests.get(url=url_clan_membros, headers=headers)

    if response.status_code == 200:
        item_obj = json.loads(response.text)
        item_lista = item_obj.get("items")

        for item in item_lista:
            print("Tag: " + str(item["tag"]))
            print("Nome: " + str(item["name"]))
            print("Cargo: " + str(item["role"]))
            print("Centro Vila: " + str(item["townHallLevel"]))
            print("Nivel de Experiencia: " + str(item["expLevel"]))
            print("Classificacao no Cla: " + str(item["clanRank"]))
            print("Doacoes: " + str(item["donations"]))
            print("Doacoes recebidas: " + str(item["donationsReceived"]))
            print("Trofeus: " + str(item["trophies"]))
            print("Trofeus Base Construtor: " + str(item["builderBaseTrophies"]))
            print("=============================")


def cla_historico_guerra(headers, tag):
    url_guerra = "https://api.clashofclans.com/v1/clans/" + tag + "/warlog"

    response = requests.get(url=url_guerra, headers=headers)

    if response.status_code == 200:
        item_obj = json.loads(response.text)
        item_lista = item_obj.get("items")

        for item in item_lista:
            print("Cla: " + item["clan"]["name"])
            print("Openente: " + str(item["opponent"]["tag"]))


def clan_liga_guerra(headers, tag):
    url_liga_guerra = "https://api.clashofclans.com/v1/clanwarleagues/wars/" + tag

    response = requests.get(url=url_liga_guerra, headers=headers)

    if response.status_code == 200:
        item_obj = json.loads(response.text)

        print(item_obj)


def clan_guerra(headers, tag):
    url_guerra = "https://api.clashofclans.com/v1/clans/" + tag + "/currentwar"

    response = requests.get(url=url_guerra, headers=headers)

    if response.status_code == 200:
        item = json.loads(response.text)

        clan = item["clan"]
        oppe = item["opponent"]

        print("Cla: " + str(clan["name"]) + "   X   Oponente: " + str(oppe["name"]))
        print("Ataque: " + str(clan["attacks"]) + " X " + str(oppe["attacks"]))
        print("Estrelas: " + str(clan["stars"]) + " X " + str(oppe["stars"]))


tagPlayer = "#9PLP92G29"
tagCla = "#2QVCLR9U9"

tagCla = urlEncode(tagCla)

# cla_membros(headers, tagCla)
# cla_informacoes(headers, tagCla)
# cla_historico_guerra(headers, tagCla)
# clan_liga_guerra(headers, tagCla)
clan_guerra(headers, tagCla)
