import logging
import os
from .Data import load_json, get_region_data
from .Warps import warps_connect_ltr, get_warp_map, get_warp_region_name


dot_dir = os.path.dirname(__file__)
errors = []
warnings = []
failed = False


def error(message):
    global errors
    global failed
    failed = True
    errors.append(message)


def warn(message):
    global warnings
    warnings.append(message)


def finish():
    global errors
    global warnings
    global failed
    warnings.sort()
    errors.sort()
    for message in warnings:
        logging.warning(message)
    for message in errors:
        logging.error(message)
    logging.debug(f"Sanity check done. Found {len(errors)} errors and {len(warnings)} warnings.")
    return not failed


def load_items():
    return load_json(os.path.join(dot_dir, "data/items.json"))


def check_exits(regions):
    for name, region in regions.items():
        for exit in region.exits:
            if (not exit in regions):
                error(f"Region [{exit}] referenced by [{name}] was not defined")


# Should probably move this to JSON
ignorable_warps = [
    # Secret Bases
    "MAP_SECRET_BASE_BROWN_CAVE1:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_BROWN_CAVE2:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_BROWN_CAVE3:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_BROWN_CAVE4:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_BLUE_CAVE1:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_BLUE_CAVE2:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_BLUE_CAVE3:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_BLUE_CAVE4:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_YELLOW_CAVE1:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_YELLOW_CAVE2:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_YELLOW_CAVE3:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_YELLOW_CAVE4:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_RED_CAVE1:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_RED_CAVE2:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_RED_CAVE3:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_RED_CAVE4:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_SHRUB1:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_SHRUB2:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_SHRUB3:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_SHRUB4:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_TREE1:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_TREE2:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_TREE3:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",
    "MAP_SECRET_BASE_TREE4:0/MAP_DYNAMIC:WARP_ID_SECRET_BASE",

    # Record Corner
    "MAP_RECORD_CORNER:0,1,2,3/MAP_DYNAMIC:WARP_ID_DYNAMIC",

    # Union Room
    "MAP_UNION_ROOM:0,1/MAP_DYNAMIC:WARP_ID_DYNAMIC",
    "MAP_PACIFIDLOG_TOWN_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",
    "MAP_MAUVILLE_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",
    "MAP_PETALBURG_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",
    "MAP_EVER_GRANDE_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",
    "MAP_EVER_GRANDE_CITY_POKEMON_LEAGUE_2F:1/MAP_UNION_ROOM:0",
    "MAP_DEWFORD_TOWN_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",
    "MAP_MOSSDEEP_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",
    "MAP_OLDALE_TOWN_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",
    "MAP_SLATEPORT_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",
    "MAP_RUSTBORO_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",
    "MAP_BATTLE_FRONTIER_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",
    "MAP_LILYCOVE_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",
    "MAP_FORTREE_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",
    "MAP_FALLARBOR_TOWN_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",
    "MAP_LAVARIDGE_TOWN_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",
    "MAP_SOOTOPOLIS_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",
    "MAP_VERDANTURF_TOWN_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0",

    # Trade Center
    "MAP_TRADE_CENTER:0,1/MAP_DYNAMIC:WARP_ID_DYNAMIC",
    "MAP_PACIFIDLOG_TOWN_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",
    "MAP_MAUVILLE_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",
    "MAP_PETALBURG_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",
    "MAP_EVER_GRANDE_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",
    "MAP_EVER_GRANDE_CITY_POKEMON_LEAGUE_2F:2/MAP_TRADE_CENTER:0",
    "MAP_DEWFORD_TOWN_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",
    "MAP_MOSSDEEP_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",
    "MAP_OLDALE_TOWN_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",
    "MAP_SLATEPORT_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",
    "MAP_RUSTBORO_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",
    "MAP_BATTLE_FRONTIER_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",
    "MAP_LILYCOVE_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",
    "MAP_FORTREE_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",
    "MAP_FALLARBOR_TOWN_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",
    "MAP_LAVARIDGE_TOWN_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",
    "MAP_SOOTOPOLIS_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",
    "MAP_VERDANTURF_TOWN_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0",

    # Terra Cave Entrances
    "MAP_TERRA_CAVE_ENTRANCE:0/MAP_DYNAMIC:WARP_ID_DYNAMIC",
    "MAP_ROUTE113:1/MAP_TERRA_CAVE_ENTRANCE:0",
    "MAP_ROUTE113:2/MAP_TERRA_CAVE_ENTRANCE:0",
    "MAP_ROUTE114:3/MAP_TERRA_CAVE_ENTRANCE:0",
    "MAP_ROUTE114:4/MAP_TERRA_CAVE_ENTRANCE:0",
    "MAP_ROUTE115:1/MAP_TERRA_CAVE_ENTRANCE:0",
    "MAP_ROUTE115:2/MAP_TERRA_CAVE_ENTRANCE:0",
    "MAP_ROUTE116:3/MAP_TERRA_CAVE_ENTRANCE:0",
    "MAP_ROUTE116:4/MAP_TERRA_CAVE_ENTRANCE:0",
    "MAP_ROUTE118:0/MAP_TERRA_CAVE_ENTRANCE:0",
    "MAP_ROUTE118:1/MAP_TERRA_CAVE_ENTRANCE:0",

    # Marine Cave Entrances
    "MAP_UNDERWATER_MARINE_CAVE:0/MAP_DYNAMIC:WARP_ID_DYNAMIC",
    "MAP_UNDERWATER_ROUTE105:0/MAP_UNDERWATER_MARINE_CAVE:0",
    "MAP_UNDERWATER_ROUTE105:1/MAP_UNDERWATER_MARINE_CAVE:0",
    "MAP_UNDERWATER_ROUTE125:0/MAP_UNDERWATER_MARINE_CAVE:0",
    "MAP_UNDERWATER_ROUTE125:1/MAP_UNDERWATER_MARINE_CAVE:0",
    "MAP_UNDERWATER_ROUTE127:0/MAP_UNDERWATER_MARINE_CAVE:0",
    "MAP_UNDERWATER_ROUTE127:1/MAP_UNDERWATER_MARINE_CAVE:0",
    "MAP_UNDERWATER_ROUTE129:0/MAP_UNDERWATER_MARINE_CAVE:0",
    "MAP_UNDERWATER_ROUTE129:1/MAP_UNDERWATER_MARINE_CAVE:0",

    # Dept. Store Elevator
    "MAP_LILYCOVE_CITY_DEPARTMENT_STORE_ELEVATOR:0,1/MAP_DYNAMIC:WARP_ID_DYNAMIC",

    # Moving Truck
    "MAP_INSIDE_OF_TRUCK:0,1,2/MAP_DYNAMIC:WARP_ID_DYNAMIC",

    # Battle Frontier Multiplayer
    "MAP_BATTLE_COLOSSEUM_2P:0,1/MAP_DYNAMIC:WARP_ID_DYNAMIC",
    "MAP_BATTLE_COLOSSEUM_4P:0,1,2,3/MAP_DYNAMIC:WARP_ID_DYNAMIC",

    # Unused
    "MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP1:0/MAP_CAVE_OF_ORIGIN_1F:1",
    "MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP1:1/MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP2:0",
    "MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP2:0/MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP1:1",
    "MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP2:1/MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP3:0",
    "MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP3:0/MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP2:1",
    "MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP3:1/MAP_CAVE_OF_ORIGIN_B1F:0",
    "MAP_LILYCOVE_CITY_UNUSED_MART:0,1/MAP_LILYCOVE_CITY:0"
]


def check_warps():
    warp_map = get_warp_map()
    for warp_source, warp_dest in warp_map.items():
        can_ignore = False
        for ignorable_warp in ignorable_warps:
            if (warp_source == ignorable_warp):
                can_ignore = True
        if (can_ignore): continue

        if (warp_dest == None):
            error(f"Warp [{warp_source}] has no destination")
        elif (not warps_connect_ltr(warp_dest, warp_source)):
            warn(f"Warp [{warp_source}] appears to be a one-way warp")
        elif (get_warp_region_name(warp_source) == None):
            warn(f"Warp [{warp_source}] was not claimed by any region")


def sanity_check():
    global failed

    region_data = get_region_data()

    check_exits(region_data)
    check_warps()
    # TODO: Check location claims

    if (failed): return finish()

    return finish()
