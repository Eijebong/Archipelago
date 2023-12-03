# Used for testing purposes, just ignore and leave commented
# from itemTable import item_table as IT, treasure_charts as TC, letters, spoils
# import dolphin_memory_engine as dme

from ..inc.packages import dolphin_memory_engine as dme
from .itemTable import item_table as IT, treasure_charts as TC, letters, spoils
import time

def can_be_given() -> bool:
    if dme.read_word(0x803E440C) == 3359508096 or \
       dme.read_word(0x803E440C) == 3359387443 or \
       dme.read_word(0x803E440C) == 3334900736:
        return False
    return True

def give_link_item(address: int, item: int):
    dme.write_byte(address, item)

def take_link_item(address: int):
    dme.write_byte(address, 0xFF)

def give_link_rupees(amount: int):
    dme.write_word(0x803CA768, amount)

def all_charts():
    dme.write_word(0x803C4CDC, 0xFFFFFFFF)
    dme.write_word(0x803C4CE0, 0x0007FFF3)

def double_magic():
    dme.write_byte(0x803C4C1B, 32)
    dme.write_byte(0x803C4C1C, 32)

def power_bracelet():
    dme.write_byte(0x803C4C18, 40)
    dme.write_byte(0x803C4CBE, 1)

def give_link_song(bit: int):
    if bit > 5 or bit < 0:
        print("Song Bit Must Be: 0 <= X <= 5")
        return
    value = dme.read_byte(0x803C4CC5)
    dme.write_byte(0x803C4CC5, value | (2**bit))

def give_item_name(name: str):
    item = next((i for i in IT if i.name == name), None)
    if item.name == "Bombs":
        dme.write_byte(0x803C4C66, dme.read_byte(0x803C4C66) | 1)
    give_link_item(item.address, item.id)

def give_next_sword():
    value = dme.read_byte(0x803C4C16)
    if value == 255:
        give_item_name("Hero's Sword")
        dme.write_byte(0x803C4CBC, 1)
        return
    if value == 56:
        give_item_name("0/2 Master Sword")
        dme.write_byte(0x803C4CBC, 3)
        return
    if value == 57:
        give_item_name("1/2 Master Sword")
        dme.write_byte(0x803C4CBC, 7)
        return
    if value == 58:
        give_item_name("2/2 Master Sword")
        dme.write_byte(0x803C4CBC, 15)
        return
    print("SHOULD HAVE ALL SWORDS")

def give_next_bow():
    value = dme.read_byte(0x803C4C50)
    if value == 255:
        give_item_name("Hero's Bow")
        dme.write_byte(0x803C4C65, dme.read_byte(0x803C4C65) | 1)
        return
    if value == 39:
        give_item_name("Fire/Ice Arrows")
        dme.write_byte(0x803C4C65, dme.read_byte(0x803C4C65) | 2)
        return
    if value == 53:
        give_item_name("Light Arrows")
        dme.write_byte(0x803C4C65, dme.read_byte(0x803C4C65) | 4)
        return
    print("SHOULD HAVE ALL BOWS")

def give_next_shield():
    value = dme.read_byte(0x803C4C17)
    if value == 255:
        give_item_name("Hero's Shield")
        dme.write_byte(0x803C4CBD, 1)
        return
    if value == 59:
        give_item_name("Mirror Shield")
        dme.write_byte(0x803C4CBD, 3)
        return
    print("SHOULD HAVE ALL SHIELDS")

def give_next_picto():
    value = dme.read_byte(0x803C4C4C)
    if value == 255:
        give_item_name("Picto Box")
        return
    if value == 35:
        give_item_name("Deluxe Picto Box")
        return
    print("SHOULD HAVE ALL PICTOS")

def give_next_bottle():
    if dme.read_byte(0x803C4C52) == 255:
        give_item_name("Bottle 1")
        return
    if dme.read_byte(0x803C4C53) == 255:
        give_item_name("Bottle 2")
        return
    if dme.read_byte(0x803C4C54) == 255:
        give_item_name("Bottle 3")
        return
    if dme.read_byte(0x803C4C55) == 255:
        give_item_name("Bottle 4")
        return
    print("SHOULD HAVE ALL BOTTLES")

def give_next_shard():
    address = 0x803C4CC6
    value = dme.read_byte(address)
    if value == 255:
        print("SHOULD HAVE ALL SHARDS")
        return
    tester = 0
    for i in range(0, 8):
        for x in range(0, i):
            tester += 2**x
        if value == tester:
            dme.write_byte(address, value | (2**i))
            return
        tester = 0

