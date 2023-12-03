from CommonClient import CommonContext, ClientCommandProcessor, server_loop, gui_enabled, get_base_parser, logger
import Utils
from Utils import Version

import asyncio

from .inc.packages import dolphin_memory_engine as dme
from worlds import network_data_package
from .Items import lookup_id_to_name as item_id_to_name
from .Tools.locationScanner import location_scanner, death_link_watch
from .Tools.itemTable import item_table as IT
from .Tools.item_checker import item_checker
from .Tools.itemGiver import ww_item_giver, kill_link, can_be_given



class WWCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

class WWCommonContext(CommonContext):
    command_processor = WWCommandProcessor
    game = "Wind Waker"
    items_handling = 0b011

    def __init__(self, server_address, password):
        super(WWCommonContext, self).__init__(server_address, password)
        self.auth = None
        self.client = None
        self.locations_checked = []
        self.items_received = []
        self.is_connected = False
        self.send_index = 0
        self.server_version: Version = Version(4, 2, 0)
        self.finished_game = False


    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(WWCommonContext, self).server_auth(password_requested)

        if not self.auth:
            logger.info("Enter slot name: ")
            self.auth = await self.console_input()

        await self.send_connect()

    def run_gui(self):
        from kvui import GameManager

        class WWManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Wind Waker Client"
        
        self.ui = WWManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    def on_deathlink(self, data: dict):
        kill_link()
        super().on_deathlink(data)
    
    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            if 'death_link' in args['slot_data']:
                Utils.async_start(self.update_death_link(bool(args['slot_data']['death_link'])))


async def ww_location_watcher(ctx: WWCommonContext):
    ww_loc_name_to_id = network_data_package["games"]["Wind Waker"]["location_name_to_id"]
    log = asyncio.create_task(location_scanner(logger, ctx, ww_loc_name_to_id), name="locSc")
    await log

#Doesn't Currently Work
async def death_link_watcher(ctx: WWCommonContext):
    watch = asyncio.create_task(death_link_watch(ctx), name='watt')
    await watch


parser = get_base_parser()
args = parser.parse_args()

def main():

    Utils.init_logging("Wind Waker Client", exception_logger="Client")

    async def _main(args):

        ctx = WWCommonContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="Server Loop")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        
        while not ctx.auth:
            await asyncio.sleep(0.01)
            

        logger.info("Attempting to connect to Dolphin")
        check: bool = False
        while not check:
            dme.hook()
            if can_be_given():
                ctx.send_index = dme.read_word(0x803C50B8) & 255
                check = True
            else:
                logger.info("Please Load Into Save File")
                await asyncio.sleep(5)
        logger.info("Dolphin Connected")

        await asyncio.sleep(3)
        location_watcher = asyncio.create_task(ww_location_watcher(ctx), name="WWProgressionWatcher")
        item_giver = asyncio.create_task(ww_item_giver(ctx), name="ItemGiver")
        item_check = asyncio.create_task(item_checker(ctx), name="WWItemChecker")

        if 'DeathLink' in ctx.tags:
            death = asyncio.create_task(death_link_watch(ctx))
            await death

        await ctx.exit_event.wait()
        ctx.server_address = None

        await location_watcher
        await item_giver
        await item_check

        await ctx.shutdown()
    
    import colorama

    colorama.init()
    asyncio.run(_main(args))
    colorama.deinit()

