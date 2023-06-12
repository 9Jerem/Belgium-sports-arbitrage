from bs4 import BeautifulSoup
import requests


def get_page():
    url = "https://paris-sportifs.pmu.fr/pari/competition/9137/football/matchs-amicaux"
    response = requests.get(url, headers={'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"})
    html = BeautifulSoup(response.content, 'html.parser')
    return html

print("Le script est en cours d'exécution.")
page = get_page()


def get_games():
    html = get_page()
    games = []
    games_elements = html.select(".row.trow")
    for el in games_elements:
        game_name = el.select(".obet-event-list-grid-formatter-col.col-rows.col-xs-3")[0].text.strip()
        game_name = "".join(game_name.split())
        team1, team2 = game_name.split("//")
        odds_el = el.select(".col-sm-3.trow--odd--item")
        odds = []
        for el2 in odds_el: 
            tmp = "".join(el2.text.split()).replace(",", ".")
            odds.append(float(tmp))
        
        games.append({
            'team1': team1,
            'team2': team2,
            'odds': odds
        })
    return games 




        

        



        


















