import requests

target = 139

def get_players():
    req = requests.get('https://mach-eight.uc.r.appspot.com')
    if req.status_code == 200:
        return req.json()['values']
    else:
        return None

def get_name(player: dict):
    return f"{player['first_name']} {player['last_name']}"

def create_map(players: list):
    mapped = {}
    for player in players:
        height = int(player['h_in'])
        if height in mapped.keys():
            mapped[height].append(get_name(player))
        else:
            mapped[height] = [get_name(player)]
    return mapped

def append_pairs(player_name:str, partners: list, result: list):
    for partner in partners:
        pair = {player_name, partner}
        if pair not in result:
            result.append(pair)
    return result


def main():
    results = []
    players = get_players()

    if players:
        mapped_table = create_map(players)

        for player in players:
            player_name = get_name(player)
            height = int(player['h_in'])
            key = target - height
            if key in mapped_table:
                results = append_pairs(player_name, mapped_table[key], results)

        return results


    else:
        return 'Error fetching source data'


if __name__ == '__main__':
    print(main())