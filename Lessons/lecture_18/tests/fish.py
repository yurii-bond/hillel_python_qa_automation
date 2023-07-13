import unittest


def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"tank_a": fish_list}


class TestAddFishToAquarium(unittest.TestCase):
    def test_add_fish_to_aquarium(self):
        actual = add_fish_to_aquarium(['shark', 'tuna'])
        expected = {'tank_a': ['shark', 'tuna']}
        self.assertEqual(actual, expected)

    def test_add_fish_to_aquarium_exceprion(self):
        with self.assertRaises(ValueError):
            add_fish_to_aquarium(fish_list=['shark', 'tuna', 'salmon', 'nemo', 'ass', 'dfd', 'dfdf', 'dfdf', 'dfgg', 'fgfgf', 'dfdd'])