def give_next_wallet():
    value = dme.read_byte(0x803C4C1A)
    if value == 0:
        dme.write_byte(0x803C4C1A, 1)
        return
    if value == 1:
        dme.write_byte(0x803C4C1A, 2)
        return
    print("SHOULD HAVE ALL WALLETS")

def give_bomb_bag():
    value = dme.read_byte(0x803C4C78)
    if value == 30:
        dme.write_byte(0x803C4C78, 60)
        dme.write_byte(0x803C4C72, 60)
        return
    if value == 60:
        dme.write_byte(0x803C4C78, 99)
        dme.write_byte(0x803C4C72, 99)
        return
    print("SHOULD HAVE ALL BOMB BAGS")

def give_quiver():
    value = dme.read_byte(0x803C4C77)
    if value == 30:
        dme.write_byte(0x803C4C77, 60)
        dme.write_byte(0x803C4C71, 60)
        return
    if value == 60:
        dme.write_byte(0x803C4C77, 99)
        dme.write_byte(0x803C4C71, 99)
        return
    print("SHOULD HAVE ALL QUIVERS")

def give_hearts(num: int):
    dme.write_byte(0x803CA77F, num)

def give_heart_piece():
    give_hearts(1)
    time.sleep(0.05)

def give_heart_container():
    give_hearts(4)
    time.sleep(0.05)

def give_hero_charm():
    dme.write_byte(0x803C4CC0, 1)

def give_pearl(pearl: str):
    address = 0x803C4CC7
    value = dme.read_byte(address)

    # Checks Pearl and gives proper one
    if pearl == "Din's Pearl":
        dme.write_byte(address, value | 2)
    elif pearl == "Nayru's Pearl":
        dme.write_byte(address, value | 1)
    elif pearl == "Farore's Pearl":
        dme.write_byte(address, value | 4)

    # Checks if you have all three to raise TotG
    if (dme.read_byte(address) & 0x7):
        dme.write_byte(0x803C5240, 0xD0)
        dme.write_byte(0x803C524A, 64)

def give_ghost_ship():
    value = dme.read_word(0x803C4CE0)
    dme.write_word(0x803C4CE0, (value | 0x00000008))


#DUNGEONS
def give_drc_sk():
    #print("ENTERING")
    curr_id = dme.read_byte(0x803C53A4)
    if(curr_id != 0x3):
        curr_keys = dme.read_byte(0x803C5014)
        dme.write_byte(0x803C5014, curr_keys+1)
    else:
        dme.write_byte(0x803CA77D, 1)

    for i in range(4):
        if not (dme.read_word(0x803C50B8) >> 16+i) & 1:
            #print("Setting bit:", 16+i)
            dme.write_word(0x803C50B8, dme.read_word(0x803C50B8) | (1 << (16+i)))
            break

        #print("ef", i)
    #print("LEAVING")


def other_drc_item(bit: int):
    curr_id = dme.read_byte(0x803C53A4)
    if curr_id != 0x3:
        value = dme.read_byte(0x803C4FF4 + 0x21)
        if not (value >> bit) & 1:
            dme.write_byte(0x803C4FF4+0x21, value | (2**bit))
    else:
        value2 = dme.read_byte(0x803C53A1)
        dme.write_byte(0x803C53A1, value2 | (2**bit))

def give_drc_map():
    other_drc_item(0)

def give_drc_comp():
    other_drc_item(1)

def give_drc_bk():
    other_drc_item(2)



def give_fw_sk():
    curr_id = dme.read_byte(0x803C53A4)
    if(curr_id != 0x4):
        curr_keys = dme.read_byte(0x803C5038)
        dme.write_byte(0x803C5038, curr_keys+1)
    else:
        dme.write_byte(0x803CA77D, 1)
    dme.write_word(0x803C50B8, dme.read_word(0x803C50B8) | (1 << 8))

def other_fw_item(bit: int):
    curr_id = dme.read_byte(0x803C53A4)
    if curr_id != 0x4:
        value = dme.read_byte(0x803C5018 + 0x21)
        if not (value >> bit) & 1:
            dme.write_byte(0x803C5018+0x21, value | (2**bit))
    else:
        value2 = dme.read_byte(0x803C53A1)
        dme.write_byte(0x803C53A1, value2 | (2**bit))

def give_fw_map():
    other_fw_item(0)

def give_fw_comp():
    other_fw_item(1)

def give_fw_bk():
    other_fw_item(2)



