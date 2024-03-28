from worlds.monster_sanctuary.tests.Monsters.Test_MonsterRandomizer import TestMonsterRandomizerBase


class TestFamiliarWolf(TestMonsterRandomizerBase):
    options = {
        "starting_familiar": 0
    }
    run_default_tests = False

    def test_starting_familiar(self):
        location = self.multiworld.get_location("Menu_0_0", self.player)
        if self.world.options.starting_familiar == "wolf":
            self.assertEqual(location.item.name, "Spectral Wolf")
        elif self.world.options.starting_familiar == "eagle":
            self.assertEqual(location.item.name, "Spectral Eagle")
        elif self.world.options.starting_familiar == "toad":
            self.assertEqual(location.item.name, "Spectral Toad")
        elif self.world.options.starting_familiar == "lion":
            self.assertEqual(location.item.name, "Spectral Lion")


class TestFamiliarWolf_Shuffle(TestFamiliarWolf):
    options = {
        "starting_familiar": 0,
        "randomize_monsters": 2
    }
    run_default_tests = False


class TestSpectralEagle(TestFamiliarWolf):
    options = {
        "starting_familiar": 1
    }
    run_default_tests = False


class TestSpectralEagle_Shuffle(TestFamiliarWolf):
    options = {
        "starting_familiar": 1,
        "randomize_monsters": 2
    }
    run_default_tests = False


class TestSpectralToad(TestFamiliarWolf):
    options = {
        "starting_familiar": 2
    }
    run_default_tests = False


class TestSpectralToad_Shuffle(TestFamiliarWolf):
    options = {
        "starting_familiar": 2,
        "randomize_monsters": 2
    }
    run_default_tests = False


class TestSpectralLion(TestFamiliarWolf):
    options = {
        "starting_familiar": 3
    }
    run_default_tests = False


class TestSpectralLion_Shuffle(TestFamiliarWolf):
    options = {
        "starting_familiar": 3,
        "randomize_monsters": 2
    }
    run_default_tests = False
