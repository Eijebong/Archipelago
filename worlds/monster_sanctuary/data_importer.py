import json
import os
from typing import List, Optional, Dict

from BaseClasses import MultiWorld, ItemClassification
from worlds.monster_sanctuary.items import ItemData, MonsterSanctuaryItemCategory, items_data
from worlds.monster_sanctuary.locations import LocationData, add_chest_data, add_champion_data, add_gift_data, add_flag_data, add_encounter_data
from worlds.monster_sanctuary.regions import RegionData, MonsterSanctuaryConnection, regions_data
from worlds.monster_sanctuary.rules import AccessCondition


def load_world():
    locations_by_id: Dict[int, LocationData] = {}
    location_id: int = 970500

    dir = os.path.dirname(__file__)
    world_file = os.path.join(dir, "data/world.json")

    with open(world_file) as file:
        data = json.load(file)
        for region_data in data:
            region = RegionData(region_data["region"])

            if region_data.get("connections") is None:
                raise SyntaxError(f"Region '{region.name}' has no defined connections")

            for conn_data in region_data.get("connections"):
                requirements = AccessCondition(conn_data.get("requirements"))
                connection = MonsterSanctuaryConnection(conn_data.get("region"), requirements)
                region.connections += [connection]

            region_name: str = region.name
            for chest_data in region_data.get("chests") or []:
                location = add_chest_data(location_id, chest_data, region_name)
                locations_by_id[location_id] = location
                location_id += 1

            for gift_data in region_data.get("gifts") or []:
                # Hack because we store comments as strings
                if isinstance(gift_data, str):
                    continue
                location = add_gift_data(location_id, gift_data, region_name)
                locations_by_id[location_id] = location
                location_id += 1

            for encounter_data in region_data.get("encounters") or []:
                result = add_encounter_data(location_id, encounter_data, region_name)
                locations_by_id.update(result[0])
                location_id = result[1]

            for champion_data in region_data.get("champion") or []:
                result = add_champion_data(location_id, champion_data, region_name)
                locations_by_id.update(result[0])
                location_id = result[1]

            for flag_data in region_data.get("flags") or []:
                location = add_flag_data(location_id, flag_data, region_name)
                locations_by_id[location_id] = location
                location_id += 1

            regions_data[region.name] = region


def load_items():
    item_id: int = 970500

    dir = os.path.dirname(__file__)
    items_file = os.path.join(dir, "data/items.json")
    monsters_file = os.path.join(dir, "data/monsters.json")

    with open(items_file) as file:
        data = json.load(file)
        for item_category_data in data:
            item_category = parse_item_type(item_category_data["type"])
            if item_category is None:
                raise KeyError(f"Item Type '{item_category}' does not match any existing item types")

            default_classification = parse_item_classification(item_category_data.get("classification"))

            for item_data in item_category_data["items"]:
                # Prioritize the item's classification, but fall back to the category's
                # classification. If both are empty, throw an error.
                item_classification = parse_item_classification(item_data.get("classification"))
                if item_classification is None:
                    item_classification = default_classification
                if item_classification is None:
                    raise KeyError(f"Item Classification for item '{item_data['name']}' is missing")

                item = ItemData(
                    item_id,
                    item_data["Name"],
                    item_classification,
                    item_category,
                    item_data.get("tier"),
                    item_data.get("unique") or False,
                    item_data.get("groups")
                )

                items_data[item.name] = item
                item_id += 1

    with open(monsters_file) as file:
        data = json.load(file)

        for monster_data in data:
            monster = ItemData(
                item_id,
                monster_data["Name"],
                ItemClassification.progression_skip_balancing,
                MonsterSanctuaryItemCategory.MONSTER,
                groups=monster_data.get("Groups")
            )

            items_data[monster.name] = monster
            item_id += 1


def parse_item_type(text) -> Optional[MonsterSanctuaryItemCategory]:
    if text == "Rank":
        return MonsterSanctuaryItemCategory.RANK
    elif text == "Key Item":
        return MonsterSanctuaryItemCategory.KEYITEM
    elif text == "Crafting Material":
        return MonsterSanctuaryItemCategory.CRAFTINGMATERIAL
    elif text == "Consumable":
        return MonsterSanctuaryItemCategory.CONSUMABLE
    elif text == "Food":
        return MonsterSanctuaryItemCategory.FOOD
    elif text == "Catalyst":
        return MonsterSanctuaryItemCategory.CATALYST
    elif text == "Weapon":
        return MonsterSanctuaryItemCategory.WEAPON
    elif text == "Accessory":
        return MonsterSanctuaryItemCategory.ACCESSORY
    elif text == "Currency":
        return MonsterSanctuaryItemCategory.CURRENCY
    elif text == "Egg":
        return MonsterSanctuaryItemCategory.EGG
    elif text == "Monster":
        return MonsterSanctuaryItemCategory.MONSTER
    elif text == "Flag":
        return MonsterSanctuaryItemCategory.FLAG
    elif text == "Costume":
        return MonsterSanctuaryItemCategory.COSTUME

    return None


def parse_item_classification(text: Optional[str]) -> Optional[ItemClassification]:
    if text == "filler":
        return ItemClassification.filler
    elif text == "progression":
        return ItemClassification.progression
    elif text == "useful":
        return ItemClassification.useful
    elif text == "trap":
        return ItemClassification.trap
    elif text == "skip_balancing":
        return ItemClassification.skip_balancing
    elif text == "progression_skip_balancing":
        return ItemClassification.progression_skip_balancing

    return None