def other_ff_item(bit: int):
    curr_id = dme.read_byte(0x803C53A4)
    if curr_id != 0x2:
        value = dme.read_byte(0x803C4FD0 + 0x21)
        if not (value >> bit) & 1:
            dme.write_byte(0x803C4FD0+0x21, value | (2**bit))
    else:
        value2 = dme.read_byte(0x803C53A1)
        dme.write_byte(0x803C53A1, value2 | (2**bit))

def give_ff_map():
    other_ff_item(0)

def give_ff_comp():
    other_ff_item(1)


def give_totg_sk():
    curr_id = dme.read_byte(0x803C53A4)
    if(curr_id != 0x5):
        curr_keys = dme.read_byte(0x803C505C)
        dme.write_byte(0x803C505C, curr_keys+1)
    else:
        dme.write_byte(0x803CA77D, 1)
    for i in range(2):
        if not dme.read_word(0x803C50B8) >> 11+i & 1:
            dme.write_word(0x803C50B8, dme.read_word(0x803C50B8) | 1 << 11+i)
            break

def other_totg_item(bit: int):
    curr_id = dme.read_byte(0x803C53A4)
    if curr_id != 0x5:
        value = dme.read_byte(0x803C503C + 0x21)
        if not (value >> bit) & 1:
            dme.write_byte(0x803C503C+0x21, value | (2**bit))
    else:
        value2 = dme.read_byte(0x803C53A1)
        dme.write_byte(0x803C53A1, value2 | (2**bit))

def give_totg_map():
    other_totg_item(0)

def give_totg_comp():
    other_totg_item(1)

def give_totg_bk():
    other_totg_item(2)



def give_et_sk():
    curr_id = dme.read_byte(0x803C53A4)
    #print("CURR_ID:", curr_id)
    if(curr_id != 0x6):
        curr_keys = dme.read_byte(0x803C5080)
        dme.write_byte(0x803C5080, curr_keys+1)
    else:
        dme.write_byte(0x803CA77D, 1)
    for i in range(3):
        #print("Reg I Loop:", not (dme.read_word(0x803C50B8) >> (13+i)) & 1)
        if not (dme.read_word(0x803C50B8) >> (13+i)) & 1:
            dme.write_word(0x803C50B8, dme.read_word(0x803C50B8) | (1 << (13+i)))
            break

def other_et_item(bit: int):
    curr_id = dme.read_byte(0x803C53A4)
    if curr_id != 0x6:
        value = dme.read_byte(0x803C5060 + 0x21)
        if not (value >> bit) & 1:
            dme.write_byte(0x803C5060+0x21, value | (2**bit))
    else:
        value2 = dme.read_byte(0x803C53A1)
        dme.write_byte(0x803C53A1, value2 | (2**bit))

def give_et_map():
    other_et_item(0)

def give_et_comp():
    other_et_item(1)

def give_et_bk():
    other_et_item(2)


def give_wt_sk():
    curr_id = dme.read_byte(0x803C53A4)
    if(curr_id != 0x7):
        curr_keys = dme.read_byte(0x803C50A4)
        dme.write_byte(0x803C50A4, curr_keys+1)
    else:
        dme.write_byte(0x803CA77D, 1)
    for i in range(2):
        if not dme.read_word(0x803C50B8) >> 9+i & 1:
            dme.write_word(0x803C50B8, dme.read_word(0x803C50B8) | 1 << 9+i)
            break

def other_wt_item(bit: int):
    curr_id = dme.read_byte(0x803C53A4)
    if curr_id != 0x7:
        value = dme.read_byte(0x803C5084 + 0x21)
        if not (value >> bit) & 1:
            dme.write_byte(0x803C5084+0x21, value | (2**bit))
    else:
        value2 = dme.read_byte(0x803C53A1)
        dme.write_byte(0x803C53A1, value2 | (2**bit))

def give_wt_map():
    other_wt_item(0)

def give_wt_comp():
    other_wt_item(1)

def give_wt_bk():
    other_wt_item(2)



#TREASURE/TRIFORCE CHARTS
def give_treasure_chart(num: int):
    if not (num > 0 and num < 42):
        print("Not Proper Chart Number (1-41)")
        return

    real_num = next((x for x in TC if x[0] == num), None)
    if real_num[1] <= 24:
        value = dme.read_word(0x803C4CDC)
        dme.write_word(0x803C4CDC, value | (2**(real_num[1]+7)))
    else:
        value = dme.read_word(0x803C4CE0)
        dme.write_word(0x803C4CE0, value | (2**(real_num[1]+7))>>32)

