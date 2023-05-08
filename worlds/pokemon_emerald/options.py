"""
Option definitions for Pokemon Emerald
"""
from typing import Dict, List, Union

from BaseClasses import MultiWorld
from Options import Choice, DefaultOnToggle, Option, OptionSet, Range, Toggle, FreeText

from .data import data


class RandomizeBadges(Choice):
    """
    Adds Badges to the pool
    Vanilla: Gym leaders give their own badge
    Shuffle: Gym leaders give a random badge
    Completely Random: Badges can be found anywhere
    """
    display_name = "Randomize Badges"
    default = 2
    option_vanilla = 0
    option_shuffle = 1
    option_completely_random = 2


class RandomizeHms(Choice):
    """
    Adds HMs to the pool
    Vanilla: HMs are at their vanilla locations
    Shuffle: HMs are shuffled among vanilla HM locations
    Completely Random: HMs can be found anywhere
    """
    display_name = "Randomize HMs"
    default = 2
    option_vanilla = 0
    option_shuffle = 1
    option_completely_random = 2


class RandomizeKeyItems(DefaultOnToggle):
    """
    Adds most key items to the pool. These are usually required to unlock
    a location or region (e.g. Devon Scope, Letter, Basement Key)
    """
    display_name = "Randomize Key Items"


class RandomizeBikes(Toggle):
    """
    Adds the mach bike and acro bike to the pool
    """
    display_name = "Randomize Bikes"


class RandomizeRods(Toggle):
    """
    Adds fishing rods to the pool
    """
    display_name = "Randomize Fishing Rods"


class RandomizeOverworldItems(DefaultOnToggle):
    """
    Adds items on the ground with a Pokeball sprite to the pool
    """
    display_name = "Randomize Overworld Items"


class RandomizeHiddenItems(Toggle):
    """
    Adds hidden items to the pool
    """
    display_name = "Randomize Hidden Items"


class RandomizeNpcGifts(Toggle):
    """
    Adds most gifts received from NPCs to the pool (not including key items or HMs)
    """
    display_name = "Randomize NPC Gifts"


class ItemPoolType(Choice):
    """
    Determines which non-progression items get put into the item pool
    Shuffled: Item pool consists of shuffled vanilla items
    Diverse Balanced: Item pool consists of random items approximately proportioned according to what they're replacing (i.e. more pokeballs, fewer X items, etc...)
    Diverse: Item pool consists of uniformly random (non-unique) items
    """
    display_name = "Item Pool Type"
    default = 0
    option_shuffled = 0
    option_diverse_balanced = 1
    option_diverse = 2


class HiddenItemsRequireItemfinder(DefaultOnToggle):
    """
    The Itemfinder is logically required to pick up hidden items
    """
    display_name = "Require Itemfinder"


class DarkCavesRequireFlash(DefaultOnToggle):
    """
    The lower floors of Granite Cave and Victory Road logically require use of HM05 Flash
    """
    display_name = "Require Flash"


class EnableFerry(Toggle):
    """
    The ferry between Slateport, Lilycove, and the Battle Frontier can be used if you have the S.S. Ticket
    """
    display_name = "Enable Ferry"


class EliteFourRequirement(Choice):
    """
    Sets the requirements to challenge the elite four
    Badges: Obtain some number of badges
    Gyms: Defeat some number of gyms
    """
    display_name = "Elite Four Requirement"
    default = 0
    option_badges = 0
    option_gyms = 1


class EliteFourCount(Range):
    """
    Sets the number of badges/gyms required to challenge the elite four
    """
    display_name = "Elite Four Count"
    range_start = 0
    range_end = 8
    default = 8


class NormanRequirement(Choice):
    """
    Sets the requirements to challenge the Petalburg Gym
    Badges: Obtain some number of badges
    Gyms: Defeat some number of gyms
    """
    display_name = "Norman Requirement"
    default = 0
    option_badges = 0
    option_gyms = 1


class NormanCount(Range):
    """
    Sets the number of badges/gyms required to challenge the Petalburg Gym
    """
    display_name = "Norman Count"
    range_start = 0
    range_end = 7
    default = 4


class RandomizeWildPokemon(Choice):
    """
    Randomizes wild pokemon encounters (grass, caves, water, fishing)
    Vanilla: Wild encounters are unchanged
    Match Base Stats: Wild pokemon are replaced with species with approximately the same bst
    Match Type: Wild pokemon are replaced with species that share a type with the original
    Match Base Stats and Type: Apply both Match Base Stats and Match Type
    Completely Random: There are no restrictions
    """
    display_name = "Randomize Wild Pokemon"
    default = 0
    option_vanilla = 0
    option_match_base_stats = 1
    option_match_type = 2
    option_match_base_stats_and_type = 3
    option_completely_random = 4


