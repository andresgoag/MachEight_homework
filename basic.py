
from libs import get_players, get_matching_pairs

def main():
    while True:
        try:
            target = input('Input the desired sum of heights ("q" to quit): ')
            if target == "q":
                break
            else:
                target = int(target)
        except:
            print("Sum must be an integer")

        players = get_players()
        if players:
            result = get_matching_pairs(target, players)
            result = map(list, result)
            if result:
                for pair in result:
                    print(f"{pair[0]} & {pair[1]}")
            else:
                print("No matches found")
        else:
            print("Error fetching source data")


if __name__ == "__main__":
    main()