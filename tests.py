import unittest

from libs import (
    get_players,
    get_name,
    create_map,
    append_pairs,
    get_matching_pairs
)

class Tests(unittest.TestCase):

    def test_get_players(self):
        result = get_players()
        self.assertEqual(len(result), 435)

    def test_get_name(self):
        player = {
            "first_name": "Alex",
            "h_in": "77",
            "h_meters": "1.96",
            "last_name": "Acker"
        }
        result = get_name(player)
        self.assertEqual(result, "Alex Acker")

    def test_create_map(self):
        players = [
            {
                "first_name": "Alex",
                "h_in": "77",
                "h_meters": "1.96",
                "last_name": "Acker"
            },
            {
                "first_name": "Hassan",
                "h_in": "76",
                "h_meters": "1.93",
                "last_name": "Adams"
            },
            {
                "first_name": "Arron",
                "h_in": "77",
                "h_meters": "1.96",
                "last_name": "Afflalo"
            },
        ]
        expected_result = {
            76: ["Hassan Adams"],
            77: ["Alex Acker", "Arron Afflalo"]
        }
        result = create_map(players)
        self.assertEqual(result, expected_result)

    def test_append_pairs(self):
        player_name = "Hassan Adams"
        partners = ["Alex Acker", "Arron Afflalo"]
        initial_result = [{"Hassan Adams", "Arron Afflalo"}]
        result = append_pairs(player_name, partners, initial_result)
        expected_resutlt = [{"Hassan Adams", "Arron Afflalo"}, {"Hassan Adams", "Alex Acker"}]
        self.assertEqual(result, expected_resutlt)

    def test_get_matching_pairs(self):
        target = 139
        players = get_players()
        result = get_matching_pairs(target, players)
        expected_result = [{"Brevin Knight", "Nate Robinson"}, {"Nate Robinson", "Mike Wilks"}]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()