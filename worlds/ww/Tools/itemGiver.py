from ..inc.packages import dolphin_memory_engine as dme
from .give_and_take_items import *
import asyncio
from ..Items import lookup_id_to_name as item_id_to_name
from .itemTable import item_table as IT

async def ww_item_giver(ctx):
    dme.hook()
    print(ctx.send_index, len(ctx.items_received))
    while not ctx.exit_event.is_set():
       #print("Item Giver")
        while(ctx.send_index < len(ctx.items_received)):
            while ((ctx.send_index < len(ctx.items_received)) and can_be_given()):
                for x in range(ctx.send_index, len(ctx.items_received)):
                    value = dme.read_word(0x803C50B8)
                    value >>= 8
                    value <<= 8
                    value += ctx.send_index+1
                    dme.write_word(0x803C50B8, value)          
                    name: str = item_id_to_name[ctx.items_received[x].item]
                    
                    found: bool = False
                    for item in IT:
                        if name == item.name:
                            give_item_name(name)
                            ctx.send_index += 1
                            found = True
                            continue
                    if found == True:
                        continue

                    if name[9:14] == "Chart":
                        if name[2] == "i":
                            give_triforce_chart(int(name[15:len(name)]))
                            ctx.send_index += 1
                            continue
                        elif name[2] == "e":
                            give_treasure_chart(int(name[15:len(name)]))
                            ctx.send_index += 1
                            continue
                    if name[-5:] == "Pearl":
                        give_pearl(name)
                        ctx.send_index += 1
                        continue
                    if name[:5] == "Heart":
                        if name[6] == "P":
                            give_heart_piece()
                            ctx.send_index += 1
                            continue
                        if name[6] == "C":
                            give_heart_container()
                            ctx.send_index += 1
                            continue
                    if name == "Progressive Picto Box":
                        give_next_picto()
                        ctx.send_index += 1
                        continue
                    if name == "Progressive Sword":
                        give_next_sword()
                        ctx.send_index += 1
                        continue
                    if name == "Progressive Bow":
                        give_next_bow()
                        ctx.send_index += 1
                        continue
                    if name == "Progressive Shield":
                        give_next_shield()
                        ctx.send_index += 1
                        continue
                    if name == "Triforce Shard":
                        give_next_shard()
                        ctx.send_index += 1
                        continue
                    if name == "Wallet Upgrade":
                        give_next_wallet()
                        ctx.send_index += 1
                        continue
                    if name == "Quiver Upgrade":
                        give_quiver()
                        ctx.send_index += 1
                        continue
                    if name == "Bomb Bag Upgrade":
                        give_bomb_bag()
                        ctx.send_index += 1
                        continue
                    if name == "Bottle":
                        give_next_bottle()
                        ctx.send_index += 1
                        continue
                    if name == "Power Bracelets":
                        power_bracelet()
                        ctx.send_index += 1
                        continue
                    if name == "Heros Charm":
                        give_hero_charm()
                        ctx.send_index += 1
                        continue
                    if name == "Double Magic":
                        double_magic()
                        ctx.send_index += 1
                        continue

                    #SONGS
                    if name == "Winds Requiem":
                        give_link_song(0)
                        ctx.send_index += 1
                        continue
                    if name == "Ballad of the Gales":
                        give_link_song(1)
                        ctx.send_index += 1
                        continue
                    if name == "Command Melody":
                        give_link_song(2)
                        ctx.send_index += 1
                        continue
                    if name == "Earth God's Lyrics":
                        give_link_song(3)
                        ctx.send_index += 1
                        continue
                    if name == "Wind God's Aria":
                        give_link_song(4)
                        ctx.send_index += 1
                        continue
                    if name == "Song of Passing":
                        give_link_song(5)
                        ctx.send_index += 1
                        continue

                    #LETTERS
                    if name == "Note to Mom" or name == "Cabana Deed" or \
                        name == "Maggies Letter" or name == "Moblins Letter":
                        give_letter(name)
                        ctx.send_index += 1
                        continue

                    #MONEY
                    if name == "Tingle Reward":
                        give_link_rupees(500)
                        ctx.send_index += 1
                        continue

                    if name[-5:] == "Rupee":
                        amount: int = 0
                        if name[0] == "G":
                            amount = 1
                        elif name[0] == "B":
                            amount = 5
                        elif name[0] == "Y":
                            amount = 10
                        elif name[0] == "R":
                            amount = 20
                        elif name[0] == "P":
                            amount = 50
                        elif name[0] == "O":
                            amount = 100
                        elif name[0] == "S":
                            amount = 200
                        give_link_rupees(amount)
                        ctx.send_index += 1
                        continue

                    #DUNGEON ITEMS
                    if name[:3] == "DRC":
                        if name[4] == "C":
                            give_drc_comp()
                        elif name[4] == "M":
                            give_drc_map()
                        elif name[4] == "B":
                            give_drc_bk()
                        else:
                            give_drc_sk()
                        ctx.send_index += 1
                        continue

                    if name[:2] == "FW":
                        if name[3] == "C":
                            give_fw_comp()
                        elif name[3] == "M":
                            give_fw_map()
                        elif name[3] == "B":
                            give_fw_bk()
                        else:
                            give_fw_sk()
                        ctx.send_index += 1
                        continue
            
                    if name[:4] == "TotG":
                        if name[5] == "C":
                            give_totg_comp()
                        elif name[5] == "M":
                            give_totg_map()
                        elif name[5] == "B":
                            give_totg_bk()
                        else:
                            give_totg_sk()
                        ctx.send_index += 1
                        continue

                    if name[:2] == "FF":
                        if name[3] == "C":
                            give_ff_comp()
                        else:
                            give_ff_map()
                        ctx.send_index += 1
                        continue
            
                    if name[:2] == "ET":
                        if name[3] == "C":
                            give_et_comp()
                        elif name[3] == "M":
                            give_et_map()
                        elif name[3] == "B":
                            give_et_bk()
                        else:
                            give_et_sk()
                        ctx.send_index += 1
                        continue

                    if name[:2] == "WT":
                        if name[3] == "C":
                            give_wt_comp()
                        elif name[3] == "M":
                            give_wt_map()
                        elif name[3] == "B":
                            give_wt_bk()
                        else:
                            give_wt_sk()
                        ctx.send_index += 1
                        continue

                    if name == "Ghost Ship Chart":
                        give_ghost_ship()
                        ctx.send_index += 1
                        continue

                    if name != "Defeat Ganon":
                        give_spoil(name)
                        ctx.send_index += 1
                        continue

                    #Defeat Ganon (Victory)
                await asyncio.sleep(3)
        await asyncio.sleep(3)

