import asyncio
from ..inc.packages import dolphin_memory_engine as dme
from .give_and_take_items import *
from ..Items import lookup_id_to_name
from .itemTable import item_table as IT, treasure_charts as TC, spoils, songs, letters

async def item_checker(ctx):
    while(not ctx.exit_event.is_set()):
        dme.hook()
        while(can_be_given() and not ctx.exit_event.is_set()):
            items_by_name = [lookup_id_to_name[x.item] for x in ctx.items_received][:]
            items_by_name.sort()
            for item in items_by_name:
                #Items that are not really trackable or useful
                if item[-5:] == "Rupee" or item in spoils or (item in letters and item != "Cabana Deed") or item == "Tingle Reward":
                    continue

                #Items on Main Item Screen
                slot = next((x for x in IT if x.name == item), None)
                if slot != None:
                    if dme.read_byte(slot.address) != slot.id:
                        give_item_name(slot.name)
                    continue

                #Progressive Items
                if item == "Progressive Picto Box":
                    count = items_by_name.count(item)
                    if count == 1:
                        if dme.read_byte(0x803C4C4C) != 0x23:
                            give_picto(count)
                    if count == 2:
                        if dme.read_byte(0x803C4C4C) != 0x26:
                            give_picto(count)
                    continue

                if item == "Progressive Sword":
                    count = items_by_name.count(item)
                    if count == 1:
                        if dme.read_byte(0x803C4C16) != 56:
                            give_sword(count)
                    if count == 2:
                        if dme.read_byte(0x803C4C16) != 57:
                            give_sword(count)
                    if count == 3:
                        if dme.read_byte(0x803C4C16) != 58:
                            give_sword(count)
                    if count == 4:
                        if dme.read_byte(0x803C4C16) != 62:
                            give_sword(count)
                    continue

                if item == "Progressive Bow":
                    count = items_by_name.count(item)
                    if count == 1:
                        if dme.read_byte(0x803C4C50) != 39:
                            give_bow(count)
                    if count == 2:
                        if dme.read_byte(0x803C4C50) != 53:
                            give_bow(count)
                    if count == 3:
                        if dme.read_byte(0x803C4C50) != 54:
                            give_bow(count)
                    continue

                if item == "Progressive Shield":
                    count = items_by_name.count(item)
                    if count == 1:
                        if dme.read_byte(0x803C4C17) != 59:
                            give_shield(count)
                    if count == 2:
                        if dme.read_byte(0x803C4C17) != 60:
                            give_shield(count)
                    continue

                if item == "Triforce Shard":
                    count = items_by_name.count(item)
                    for i in range(count):
                        if not dme.read_byte(0x803C4CC6) >> i & 1:
                            val = dme.read_byte(0x803C4CC6)
                            val |= (1 << i)
                            dme.write_byte(0x803C4CC6, val)
                    for x in range(count, 8):
                        if dme.read_byte(0x803C4CC6) >> x & 1:
                            give_shard(count)
                            break
                    continue

                if item == "Bottle":
                    count = items_by_name.count(item)
                    for i in range(count):
                        if dme.read_byte(0x803C4C52+i) == 255:
                            give_next_bottle()
                    for x in range(count, 4):
                        if dme.read_byte(0x803C4C52+i) != 255:
                            give_bottle(count)
                            break
                    continue

                if item == "Quiver Upgrade":
                    count = items_by_name.count(item)
                    if count == 1:
                        if dme.read_byte(0x803C4C77) != 60:
                            give_quiver_bu(count)
                    if count == 2:
                        if dme.read_byte(0x803C4C77) != 99:
                            give_quiver_bu(count)
                    continue

                if item == "Bomb Bag Upgrade":
                    count = items_by_name.count(item)
                    if count == 1:
                        if dme.read_byte(0x803C4C78) != 60:
                            give_bomb_bag_bu(count)
                    if count == 2:
                        if dme.read_byte(0x803C4C78) != 99:
                            give_bomb_bag_bu(count)
                    continue

                if item == "Wallet Upgrade":
                    count = items_by_name.count(item)
                    if count == 1:
                        if dme.read_byte(0x803C4C1A) != 1:
                            give_wallet(count)
                    if count == 2:
                        if dme.read_byte(0x803C4C1A) != 2:
                            give_wallet(count)
                    continue

                #Triforce/Treaure Charts
                if item[9:14] == "Chart":
                    chart_number = int(item[15:len(item)])
                    if item[2] == 'e':
                        bit = next(x for x in TC if x[0] == chart_number)
                        if bit[1] <= 24:
                            if not dme.read_word(0x803C4CDC) >> bit[1]+7 & 1:
                                give_treasure_chart(chart_number)
                        else:
                            if not dme.read_word(0x803C4CDC) >> bit[1]+39 & 1:
                                give_treasure_chart(chart_number)
                    elif item[2] == 'i':
                        if not dme.read_word(0x803C4CDC) >> chart_number-1 & 1:
                            give_triforce_chart(chart_number)
                    continue

                #Heart Container/Pieces
                if item[:5] == "Heart":
                    total = items_by_name.count("Heart Piece") + (items_by_name.count("Heart Container") * 4) + 12
                    while dme.read_byte(0x803C4C09) < total:
                        give_heart_piece()
                    continue

                #Wind Waker Song
                if item in songs:
                    bit = songs.index(item)
                    if not dme.read_byte(0x803C4CC5) >> bit & 1:
                        give_link_song(bit)
                    continue

                #Pearls
                if item[-5:] == "Pearl":
                    if item[0] == "D":
                        if not dme.read_byte(0x803C4CC7) >> 1 & 1:
                            give_pearl("Din's Pearl")
                    elif item[0] == "N":
                        if not dme.read_byte(0x803C4CC7) & 1:
                            give_pearl("Nayru's Pearl")
                    elif item[0] == "F":
                        if not dme.read_byte(0x803C4CC7) >> 2 & 1:
                            give_pearl("Farore's Pearl")
                    continue

                #Special Items
                if item == "Ghost Ship Chart":
                    if not dme.read_word(0x803C4CE0) & 0x00000008:
                        give_ghost_ship()
                    continue

                if item == "Power Bracelets":
                    if dme.read_byte(0x803C4C18) != 40:
                        power_bracelet()
                    continue

                if item == "Heros Charm":
                    if dme.read_byte(0x803C4CC0) != 1:
                        give_hero_charm()
                    continue

                if item == "Cabana Deed":
                    base_address = 0x803C4C8E
                    found: bool = False
                    for i in range(8):
                        if dme.read_byte(base_address+i) == 0x9C:
                            found = True
                    if not found:
                        give_letter("Cabana Deed")
                    continue

                if item == "Double Magic":
                    if dme.read_byte(0x803C4C1B) != 32:
                        double_magic()
                    continue

                if item[:3] == "DRC":
                    if item[4] == 'C':
                        if not dme.read_byte(0x803C4FF4 + 0x21) >> 1 & 1:
                            give_drc_comp()
                    elif item[4] == 'M':
                        if not dme.read_byte(0x803C4FF4 + 0x21) & 1:
                            give_drc_map()
                    elif item[4] == 'B':
                        if not dme.read_byte(0x803C4FF4 + 0x21) >> 2 & 1:
                            give_drc_bk()
                    else:
                        count = items_by_name.count(item)
                        for i in range(count):
                            #print("I:", i, not (dme.read_word(0x803C50B8) >> 16+i))
                            if not (dme.read_word(0x803C50B8) >> 16+i) & 1:
                                give_drc_sk_bu(count)
                                break
                        for x in range(i+1, 4):
                            #print("X:", x, (dme.read_word(0x803C50B8) >> 16+x) & 1)
                            if (dme.read_word(0x803C50B8) >> 16+x) & 1:
                                give_drc_sk_bu(count)
                                break
                    continue

                if item[:2] == "FW":
                    if item[3] == 'C':
                        if not dme.read_byte(0x803C5018 + 0x21) >> 1 & 1:
                            give_fw_comp()
                    elif item[3] == 'M':
                        if not dme.read_byte(0x803C5018 + 0x21) & 1:
                            give_fw_map()
                    elif item[3] == 'B':
                            if not dme.read_byte(0x803C5018 + 0x21) >> 2 & 1:
                                give_fw_bk()
                    else:
                        if not (dme.read_word(0x803C50B8) >> 8) & 1:
                            give_fw_sk()
                    continue

                if item[:4] == "TotG":
                    if item[5] == 'C':
                        if not dme.read_byte(0x803C503C + 0x21) >> 1 & 1:
                            give_totg_comp()
                    elif item[5] == 'M':
                        if not dme.read_byte(0x803C503C + 0x21) & 1:
                            give_totg_map()
                    elif item[5] == 'B':
                        if not dme.read_byte(0x803C503C + 0x21) >> 2 & 1:
                            give_totg_bk()
                    else:
                        count = items_by_name.count(item)
                        #count = 1
                        for i in range(count):
                            print("I:", i,  not (dme.read_word(0x803C50B8) >> 11+i) & 1)
                            if not dme.read_word(0x803C50B8) >> 11+i & 1:
                                
                                give_totg_sk_bu(count)
                                break
                        for x in range(i+1, 2):
                            print("X:", x, (dme.read_word(0x803C50B8) >> 11+x) & 1)
                            if (dme.read_word(0x803C50B8) >> 11+x) & 1:
                                give_totg_sk_bu(count)
                                break
                    continue

                if item[:2] == "FF":
                    if item[3] == 'C':
                        if not dme.read_byte(0x803C4FD0 + 0x21) >> 1 & 1:
                            give_ff_comp()
                    else:
                        if not dme.read_byte(0x803C4FD0 + 0x21) & 1:
                            give_ff_map()
                    continue

                if item[:2] == "ET":
                    if item[3] == 'C':
                        if not dme.read_byte(0x803C5060 + 0x21) >> 1 & 1:
                            give_et_comp()
                    elif item[3] == 'M':
                        if not dme.read_byte(0x803C5060 + 0x21) & 1:
                            give_et_map()
                    elif item[3] == 'B':
                        if not dme.read_byte(0x803C5060 + 0x21) >> 2 & 1:
                            give_et_bk()
                    else:
                        count = items_by_name.count(item)
                        #print("ET:", count)
                        for i in range(count):
                            #print("I loop:", not (dme.read_word(0x803C50B8) >> (13+i)) & 1)
                            if not (dme.read_word(0x803C50B8) >> (13+i)) & 1:
                                give_et_sk_bu(count)
                                break
                        for x in range(i+1, 3):
                            #print("X loop:", x, (dme.read_word(0x803C50B8) >> (13+x)) & 1)
                            if (dme.read_word(0x803C50B8) >> (13+x)) & 1:
                                #print('X RUN')
                                give_et_sk_bu(count)
                                break
                    continue

                if item[:2] == "WT":
                    if item[3] == 'C':
                        if not dme.read_byte(0x803C5084 + 0x21) >> 1 & 1:
                            give_wt_comp()
                    elif item[3] == 'M':
                        if not dme.read_byte(0x803C5084 + 0x21) & 1:
                            give_wt_map()
                    elif item[3] == 'B':
                        if not dme.read_byte(0x803C5084 + 0x21) >> 2 & 1:
                            give_wt_bk()
                    else:
                        count = items_by_name.count(item)
                        for i in range(count):
                            if not (dme.read_word(0x803C50B8) >> 9+i) & 1:
                                give_wt_sk_bu(count)
                                break
                        for x in range(i+1, 2):
                            if (dme.read_word(0x803C50B8) >> 9+x) & 1:
                                give_wt_sk_bu(count)
                                break
                    continue
            #print("Wow Done Checking for now")
            for _ in range(120):
                if not ctx.exit_event.is_set():
                    await asyncio.sleep(5)
        if not ctx.exit_event.is_set():
            await asyncio.sleep(5)
