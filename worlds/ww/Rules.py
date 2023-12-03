from BaseClasses import MultiWorld
from worlds.generic.Rules import set_rule
from worlds.AutoWorld import LogicMixin
from BaseClasses import MultiWorld

class WindWakerLogic(LogicMixin):

    def _ww_has_mirror_shield(self, player: int):
        return self.has("Progressive Shield", player, 2)

    def _ww_elemental(self, player: int):
        return self.has("Progressive Bow", player, 2)

    def _ww_can_feed_pig(self, player: int):
        return self.has("Power Bracelets", player) and self.has("Bait Bag", player)

    def _ww_can_defeat_enemies(self, player: int):
        return self.has("Progressive Sword", player) or (self.has("Progressive Bow", player) and self.has("Quiver Upgrade", player)) or \
              (self.has("Bombs", player) and self.has("Bomb Bag Upgrade", player)) or self.has('Skull Hammer', player)

    def _ww_can_defeat_enemies_wo_upgrades(self, player: int):
        return self.has("Progressive Sword", player) or self.has("Progressive Bow", player) or \
               self.has("Bombs", player) or self.has("Skull Hammer", player)

    def _ww_can_do_savage_thirty(self, player: int):
        return self._ww_can_defeat_enemies and (self.has("Hookshot", player) or self.has("Deku Leaf", player)) and \
               self.has("Power Bracelets", player) and self.has("Grappling Hook", player) and \
               self.has("Wind Waker", player) and self.has("Winds Requiem", player)

    def _ww_can_do_savage_fifty(self, player: int):
        return self._ww_can_do_savage_thirty(player) and self._ww_has_mirror_shield(player)

    def _ww_can_remove_rock(self, player: int):
        return self.has("Bombs", player) or self.has("Power Bracelets", player)

    def _ww_can_loot_spoils(self, player: int):
        return self._ww_can_defeat_enemies and self.has("Spoils Bag", player) and self.has("Grappling Hook", player)

    def _ww_get_over_small_gap(self, player: int):
        return self.has("Deku Leaf", player) or self.has("Hookshot", player)

    def _ww_top_boulder(self, player: int):
        return self.has("Bombs", player) or self.has("Progressive Bow", player, 1) or self.has("Boomerang", player) or self.has("Bait Bag", player)

    def _ww_get_into_drc_basement(self, player: int):
        return ((self.has("DRC Small Key", player, 4) and self.has("Progressive Sword", player)) or \
                 self._ww_elemental(player) or self.has("Deku Leaf", player)) and self.has("Grappling Hook", player)

    def _ww_get_into_fw(self, player: int):
        return self.has("Deku Leaf", player) and self.has("Wind Waker", player) and self.has("Winds Requiem", player) and \
               (self.has("Progressive Sword", player, 1) or self.has("Boomerang", player) or self.has("Double Magic", player) or \
                self.has("Bombs", player) or self.has("Skull Hammer", player))

    def _ww_kill_fw_bulbs(self, player: int):
        return self.has("Progressive Bow", player) or self.has("Hookshot", player) or \
               self.has("Bombs", player) or self.has("Boomerang", player)

    def _ww_get_into_tog(self, player: int):
        return self.has("Din's Pearl", player) and self.has("Nayru's Pearl", player) and self.has("Farore's Pearl", player)

    def _ww_destroy_cannons(self, player: int):
        return self.has("Bombs", player) or self.has("Boomerang", player)

    def _ww_defeat_big_octos(self, player: int):
        return (self.has("Progressive Bow", player) or self.has("Bombs", player) or self.has("Boomerang", player)) and self.has("Grappling Hook", player)

    def _ww_hs_sub(self, player: int):
        return self.has("Progressive Sword", player) or self.has("Progressive Bow", player) or self.has("Boomerang", player) or \
               self.has("Skull Hammer", player) or self.has("Grappling Hook", player)

    def _ww_defeat_staflos(self, player: int):
        return self.has("Skull Hammer", player) or self.has("Progressive Bow", player, 3) or \
               self.has("Progressive Sword", player) or self.has("Bombs", player) or self.has("Hookshot", player)

    def _ww_cursed_bubbles(self, player: int):
        return self.has("Progressive Bow", player, 2) or self.has("Bombs", player) or \
               self.has("Deku Leaf", player) or self.has("Hookshot", player)

    def _ww_into_wt(self, player: int):
        return self.has("Iron Boots", player) and self.has("Skull Hammer", player) and \
               self.has("Wind Waker", player) and self.has("Command Melody", player)

    def _ww_withered_trees(self, player: int):
        return self.has("Bottle", player) and self.has("Deku Leaf", player) and (self._ww_hs_sub(player) or \
               self.has("Bombs", player) or self.has("Hookshot", player))

    def _ww_can_beat_ganon(self, player: int):
        return self.has("Progressive Bow", player, 3) and self.has("Progressive Shield", player, 1) and \
               self.has("Grappling Hook", player) and self.has("Hookshot", player) and \
               self.has("Boomerang", player) and self.has("Progressive Sword", player, 4) and self.has("Triforce Shard", player, 8)

    def _ww_wizzrobe_cave1(self, player: int):
        return self.has("Hookshot", player) and (self.has("Skull Hammer", player) or self.has("Progressive Bow", player, 3) or \
               self.has("Progressive Sword", player) or self.has("Bombs", player))

    def _ww_wizzrobe_cave2(self, player: int):
        return ((self.has("Boomerang", player) or self.has("Deku Leaf", player)) and self.has("Progressive Sword", player)) or \
                 self.has("Progressive Bow", player) or self.has("Bombs", player) or self.has("Skull Hammer", player)

    def _ww_cliff_plateau_cave(self, player: int):
        return self.has("Progressive Sword", player) or self.has("Boomerang", player) or self.has("Skull Hammer", player) or self.has("Hookshot", player) or \
               self.has("Bombs", player) or self.has("Progressive Bow", player) or (self.has("Deku Leaf", player) and self.has("Grappling Hook", player))

    def _ww_cliff_upper(self, player: int):
        return self.has("Deku Leaf", player) and (self.has("Progressive Sword", player) or self.has("Boomerang", player) or \
               self.has("Skull Hammer", player) or self.has("Hookshot", player) or self.has("Bombs", player) or \
               self.has("Progressive Bow", player) or self.has("Grappling Hook", player))

    def _ww_fc_sub(self, player: int):
        return (self.has("Progressive Sword", player) or self.has("Progressive Bow", player) or self.has("Bombs", player) or \
                self.has("Skull Hammer", player)) and (self.has("Progressive Bow", player) or self.has("Hookshot", player))