def give_triforce_chart(num: int):
    if not (num > 0 and num < 9):
        print("Not Proper Chart Number (1-8)")
        return
        
    value = dme.read_word(0x803C4CDC)
    dme.write_word(0x803C4CDC, value | (2**(num-1)))


def give_letter(letter: str):
    base_address = 0x803C4C8E
    let = next((x for x in letters if x[0] == letter), None)
    if let != None:
        for x in range(0, 8):
            if(dme.read_byte(base_address + x) == 255):
                dme.write_byte(base_address + x, let[1])
                return

def give_spoil(spoil: str):
    base_address = 0x803C4C7E
    spo = next((x for x in spoils if x[0] == spoil), None)
    if spo != None:
        for x in range(0, 8):
            slot = dme.read_byte(base_address + x)
            if(slot == int(spo[1])):
                value = dme.read_byte(spo[2])
                dme.write_byte(base_address + x, spo[1])
                dme.write_byte(spo[2], value+1)
                return
        for x in range(0, 8):
            slot = dme.read_byte(base_address + x)
            if(slot == 255):
                value = dme.read_byte(spo[2])
                dme.write_byte(base_address + x, spo[1])
                dme.write_byte(spo[2], value+1)
                return
    else:
        print(f"{spoil} not Real Spoil")

def kill_link():
    dme.write_byte(0x803C4C0B, 0)

def give_sword(sword: int):
    dme.write_byte(0x803C4C16, 255)
    dme.write_byte(0x803C4CBC, 0)
    for _ in range(sword):
        give_next_sword()

def give_bow(bow: int):
    dme.write_byte(0x803C4C50, 255)
    dme.write_byte(0x803C4C65, 0)
    for _ in range(bow):
        give_next_bow()

def give_shield(shield: int):
    dme.write_byte(0x803C4C17, 255)
    dme.write_byte(0x803C4CBD, 0)
    for _ in range(shield):
        give_next_shield()

def give_shard(shard: int):
    dme.write_byte(0x803C4CC6, 0)
    for _ in range(shard):
        give_next_shard()

def give_bottle(bottle: int):
    address = 0x803C4C52
    owned = []
    for i in range(4):
        owned.append(dme.read_byte(address+i))
        dme.write_byte(address+i, 255)
    for x in range(bottle):
        dme.write_byte(address+x, owned[x])

def give_quiver_bu(quiver: int):
    dme.write_byte(0x803C4C77, 30)
    dme.write_byte(0x803C4C71, 30)
    for _ in range(quiver):
        give_quiver()

def give_bomb_bag_bu(bb: int):
    dme.write_byte(0x803C4C78, 30)
    dme.write_byte(0x803C4C72, 30)
    for _ in range(bb):
        give_bomb_bag()

def give_picto(picto: int):
    dme.write_byte(0x803C4C4C, 255)
    for _ in range(picto):
        give_next_picto()

def give_wallet(wallet: int):
    dme.write_byte(0x803C4C1A, 0)
    for _ in range(wallet):
        give_next_wallet()

def give_drc_sk_bu(sk: int):
    dme.write_byte(0x803C5014, 0)
    value = dme.read_word(0x803C50B8)
    for i in range(4):
        value &= ~(1 << 16+i)
    dme.write_word(0x803C50B8, value)
    #print("BU_VALUE:", sk, value, value>>16&1, value>>17&1, value>>18&1, value>>19&1)
    for _ in range(sk):
        give_drc_sk()

def give_totg_sk_bu(sk: int):
    dme.write_byte(0x803C505C, 0)
    value = dme.read_word(0x803C50B8)
    for i in range(2):
        value &= ~(1 << 11+i)
    dme.write_word(0x803C50B8, value)
    for _ in range(sk):
        give_totg_sk()

def give_et_sk_bu(sk: int):
    dme.write_byte(0x803C5080, 0)
    value = dme.read_word(0x803C50B8)
    #print("Value:", value, (value>>13)&1, (value>>14)&1, (value>>15)&1)
    for i in range(3):
        value &= ~(1 << 13+i)
    dme.write_word(0x803C50B8, value)
    for _ in range(sk):
        give_et_sk()

def give_wt_sk_bu(sk: int):
    dme.write_byte(0x803C50A4, 0)
    value = dme.read_word(0x803C50B8)
    for i in range(2):
        value &= ~(1 << 9+i)
    dme.write_word(0x803C50B8, value)
    for _ in range(sk):
        give_wt_sk()