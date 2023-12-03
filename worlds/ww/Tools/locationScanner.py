from ..inc.packages import dolphin_memory_engine as dme
from .LocationTable import location_table as LT
import time
import asyncio

class stage:
    def __init__(self, id: int, chest_max: int, pick_max: int):
        self.id: int = id
        self.chest_max: int = chest_max
        self.pick_max: int = pick_max
        self.mem_max: int = []
        self.chart_max: int = []


def calc_bit(bit: int) -> list: 
    active_bits = []

    if bit <= 0:
        active_bits.append(-1)
        return active_bits

    for x in range(0, 32):
        if bit & 1:
            active_bits.append(x)
        bit >>= 1

    return active_bits

#Doesn't currently work
async def death_link_watch(ctx):
    dme.hook()
    while(not ctx.exit_event.is_set()):
        #print("Death Link")
        #print(dme.read_byte(0x803C4C0B))
        if dme.read_byte(0x803C4C0B) == 0 and time.time() - ctx.last_death_link > 30:
            await ctx.send_death()
            while dme.read_byte(0x803C4C0B) == 0:
                i=0
        
        await asyncio.sleep(3)


async def printCheckFound(checkFound, logger, ctx, ww_loc_name_to_id):
    if checkFound.name == "Victory" and ctx.finished_game == False:
        await ctx.send_msgs([{
            "cmd": "StatusUpdate",
            "status": 30
        }])
        ctx.finished_game = True
    else:    
        checks = [ww_loc_name_to_id[checkFound.name]]
        await ctx.send_msgs([{
            "cmd": "LocationChecks", "locations": checks
        }])
        #await ww_item_giver(ctx)



