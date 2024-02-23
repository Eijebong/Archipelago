from worlds.monster_sanctuary import locations as LOCATIONS
from worlds.monster_sanctuary import items as ITEMS
from test.bases import WorldTestBase


class MonsterSanctuaryTestBase(WorldTestBase):
    game = "Monster Sanctuary"
    player: int = 1

    def assert_item_can_be_placed(self, item_name, location_name):
        location_data = LOCATIONS.location_data[location_name]
        with self.subTest(f"{item_name} can be placed at {location_name}"):
            world = self.multiworld.worlds[1]
            item = world.create_item(item_name)
            location = self.multiworld.get_location(location_data.name, 1)

            self.assertTrue(ITEMS.can_item_be_placed(world, item, location))

    def assert_item_can_not_be_placed(self, item_name, location_name):
        location_data = LOCATIONS.location_data[location_name]
        with self.subTest(f"{item_name} can't be placed at {location_name}"):
            world = self.multiworld.worlds[1]
            item = world.create_item(item_name)
            location = self.multiworld.get_location(location_data.name, 1)

            self.assertFalse(ITEMS.can_item_be_placed(world, item, location))

    def assert_location_exists(self, location_name):
        with self.subTest(f"{location_name} exists"):
            self.assertIn(location_name, self.multiworld.regions.location_cache[self.player])

    def assert_location_does_not_exist(self, location_name):
        with self.subTest(f"{location_name} does not exist"):
            self.assertNotIn(location_name, self.multiworld.regions.location_cache[self.player])