def set_rules(world: MultiWorld, player: int):
    set_rule(world.get_location("Outset - Jabun's Cave", player), lambda state: state.has("Bombs", player))
    set_rule(world.get_location("Outset - Big Pig", player), lambda state: state._ww_can_feed_pig(player))
    set_rule(world.get_location("Outset - Savage Labryinth Floor 30", player), lambda state: state._ww_can_do_savage_thirty(player))
    set_rule(world.get_location("Outset - Savage Labryinth Floor 50", player), lambda state: state._ww_can_do_savage_fifty(player))
    set_rule(world.get_location("Outset - Give Orca 10 Knights Crest", player), lambda state: state._ww_can_loot_spoils(player) and (state.has("Triforce Shard", player, 8) or (state.has("Iron Boots", player) and \
                                                                                              state.has("Skull Hammer", player)) or (state.has("Wind Waker", player) and state.has("Winds Reqium", player) and \
                                                                                             (state.has("Hookshot", player) or state.has("Power Bracelets", player)))) and state.has("Progressive Sword", player))

    set_rule(world.get_entrance("Windfall - Potion Shop Entrance", player), lambda state: state._ww_can_loot_spoils(player))
    set_rule(world.get_entrance("Windfall - Lenzo Upper Entrance", player), lambda state: state.has("Progressive Picto Box", player))
    set_rule(world.get_location("Windfall - Light the Lighthouse", player), lambda state: state._ww_elemental(player))
    set_rule(world.get_location("Windfall - Transparent Chest", player), lambda state: state._ww_elemental(player) and state._ww_get_over_small_gap(player))

    set_rule(world.get_location("DRI - Wind Shrine", player), lambda state: state.has("Wind Waker", player))
    set_rule(world.get_location("DRI - Top of Boulder", player), lambda state: state._ww_top_boulder(player))
    set_rule(world.get_entrance("Fly Around Island Entrance", player), lambda state: state.has("Deku Leaf", player) and state.has("Wind Waker", player) and state.has("Winds Requiem", player) and \
                                                                                     (state.has("Progressive Sword", player, 1) or state.has("Bombs", player) or state.has("Skull Hammer", player) or \
                                                                                      state.has("Boomerang", player) or state.has("Double Magic", player)))
    set_rule(world.get_location("DRI - Secret Cave", player), lambda state: state._ww_can_remove_rock(player) and state._ww_can_defeat_enemies(player))

    set_rule(world.get_entrance("DRC - HUB Room Entrance", player), lambda state: state.has("DRC Small Key", player))
    set_rule(world.get_entrance("DRC - 1st Locked Door", player), lambda state: state.has("DRC Small Key", player, 2)),
    set_rule(world.get_location("DRC - Across Lava Pit", player), lambda state: state._ww_get_over_small_gap(player) or state.has("Grappling Hook", player))
    set_rule(world.get_entrance("DRC - Rat Room Locked Door", player), lambda state: state.has("DRC Small Key", player, 3))
    set_rule(world.get_entrance("DRC - Into Dark Room", player), lambda state: state.has("DRC Small Key", player, 4))
    set_rule(world.get_location("DRC - Tingle Chest in DRC HUB", player), lambda state: state.has("Bombs", player))
    set_rule(world.get_entrance("DRC - Basement Entrance", player), lambda state: state._ww_get_into_drc_basement(player))
    set_rule(world.get_location("DRC - Under Bridge", player), lambda state: state.has("Grappling Hook", player) or (state.has("Deku Leaf", player) and \
                                                                             state.has("Wind Waker", player) and state.has("Winds Requiem", player)))
    set_rule(world.get_location("DRC - Tingle Chest in DRC Basement", player), lambda state: state.has("Bombs", player))
    set_rule(world.get_location("DRC - Outside Boss Door Left", player), lambda state: state._ww_get_over_small_gap(player) or state.has("Grappling Hook", player))
    set_rule(world.get_location("DRC - Outside Boss Door Right", player), lambda state: state._ww_get_over_small_gap(player) or state.has("Grappling Hook", player))
    set_rule(world.get_location("DRC - Gohma Heart Container", player), lambda state: state.has("DRC Big Key", player) and state.has("Grappling Hook", player))

    set_rule(world.get_entrance("Forest Haven Entrance", player), lambda state: state.has("Grappling Hook", player))
    set_rule(world.get_location("Forest Haven - On Small Island", player), lambda state: state.has("Grappling Hook", player) and state.has("Deku Leaf", player) and \
                                                                                         state.has("Winds Requiem", player) and state.has("Wind Waker", player))

    set_rule(world.get_entrance("Forbidden Woods Entrance", player), lambda state: state._ww_get_into_fw(player))
    set_rule(world.get_location("Forbidden Woods - Climb to Top", player), lambda state: state._ww_kill_fw_bulbs(player))
    set_rule(world.get_entrance("Forbidden Woods - Locked Door", player), lambda state: state.has("FW Small Key", player))
    set_rule(world.get_location("Forbidden Woods - Mini-Boss", player), lambda state: state._ww_can_defeat_enemies(player))
    set_rule(world.get_location("Forbidden Woods - Past Hanging Vines", player), lambda state: state._ww_kill_fw_bulbs(player))
    set_rule(world.get_entrance("Forbidden Woods - Basement Entrance", player), lambda state: state.has("Boomerang", player))
    set_rule(world.get_location("Forbidden Woods - Tingle Chest", player), lambda state: state.has("Bombs", player))
    set_rule(world.get_location("Forbidden Woods - Double Mothula", player), lambda state: state._ww_kill_fw_bulbs(player))
    set_rule(world.get_location("Forbidden Woods - Kalle Demos Heart Container", player), lambda state: state.has("Boomerang", player) and state._ww_can_defeat_enemies(player) and state.has("FW Big Key", player))

    set_rule(world.get_location("Greatfish - Hidden Chest", player), lambda state: state.has("Deku Leaf", player))
    
    set_rule(world.get_entrance("Tower of Gods Entrance", player), lambda state: state._ww_get_into_tog(player))
    set_rule(world.get_entrance("Tower of Gods - Left Side Entrance", player), lambda state: state.has("Bombs", player))
    set_rule(world.get_location("Tower of Gods - Skull Room Shoot The Eye", player), lambda state: state.has("Progressive Bow", player))
    set_rule(world.get_location("Tower of Gods - Behind Bombable Wall", player), lambda state: state.has("Bombs", player))
    set_rule(world.get_entrance("Tower of Gods - Until Stone Tablet Entrance", player), lambda state: state.has("TotG Small Key", player) and state.has("Bombs", player))
    set_rule(world.get_location("Tower of Gods - First Chest Guarded", player), lambda state: state.has("Progressive Bow", player))
    set_rule(world.get_location("Tower of Gods - Stone Tablet", player), lambda state: state.has("Wind Waker", player))
    set_rule(world.get_entrance("Tower of Gods - Mini Boss Arena Entrance", player), lambda state: (state.has("Deku Leaf", player) or state.has("Grappling Hook", player)) and \
                                                                                                    state.has("Command Melody", player) and state.has("Wind Waker", player))
    set_rule(world.get_entrance("Tower of Gods - After Mini Boss", player), lambda state: state.has("Progressive Bow", player))
    set_rule(world.get_location("Tower of Gods - Second Chest Guarded", player), lambda state: state.has("Winds Requiem", player))
    set_rule(world.get_entrance("Tower of Gods - Locked Door", player), lambda state: state.has("TotG Small Key", player, 2))
    set_rule(world.get_location("Tower of Gods - Big Key Chest", player), lambda state: state.has("Deku Leaf", player))
    set_rule(world.get_location("Tower of Gods - Gohdan Heart Container", player), lambda state: state.has("TotG Big Key", player) and state.has("Deku Leaf", player))

    set_rule(world.get_entrance("Hyrule Entrance", player), lambda state: state.has("Triforce Shard", player, 8))
    set_rule(world.get_location("Hyrule - Master Sword Chamber", player), lambda state: state._ww_can_defeat_enemies(player))

    set_rule(world.get_entrance("Forsaken Fortress Interior Entrance", player), lambda state: state.has("Bombs", player))
    set_rule(world.get_location("Forsaken Fortress - Phantom Ganon", player), lambda state: state.has("Progressive Sword", player, 2))
    set_rule(world.get_entrance("Forsaken Fortress - Within the Walls Entrance", player), lambda state: state.has("Skull Hammer", player))
    set_rule(world.get_location("Forsaken Fortress - Helmaroc King Heart Container", player), lambda state: state.has("Deku Leaf", player) or state.has("Hookshot", player))

    set_rule(world.get_entrance("Mother & Child Warp Point", player), lambda state: state.has("Wind Waker", player) and state.has("Ballad of the Gales", player))

    set_rule(world.get_location("Fire Mountain - Cave", player), lambda state: state.has("Progressive Bow", player, 2))
    set_rule(world.get_location("Fire Mountain - Cannon Platform", player), lambda state: state._ww_destroy_cannons(player))
    #set_rule(world.get_location("Fire Mountain - Big Octo", player), lambda state: state._ww_defeat_big_octos(player))

    set_rule(world.get_entrance("Ice Ring Cave Entrance", player), lambda state: state.has("Progressive Bow", player, 2))
    set_rule(world.get_entrance("Ice Ring Inner Cave Entrance", player), lambda state: state.has("Iron Boots", player))

    set_rule(world.get_location("Headstone Island - Top of Island", player), lambda state: state.has("Bait Bag", player))
    set_rule(world.get_location("Headstone Island - Submarine", player), lambda state: state._ww_hs_sub(player))

    set_rule(world.get_entrance("Headstone Island Entrance", player), lambda state: state.has("Power Bracelets", player) and state.has("Command Melody", player) and state.has("Wind Waker", player))
    set_rule(world.get_location("Earth Temple - Transparent Chest in 1st Crypt", player), lambda state: state.has("Skull Hammer", player))
    set_rule(world.get_location("Earth Temple - Behind Destructable Walls", player), lambda state: state.has("Progressive Shield", player, 2) and state.has("Skull Hammer", player))
    set_rule(world.get_entrance("Earth Temple - Left Side Entrance", player), lambda state: state.has("ET Small Key", player, 2) and state.has("Progressive Bow", player, 2))
    set_rule(world.get_location("Earth Temple - Staflos Mini Boss", player), lambda state: state.has("ET Small Key", player, 3) and state._ww_defeat_staflos(player))
    set_rule(world.get_entrance("Earth Temple - Basement Entrance", player), lambda state: state.has("Progressive Shield", player, 2))
    set_rule(world.get_location("Earth Temple - Tingle Chest", player), lambda state: state.has("Bombs", player))
    set_rule(world.get_entrance("Earth Temple - Song Stone", player), lambda state: state.has("Earth God's Lyrics", player))
    set_rule(world.get_location("Earth Temple - Floormaster Room Fight", player), lambda state: state.has("Progressive Bow", player) or state.has("Progressive Sword", player))
    set_rule(world.get_entrance("Earth Temple - 2nd Locked Door", player), lambda state: state.has("ET Small Key", player, 3) and state.has("Skull Hammer", player))
    set_rule(world.get_location("Earth Temple - Big Key Chest", player), lambda state: state._ww_cursed_bubbles(player))
    set_rule(world.get_entrance("Earth Temple - Boss Arena Entrance", player), lambda state: state.has("ET Big Key", player))

    set_rule(world.get_entrance("Gale Isle Entrance", player), lambda state: state._ww_into_wt(player))
    set_rule(world.get_entrance("Wind Temple - HUB Room Entrance", player), lambda state: state.has("Deku Leaf", player))
    set_rule(world.get_location("Wind Temple - Tingle Chest", player), lambda state: state.has("Bombs", player))
    set_rule(world.get_location("Wind Temple - Behind Stone Head", player), lambda state: state.has("Hookshot", player))
    set_rule(world.get_location("Wind Temple - Big Key Chest", player), lambda state: state.has("Wind God's Aria", player))
    set_rule(world.get_location("Wind Temple - Wizzrobe Mini Boss", player), lambda state: state.has("WT Small Key", player, 2))
    set_rule(world.get_entrance("Wind Temple - Basement Entrance", player), lambda state: state.has("WT Small Key", player, 2) and state.has("Hookshot", player))
    set_rule(world.get_entrance("Wind Temple - Boss Arena Entrance", player), lambda state: state.has("WT Big Key", player) and state.has("Wind God's Aria", player))

    set_rule(world.get_entrance("Ganons Tower Entrance", player), lambda state: state.has("Progressive Sword", player, 4) and (state.has("Deku Leaf", player) or state.has("Hookshot", player)))

    set_rule(world.get_location("Great Sea - Defeat Cyclos", player), lambda state: state.has("Progressive Bow", player))
    set_rule(world.get_location("Great Sea - Withered Trees", player), lambda state: state._ww_withered_trees(player))
    set_rule(world.get_location("Great Sea - Ghost Ship", player), lambda state: state.has("Ghost Ship Chart", player) and state.has("Deku Leaf", player) and state._ww_can_defeat_enemies(player))

    set_rule(world.get_location("Private Oasis - Top of Waterfall", player), lambda state: state._ww_get_over_small_gap(player))
    set_rule(world.get_entrance("Cabana Labryinth Entrance", player), lambda state: state.has("Delivery Bag", player) and state.has("Cabana Deed", player) and \
                                                                                    state.has("Grappling Hook", player) and state.has("Skull Hammer", player))
    #set_rule(world.get_location("Private Oasis - Big Octo", player), lambda state: state._ww_defeat_big_octos(player))
    set_rule(world.get_location("Cabana Labryinth - Upper", player), lambda state: state.has("Wind Waker", player) and state.has("Winds Requiem", player))

    set_rule(world.get_location("Needle Rock - Chest in Ring of Fire", player), lambda state: state.has("Bait Bag", player))
    set_rule(world.get_entrance("Needle Rock Cave Entrance", player), lambda state: state.has("Progressive Bow", player, 2))
    #set_rule(world.get_location("Needle Rock - Golden Gunboat", player), lambda state: state.has("Bombs", player) and state.has("Grappling Hook", player))

    set_rule(world.get_location("Angular - Cave", player), lambda state: state.has("Progressive Shield", player, 2) and (state.has("Hookshot", player) or state.has("Deku Leaf", player)))

    set_rule(world.get_location("Boating Course - Cave", player), lambda state: state._ww_get_over_small_gap(player) and (state._ww_can_defeat_enemies(player) or state.has("Boomerang", player)) and \
                                                                               (state.has("Boomerang", player) or state.has("Hookshot", player) or state.has("Progressive Bow", player)))

    set_rule(world.get_location("Stone Watcher - Cave", player), lambda state: state.has("Power Bracelets", player) and state.has("Wind Waker", player) and state.has("Winds Requiem", player) and \
                                                                              (state.has("Progressive Sword", player) or state.has("Progressive Bow", player, 3) or state.has("Skull Hammer", player)))
    set_rule(world.get_location("Stone Watcher - Cannon Platform", player), lambda state: state._ww_destroy_cannons(player))

    set_rule(world.get_location("Islet of Steel - Cave", player), lambda state: state.has("Wind Waker", player) and state.has("Winds Requiem", player) and state.has("Bombs", player))
    set_rule(world.get_location("Islet of Steel - Enemy Platform", player), lambda state: state.has("Progressive Bow", player) or state.has("Hookshot", player))
    
    set_rule(world.get_location("Overlook - Cave", player), lambda state: state.has("Hookshot", player) and (state.has("Progressive Sword", player) or state.has("Progressive Bow", player, 3) or \
                                                                          state.has("Skull Hammer", player)) and state.has("Wind Waker", player) and state.has("Winds Requiem", player))

    set_rule(world.get_location("Birds Peak Rock - Cave", player), lambda state: state.has("Bait Bag", player) and state.has("Wind Waker", player) and state.has("Winds Requiem", player))

    set_rule(world.get_location("Pawprint - Chu Cave - Left Boulder", player), lambda state: state.has("Bombs", player) or state.has("Power Bracelets", player))
    set_rule(world.get_location("Pawprint - Chu Cave - Right Boulder", player), lambda state: state.has("Bombs", player) or state.has("Power Bracelets", player))
    set_rule(world.get_location("Pawprint - Chu Cave - Scale Wall", player), lambda state: state.has("Grappling Hook", player))
    set_rule(world.get_location("Pawprint - Wizzrobe Cave", player), lambda state: state._ww_wizzrobe_cave1(player) and state._ww_wizzrobe_cave2(player))

    set_rule(world.get_location("Thorned Fairy - Cannon Platform", player), lambda state: state._ww_destroy_cannons(player))
    set_rule(world.get_location("Thorned Fairy - Enemy Platform", player), lambda state: state.has("Deku Leaf", player))
    set_rule(world.get_location("Eastern Fairy - Cannon Platform", player), lambda state: state._ww_destroy_cannons(player))
    set_rule(world.get_location("Southern Fairy - NW Cannon Platform", player), lambda state: state._ww_destroy_cannons(player) and state.has("Deku Leaf", player))
    set_rule(world.get_location("Southern Fairy - SE Cannon Platform", player), lambda state: state._ww_destroy_cannons(player) and state.has("Deku Leaf", player))

    #set_rule(world.get_location("Tingle Island - Big Octo", player), lambda state: (state.has("Bombs", player) or state.has("Boomerang", player) or state.has("Progressive Bow", player, 3) or \
    #                                                                       (state.has("Progressive Bow", player) and state.has("Quiver Upgrade", player))) and state.has("Grappling Hook", player))

    set_rule(world.get_entrance("Diamond Steppe Cave Entrance", player), lambda state: state.has("Hookshot", player))
    #set_rule(world.get_location("Diamond Steppe - Big Octo", player), lambda state: state._ww_defeat_big_octos(player))

    set_rule(world.get_location("Bomb Island - Cave", player), lambda state: (state._ww_hs_sub(player) or state.has("Bombs", player) or state.has("Hookshot", player)) and \
                                                                             (state.has("Bombs", player) or state.has("Power Bracelets", player)))

    set_rule(world.get_location("Rock Spire - Cave", player), lambda state: state.has("Bombs", player))
    set_rule(world.get_entrance("Expensive Beedle Ship Entrance", player), lambda state: state.has("Wallet Upgrade", player))
    set_rule(world.get_location("Rock Spire - Western Cannon Platform", player), lambda state: state._ww_destroy_cannons(player) and state.has("Deku Leaf", player))
    set_rule(world.get_location("Rock Spire - Eastern Cannon Platform", player), lambda state: state._ww_destroy_cannons(player) and state.has("Deku Leaf", player))
    #set_rule(world.get_location("Rock Spire - Southeast Gunboat", player), lambda state: state.has("Bombs", player) and state.has("Grappling Hook", player))

    set_rule(world.get_location("Shark Island - Cave", player), lambda state: state.has("Iron Boots", player) and state.has("Skull Hammer", player))

    set_rule(world.get_location("Cliff Plateau - Cave", player), lambda state: state._ww_cliff_plateau_cave(player))
    set_rule(world.get_location("Cliff Plateau - Upper", player), lambda state: state._ww_cliff_upper(player))

    set_rule(world.get_location("Crescent Moon - Submarine", player), lambda state: state._ww_hs_sub(player) or state.has("Bombs", player))

    set_rule(world.get_location("Horseshoe - Play Golf", player), lambda state: state.has("Deku Leaf", player))
    set_rule(world.get_location("Horseshoe - Cave", player), lambda state: state._ww_can_defeat_enemies_wo_upgrades(player) and state.has("Deku Leaf", player))

    set_rule(world.get_location("Flight Control - Submarine", player), lambda state: state._ww_fc_sub(player))

    set_rule(world.get_location("Star Island - Cave", player), lambda state: state._ww_can_remove_rock(player) and (state._ww_hs_sub(player) or state.has("Bombs", player) or state.has("Grappling Hook", player)))

    set_rule(world.get_location("5 Star - Cannon Platform", player), lambda state: state._ww_destroy_cannons(player))
    set_rule(world.get_location("7 Star - Southern Platform", player), lambda state: state.has("Progressive Bow", player) or state.has("Hookshot", player))
    #set_rule(world.get_location("7 Star - Big Octo", player), lambda state: (state.has("Bombs", player) or state.has("Boomerang", player) or state.has("Progressive Bow", player, 3) or \
    #                                                                        (state.has("Progressive Bow", player) and state.has("Quiver Upgrade", player))) and state.has("Grappling Hook", player))

    set_rule(world.get_location("1 Eye Reef - Top of Eye", player), lambda state: state.has("Bombs", player) and state.has("Deku Leaf", player))
    set_rule(world.get_location("2 Eye Reef - Top of Eye", player), lambda state: state.has("Bombs", player) and state.has("Deku Leaf", player))
    set_rule(world.get_location("2 Eye Reef - Big Octo Fairy", player), lambda state: state.has("Progressive Bow", player) or state.has("Boomerang", player) or state.has("Bombs", player))
    set_rule(world.get_location("3 Eye Reef - Top of Eye", player), lambda state: state.has("Bombs", player) and state.has("Deku Leaf", player))
    set_rule(world.get_location("4 Eye Reef - Top of Eye", player), lambda state: state.has("Bombs", player) and state.has("Deku Leaf", player))
    set_rule(world.get_location("5 Eye Reef - Top of Eye", player), lambda state: state.has("Bombs", player) and state.has("Deku Leaf", player))
    set_rule(world.get_location("6 Eye Reef - Top of Eye", player), lambda state: state.has("Bombs", player) and state.has("Deku Leaf", player))
    set_rule(world.get_location("6 Eye Reef - Cannon Platform", player), lambda state: state._ww_destroy_cannons(player))

    set_rule(world.get_location("Treasure Chart 1 Salvage", player), lambda state: state.has("Treasure Chart 1", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 2 Salvage", player), lambda state: state.has("Treasure Chart 2", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 3 Salvage", player), lambda state: state.has("Treasure Chart 3", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 4 Salvage", player), lambda state: state.has("Treasure Chart 4", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 5 Salvage", player), lambda state: state.has("Treasure Chart 5", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 6 Salvage", player), lambda state: state.has("Treasure Chart 6", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 7 Salvage", player), lambda state: state.has("Treasure Chart 7", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 8 Salvage", player), lambda state: state.has("Treasure Chart 8", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 9 Salvage", player), lambda state: state.has("Treasure Chart 9", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 10 Salvage", player), lambda state: state.has("Treasure Chart 10", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 11 Salvage", player), lambda state: state.has("Treasure Chart 11", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 12 Salvage", player), lambda state: state.has("Treasure Chart 12", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 13 Salvage", player), lambda state: state.has("Treasure Chart 13", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 14 Salvage", player), lambda state: state.has("Treasure Chart 14", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 15 Salvage", player), lambda state: state.has("Treasure Chart 15", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 16 Salvage", player), lambda state: state.has("Treasure Chart 16", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 17 Salvage", player), lambda state: state.has("Treasure Chart 17", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 18 Salvage", player), lambda state: state.has("Treasure Chart 18", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 19 Salvage", player), lambda state: state.has("Treasure Chart 19", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 20 Salvage", player), lambda state: state.has("Treasure Chart 20", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 21 Salvage", player), lambda state: state.has("Treasure Chart 21", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 22 Salvage", player), lambda state: state.has("Treasure Chart 22", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 23 Salvage", player), lambda state: state.has("Treasure Chart 23", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 24 Salvage", player), lambda state: state.has("Treasure Chart 24", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 25 Salvage", player), lambda state: state.has("Treasure Chart 25", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 26 Salvage", player), lambda state: state.has("Treasure Chart 26", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 27 Salvage", player), lambda state: state.has("Treasure Chart 27", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 28 Salvage", player), lambda state: state.has("Treasure Chart 28", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 29 Salvage", player), lambda state: state.has("Treasure Chart 29", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 30 Salvage", player), lambda state: state.has("Treasure Chart 30", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 31 Salvage", player), lambda state: state.has("Treasure Chart 31", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 32 Salvage", player), lambda state: state.has("Treasure Chart 32", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 33 Salvage", player), lambda state: state.has("Treasure Chart 33", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 34 Salvage", player), lambda state: state.has("Treasure Chart 34", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 35 Salvage", player), lambda state: state.has("Treasure Chart 35", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 36 Salvage", player), lambda state: state.has("Treasure Chart 36", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 37 Salvage", player), lambda state: state.has("Treasure Chart 37", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 38 Salvage", player), lambda state: state.has("Treasure Chart 38", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 39 Salvage", player), lambda state: state.has("Treasure Chart 39", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 40 Salvage", player), lambda state: state.has("Treasure Chart 40", player) and state.has("Grappling Hook", player))
    set_rule(world.get_location("Treasure Chart 41 Salvage", player), lambda state: state.has("Treasure Chart 41", player) and state.has("Grappling Hook", player))

    set_rule(world.get_location("Triforce Chart 1 Salvage", player), lambda state: state.has("Triforce Chart 1", player) and state.has("Grappling Hook", player) and state.has("Wallet Upgrade", player))
    set_rule(world.get_location("Triforce Chart 2 Salvage", player), lambda state: state.has("Triforce Chart 2", player) and state.has("Grappling Hook", player) and state.has("Wallet Upgrade", player))
    set_rule(world.get_location("Triforce Chart 3 Salvage", player), lambda state: state.has("Triforce Chart 3", player) and state.has("Grappling Hook", player) and state.has("Wallet Upgrade", player))
    set_rule(world.get_location("Triforce Chart 4 Salvage", player), lambda state: state.has("Triforce Chart 4", player) and state.has("Grappling Hook", player) and state.has("Wallet Upgrade", player))
    set_rule(world.get_location("Triforce Chart 5 Salvage", player), lambda state: state.has("Triforce Chart 5", player) and state.has("Grappling Hook", player) and state.has("Wallet Upgrade", player))
    set_rule(world.get_location("Triforce Chart 6 Salvage", player), lambda state: state.has("Triforce Chart 6", player) and state.has("Grappling Hook", player) and state.has("Wallet Upgrade", player))
    set_rule(world.get_location("Triforce Chart 7 Salvage", player), lambda state: state.has("Triforce Chart 7", player) and state.has("Grappling Hook", player) and state.has("Wallet Upgrade", player))
    set_rule(world.get_location("Triforce Chart 8 Salvage", player), lambda state: state.has("Triforce Chart 8", player) and state.has("Grappling Hook", player) and state.has("Wallet Upgrade", player))
    
    set_rule(world.get_location("Victory", player), lambda state: state._ww_can_beat_ganon(player))

def completion_rules(world: MultiWorld, player: int):
    requirements = lambda state: state._ww_can_beat_ganon(player)
    world.completion_condition[player] = lambda state: requirements(state)