class AllowWildLegendaries(DefaultOnToggle):
    """
    Wild encounters can be replaced by legendaries. Only applied if Randomize Wild Pokemon is not Vanilla.
    """
    display_name = "Allow Wild Legendaries"


class RandomizeStarters(Choice):
    """
    Randomizes the starter pokemon in Professor Birch's bag
    Vanilla: Starters are unchanged
    Match Base Stats: Starters are replaced with species with approximately the same bst
    Match Type: Starters are replaced with species that share a type with the original
    Match Base Stats and Type: Apply both Match Base Stats and Match Type
    Completely Random: There are no restrictions
    """
    display_name = "Randomize Starters"
    default = 0
    option_vanilla = 0
    option_match_base_stats = 1
    option_match_type = 2
    option_match_base_stats_and_type = 3
    option_completely_random = 4


class AllowStarterLegendaries(DefaultOnToggle):
    """
    Starters can be replaced by legendaries. Only applied if Randomize Starters is not Vanilla.
    """
    display_name = "Allow Starter Legendaries"


class RandomizeTrainerParties(Choice):
    """
    Randomizes the parties of all trainers (this will forcibly randomize the moves of pokemon with custom moves like those of gym leaders).
    Vanilla: Parties are unchanged
    Match Base Stats: Trainer pokemon are replaced with species with approximately the same bst
    Match Type: Trainer pokemon are replaced with species that share a type with the original
    Match Base Stats and Type: Apply both Match Base Stats and Match Type
    Completely Random: There are no restrictions
    """
    display_name = "Randomize Trainer Parties"
    default = 0
    option_vanilla = 0
    option_match_base_stats = 1
    option_match_type = 2
    option_match_base_stats_and_type = 3
    option_completely_random = 4


class AllowTrainerLegendaries(DefaultOnToggle):
    """
    Enemy trainer pokemon can be replaced by legendaries. Only applied if Randomize Trainer Parties is not Vanilla.
    """
    display_name = "Allow Trainer Legendaries"


class RandomizeTypes(Toggle):
    """
    Randomizes the types of every pokemon. If a species is dual-typed in vanilla, it will still be dual-typed. Types do not remain consistent across evolutions.
    """
    display_name = "Randomize Types"


class Abilities(Choice):
    """
    Randomizes abilities of every species. Each species will have the same number of abilities.
    Vanilla: Abilities are unchanged
    Randomized: Each species has its abilities randomized
    Follow Evolutions: Abilities are randomized, but if a pokemon would normally retain its ability when evolving, the random ability will also be retained
    """
    display_name = "Abilities"
    default = 0
    option_vanilla = 0
    option_randomized = 1
    option_follow_evolutions = 2


class AbilityBlacklist(OptionSet):
    """
    A list of abilities which no pokemon should have if abilities are randomized. For example, you could exclude Wonder Guard and Pressure like this:
    ["Wonder Guard", "Pressure"]
    """
    display_name = "Ability Blacklist"
    valid_keys = frozenset([ability.label for ability in data.abilities])


class LevelUpMoves(Choice):
    """
    Randomizes the moves a pokemon learns when they reach a level where they would learn a move. Your starter is guaranteed to have a usable damaging move.
    Vanilla: Learnset is unchanged
    Randomized: Moves are randomized
    Start with Four Moves: Moves are randomized and all Pokemon know 4 moves at level 1
    """
    display_name = "Level Up Moves"
    default = 0
    option_vanilla = 0
    option_randomized = 1
    option_start_with_four_moves = 2


class TmMoves(Toggle):
    """
    Randomizes the moves taught by TMs
    """
    display_name = "TM Moves"


class ReusableTms(Toggle):
    """
    Sets TMs to not break after use (they remain sellable)
    """
    display_name = "Reusable TMs"


class TmCompatibility(Choice):
    """
    Modifies the compatability of TMs with species
    Vanilla: Compatibility is unchanged
    Fully Compatible: Every species can learn any TM
    Completely Random: Compatibility is 50/50 for every TM (does not remain consistent across evolution)
    """
    display_name = "TM Compatibility"
    default = 0
    option_vanilla = 0
    option_fully_compatible = 1
    option_completely_random = 2


class HmCompatibility(Choice):
    """
    Modifies the compatability of HMs with species
    Vanilla: Compatibility is unchanged
    Fully Compatible: Every species can learn any HM
    Completely Random: Compatibility is 50/50 for every HM (does not remain consistent across evolution)
    """
    display_name = "HM Compatibility"
    default = 1
    option_vanilla = 0
    option_fully_compatible = 1
    option_completely_random = 2