async def location_scanner(logger, ctx, ww_loc_name_to_id):
    dme.hook()

    stage_max_list = [
        stage(int(0x0), 0, 0),
        stage(int(0x1), 0, 0),
        stage(int(0x2), 0, 0),
        stage(int(0x3), 0, 0),
        stage(int(0x4), 0, 0),
        stage(int(0x5), 0, 0),
        stage(int(0x6), 0, 0),
        stage(int(0x7), 0, 0),
        stage(int(0x8), 0, 0),
        stage(int(0x9), 0, 0),
        stage(int(0xA), 0, 0),
        stage(int(0xB), 0, 0),
        stage(int(0xC), 0, 0),
        stage(int(0xD), 0, 0)
    ]

    for i in stage_max_list:
        for _ in range(0, 4):
            i.mem_max.append(0)
            i.chart_max.append(0)


    #print("Scanning: ")
    #logger.info("SCANNING")


    while not ctx.exit_event.is_set():
        #print("Location Scanner")
        stage_id = hex(dme.read_byte(0x803C53A4))
        stage_maxs = next((x for x in stage_max_list if hex(x.id) == stage_id), None)
        stage_chest_value = dme.read_word(0x803C5380)
        stage_pick_value = dme.read_word(0x803C5394)
        stage_mem_values =  [dme.read_word(0x803C5384),
                             dme.read_word(0x803C5388),
                             dme.read_word(0x803C538C),
                             dme.read_word(0x803C5390)]

        stage_chart_values = [dme.read_word(0x803C4CFC),
                              dme.read_word(0x803C4D00),
                              dme.read_word(0x803C4D04),
                              dme.read_word(0x803C4D08)]

        if(stage_maxs == None):
            continue
        if(stage_chest_value > stage_maxs.chest_max):
            bit = calc_bit(stage_chest_value - stage_maxs.chest_max)
            for the_bit in bit:
                checkFound = next((x for x in LT if hex(x.stageID) == stage_id and x.which_bit == the_bit and x.isChestID == True), None)
                if checkFound == None:
                    running = 0
                    print("Check not registered")
                    continue
                await printCheckFound(checkFound, logger, ctx, ww_loc_name_to_id)
                stage_maxs.chest_max = stage_chest_value
        
        #Sea Alt Chests
        if stage_id == hex(0):
            stage1_chest_val = dme.read_word(0x803C4FAC)
            stage1_maxs = next((x for x in stage_max_list if hex(x.id) == hex(1)), None)
            if(stage1_maxs.chest_max < stage1_chest_val):
                bit1 = calc_bit(stage1_chest_val - stage1_maxs.chest_max)
                for bits in bit1:
                    check1Found = next((x for x in LT if hex(x.stageID) == hex(1) and x.which_bit == bits and x.isChestID == True), None)
                    if check1Found == None:
                        running = 0
                        continue
                    await printCheckFound(check1Found, logger, ctx, ww_loc_name_to_id)
                    stage1_maxs.chest_max = stage1_chest_val


        if(stage_pick_value > stage_maxs.pick_max):
            pbit = calc_bit(stage_pick_value - stage_maxs.pick_max)
            for p in pbit:
                pickFound = next((x for x in LT if hex(x.stageID) == stage_id and x.which_bit == p and x.isPickID == True), None)
                if pickFound != None:
                    await printCheckFound(pickFound, logger, ctx, ww_loc_name_to_id)
                stage_maxs.pick_max = stage_pick_value
        
        #stage_mem_values are values just now read in
        #stage_maxs.mem_max
        counter: int = 0
        for x in stage_mem_values:
            if x > stage_maxs.mem_max[counter]:
                mbit = calc_bit(x - stage_maxs.mem_max[counter])
                for m in mbit:
                    #logger.info(f"{stage_id}:{counter}:{m} bit activated")
                    memFound = next((i for i in LT if hex(i.stageID) == stage_id and i.which_bit == m and i.isMemID == True and i.which_mem == counter), None)
                    if memFound != None:
                        await printCheckFound(memFound, logger, ctx, ww_loc_name_to_id)
                    stage_maxs.mem_max[counter] = x
            if x < stage_maxs.mem_max[counter]:
                x = stage_maxs.mem_max[counter]
            counter += 1

        #Chart Salvages
        counter = 0
        for scv in stage_chart_values:
            if scv > stage_maxs.chart_max[counter]:
                cbit = calc_bit(scv - stage_maxs.chart_max[counter])
                for c in cbit:
                    chartFound = next((i for i in LT if hex(i.stageID) == stage_id and i.which_bit == c and i.isChart == True and i.which_chart == counter), None)
                    if chartFound != None:
                        await printCheckFound(chartFound, logger, ctx, ww_loc_name_to_id)
                    stage_maxs.chart_max[counter] = scv
            if scv < stage_maxs.chart_max[counter]:
                scv = stage_maxs.chart_max[counter]
            counter += 1

        #Various
        #Cyclos
        CyclosCheck = next((y for y in LT if y.name == "Great Sea - Defeat Cyclos" and y.hasGotten == False), None)
        if CyclosCheck != None:
            CyclosValue = dme.read_byte(0x803C5253)
            if CyclosValue >> 4 & 1:
                await printCheckFound(CyclosCheck, logger, ctx, ww_loc_name_to_id)
                CyclosCheck.hasGotten = True

        #Expensive Beedle
        ExpensiveValue = dme.read_byte(0x803C524C)
        for evBit in range(3,6):
            if (ExpensiveValue >> evBit) & 1:
                ExpensiveCheck = next((E for E in LT if E.isVar == True and hex(E.stageID) == hex(0xA) and E.which_bit == evBit and E.hasGotten == False), None)
                if ExpensiveCheck != None:
                    await printCheckFound(ExpensiveCheck, logger, ctx, ww_loc_name_to_id)
                    ExpensiveCheck.hasGotten = True

        #BattleSquid
        BattleValue = dme.read_byte(0x803C532A)
        BattleCheck = next((B for B in LT if B.isVar == True and B.which_bit == BattleValue and B.name[15:22] == "Sploosh" and B.hasGotten == False), None)
        if BattleCheck != None:
            await printCheckFound(BattleCheck, logger, ctx, ww_loc_name_to_id)
            BattleCheck.hasGotten = True

        #Mail Game
        MailValue = dme.read_byte(0x803C52EE)
        if MailValue == 3:
            MailCheck = next((M for M in LT if M.name == "DRI - Mail Game" and M.hasGotten == False), None)
            if MailCheck != None:
                await printCheckFound(MailCheck, logger, ctx, ww_loc_name_to_id)
                MailCheck.hasGotten = True

        #Potion Shop
        PotionValue = dme.read_byte(0x803C5239)
        for pvBit in range(1, 3):
            PotionCheck = next((P for P in LT if P.which_bit == pvBit and P.name[-7:] == "Brewery" and P.hasGotten == False), None)
            if (PotionValue >> pvBit) & 1 and PotionCheck != None:
                await printCheckFound(PotionCheck, logger, ctx, ww_loc_name_to_id)
                PotionCheck.hasGotten = True

        #WitheredTrees
        WitheredValue = dme.read_byte(0x803C525A)
        if (WitheredValue >> 5) & 1:
            WitheredCheck = next((W for W in LT if W.name == "Great Sea - Withered Trees" and W.hasGotten == False), None)
            if WitheredCheck != None:
                await printCheckFound(WitheredCheck, logger, ctx, ww_loc_name_to_id)
                WitheredCheck.hasGotten = True

        #Orca Spoils
        OrcaValue = dme.read_byte(0x803C5237)
        if (OrcaValue >> 5) & 1:
            OrcaCheck = next((O for O in LT if O.name == "Outset - Give Orca 10 Knights Crest" and O.hasGotten == False), None)
            if OrcaCheck != None:
                await printCheckFound(OrcaCheck, logger, ctx, ww_loc_name_to_id)
                OrcaCheck.hasGotten = True

        await asyncio.sleep(1)
