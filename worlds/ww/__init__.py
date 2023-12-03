from typing import Any, Dict
from .Regions import wind_waker_regions as wwr, mandatory_connections as mc, link_ww_structures
from .Locations import WindWakerAchievement, achievement_table
from .Rules import set_rules as _ww_set_rules, completion_rules as _ww_completion_rules
from .Items import WindWakerItem, item_table
from .Options import wind_waker_options

from BaseClasses import ItemClassification, Region, Entrance, Item, Tutorial
from worlds.AutoWorld import World, WebWorld

from worlds.LauncherComponents import Component, components, Type, SuffixIdentifier, launch_subprocess
from multiprocessing import Process


def run_client():
    print('Running WW Client')
    from .WWClient import main
    launch_subprocess(main, name="WindWakerClient")


components.append(Component('Wind Waker Client', 'WindWakerClient', func=run_client, component_type=Type.CLIENT, file_identifier=SuffixIdentifier('.apww')))


class WindWakerWebWorld(WebWorld):
    theme = "ocean"

    setup = Tutorial(
        "Wind Waker Tutorial",
        "This will help you install Wind Waker via Arch",
        "English",
        "windwaker_en.md",
        "windwaker/en",
        ["Devin Munsey"]

    )

    tutorials = [setup]


class WindWakerWorld(World):
    """
    Wind Waker is an open world game where Link travels by boat.
    The Default Victory is to Beat Ganondorf.
    """
    game: str = "Wind Waker"
    option_definitions = wind_waker_options
    topology_present = True
    remote_items: bool = True

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in achievement_table.items()}

    data_version: int = 237

    web = WindWakerWebWorld()

    def _get_ww_data(self):
        exits = [con[0] for con in mc]
        return {
            'world_seed': self.world.slot_seeds[self.player].getrandbits(32),
            'seed_name': self.world.seed_name,
            'player_name': self.world.get_player_name(self.player),
            'player_id': self.player,
            'structures': {exit: self.world.get_entrance(exit, self.player).connected_region.name for exit in exits},
            'advancement_goal': self.world.advancement_goal[self.player].value,
        }

    def generate_basic(self):
        itempool = []

        for item in item_table:
            the_item = item_table[item]
            for _ in range(the_item.count):
                if the_item.code != None:
                    itempool.append(item)
               
        itempool = [item for item in map(lambda name: self.create_item(name), itempool)]

        self.multiworld.get_location("Victory", self.player).place_locked_item(self.create_item("Defeat Ganon"))

        self.multiworld.completion_condition[self.player] = lambda state: state.has("Defeat Ganon", self.player)

        self.multiworld.itempool += itempool

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]

        if item_data.progression:
            classification = ItemClassification.progression
        else:
            classification = ItemClassification.filler

        item = WindWakerItem(name, classification, item_data.code, self.player)
        return item

    def create_regions(self):
        def WWRegion(name: str, exits=[]):
            ret = Region(name, self.player, self.multiworld)
            ret.locations = [WindWakerAchievement(self.player, loc_name, loc_data.id, ret)
                for loc_name, loc_data in achievement_table.items()
                if loc_data.region == name]
            for exit in exits:
                ret.exits.append(Entrance(self.player, exit, ret))
            return ret
        
        self.multiworld.regions += [WWRegion(*r) for r in wwr]
        link_ww_structures(self.multiworld, self.player)

    def set_rules(self):
        _ww_set_rules(self.multiworld, self.player)
        _ww_completion_rules(self.multiworld, self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            'death_link': self.multiworld.death_link[self.player].value,
        }