class MinCatchRate(Range):
    """
    Sets the minimum catch rate a pokemon can have. Any pokemon with a catch rate below this floor will have it raised to this value.
    Legendaries are often in the single digits
    Fully evolved pokemon are often double digits
    Pidgey is 255
    """
    display_name = "Minimum Catch Rate"
    range_start = 3
    range_end = 255
    default = 3


class GuaranteedCatch(Toggle):
    """
    Every throw is guaranteed to catch a wild pokemon
    """
    display_name = "Guaranteed Catch"


class ExpModifier(Range):
    """
    Multiplies gained experience by a percentage
    100 is default
    50 is half
    200 is double
    etc...
    """
    display_name = "Exp Modifier"
    range_start = 0
    range_end = 10000
    default = 100


class BlindTrainers(Toggle):
    """
    Causes trainers to not start a battle with you unless you talk to them
    """
    display_name = "Blind Trainers"


class DoubleBattleChance(Range):
    """
    The percent chance that a trainer with more than 1 pokemon will be converted into a double battle.

    If these trainers would normally approach you, they will only do so if you have 2 unfainted pokemon. They can be battled by talking to them no matter what.
    """
    display_name = "Double Battle Chance"
    range_start = 0
    range_end = 100
    default = 0


class BetterShops(Toggle):
    """
    Pokemarts sell every item that can be obtained in a pokemart (except mail, which is still unique to the relevant city)
    """
    display_name = "Better Shops"


class FlyWithoutBadge(Toggle):
    """
    Fly does not require the Feather Badge to use in the field
    """
    display_name = "Fly Without Badge"


class TurboA(Toggle):
    """
    Holding A will advance most text automatically
    """
    display_name = "Turbo A"


class ReceiveItemMessages(Choice):
    """
    Determines whether you receive an in-game notification when receiving an item. Items can still only be received in the overworld.
    All: Every item shows a message
    Progression: Only progression items show a message
    None: All items are added to your bag silently (badges will still show)
    """
    display_name = "Receive Item Messages"
    default = 0
    option_all = 0
    option_progression = 1
    option_none = 2


class EasterEgg(FreeText):
    """
    ???
    """


option_definitions: Dict[str, Option] = {
  "badges": RandomizeBadges,
  "hms": RandomizeHms,
  "key_items": RandomizeKeyItems,
  "bikes": RandomizeBikes,
  "rods": RandomizeRods,
  "overworld_items": RandomizeOverworldItems,
  "hidden_items": RandomizeHiddenItems,
  "npc_gifts": RandomizeNpcGifts,

  "item_pool_type": ItemPoolType,

  "require_itemfinder": HiddenItemsRequireItemfinder,
  "require_flash": DarkCavesRequireFlash,
  "enable_ferry": EnableFerry,
  "elite_four_requirement": EliteFourRequirement,
  "elite_four_count": EliteFourCount,
  "norman_requirement": NormanRequirement,
  "norman_count": NormanCount,

  "wild_pokemon": RandomizeWildPokemon,
  "allow_wild_legendaries": AllowWildLegendaries,
  "starters": RandomizeStarters,
  "allow_starter_legendaries": AllowStarterLegendaries,
  "trainer_parties": RandomizeTrainerParties,
  "allow_trainer_legendaries": AllowTrainerLegendaries,

  "types": RandomizeTypes,
  "abilities": Abilities,
  "ability_blacklist": AbilityBlacklist,
  "level_up_moves": LevelUpMoves,
  "tm_moves": TmMoves,
  "reusable_tms": ReusableTms,
  "tm_compatibility": TmCompatibility,
  "hm_compatibility": HmCompatibility,

  "min_catch_rate": MinCatchRate,
  "guaranteed_catch": GuaranteedCatch,
  "exp_modifier": ExpModifier,
  "blind_trainers": BlindTrainers,
  "double_battle_chance": DoubleBattleChance,
  "better_shops": BetterShops,
  "fly_without_badge": FlyWithoutBadge,
  "turbo_a": TurboA,
  "receive_item_messages": ReceiveItemMessages,

  "easter_egg": EasterEgg
}


def get_option_value(multiworld: MultiWorld, player: int, option_name: str) -> Union[int, str, Dict, List]:
    """
    Returns the option value for a player in a multiworld
    """
    option = getattr(multiworld, option_name, None)
    if option is None:
        return option_definitions[option_name].default

    return option[player].value
