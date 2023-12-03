class Item:
    def __init__(self, name: str, address: int, id: int):
        self.name = name
        self.address = address
        self.id = id

item_table = [
    Item("Telescope"        , 0x803C4C44, 0x20),
    Item("Tingle Tuner"     , 0x803C4C4B, 0x21),
    Item("Wind Waker"       , 0x803C4C46, 0x22),
    Item("Picto Box"        , 0x803C4C4C, 0x23),
    Item("Spoils Bag"       , 0x803C4C48, 0x24),
    Item("Grappling Hook"   , 0x803C4C47, 0x25),
    Item("Deluxe Picto Box" , 0x803C4C4C, 0x26),
    Item("Hero's Bow"       , 0x803C4C50, 0x27),
    Item("Iron Boots"       , 0x803C4C4D, 0x29),
    Item("Magic Armor"      , 0x803C4C4E, 0x2A),
    Item("Bait Bag"         , 0x803C4C4F, 0x2C),
    Item("Boomerang"        , 0x803C4C49, 0x2D),
    Item("Hookshot"         , 0x803C4C57, 0x2F),
    Item("Delivery Bag"     , 0x803C4C56, 0x30),
    Item("Bombs"            , 0x803C4C51, 0x31),
    Item("Skull Hammer"     , 0x803C4C58, 0x33),
    Item("Deku Leaf"        , 0x803C4C4A, 0x34),
    Item("Fire/Ice Arrows"  , 0x803C4C50, 0x35),
    Item("Light Arrows"     , 0x803C4C50, 0x36),
    Item("Hero's Sword"     , 0x803C4C16, 0x38),
    Item("0/2 Master Sword" , 0x803C4C16, 0x39),
    Item("1/2 Master Sword" , 0x803C4C16, 0x3A),
    Item("Hero's Shield"    , 0x803C4C17, 0x3B),
    Item("Mirror Shield"    , 0x803C4C17, 0x3C),
    Item("2/2 Master Sword" , 0x803C4C16, 0x3E),
    Item("Bottle 1"         , 0x803C4C52, 0x50),
    Item("Bottle 2"         , 0x803C4C53, 0x50),
    Item("Bottle 3"         , 0x803C4C54, 0x50),
    Item("Bottle 4"         , 0x803C4C55, 0x50)
]

treasure_charts = [
#  (Chart Wanted, Bit Needed)  
    (11, 1),
    (15, 2),
    (30, 3),
    (20, 4),
    (5, 5),
    (23, 6),
    (31, 7),
    (33, 8),
    (2, 9),
    (38, 10),
    (39, 11),
    (24, 12),
    (6, 13),
    (12, 14),
    (35, 15),
    (1, 16),
    (29, 17),
    (34, 18),
    (18, 19),
    (16, 20),
    (28, 21),
    (4, 22),
    (3, 23),
    (40, 24),
    (10, 25),
    (14, 26),
    (9, 29),
    (22, 30),
    (36, 31),
    (17, 32),
    (25, 33),
    (37, 34),
    (8, 35),
    (26, 36),
    (41, 37),
    (19, 38),
    (32, 39),
    (13, 40),
    (21, 41),
    (27, 42),
    (7, 43)
]

letters = [
#   (Name, ID) 
    ("Note to Mom"    , 0x99),
    ("Maggies Letter", 0x9A),
    ("Moblins Letter", 0x9B), 
    ("Cabana Deed"    , 0x9C)
]

spoils = [
#   (Name, ID, Counter Address) 
    ("Joy Pendant"    , 0x1F, 0x803C4CAB),
    ("Skull Necklace" , 0x45, 0x803C4CA4),
    ("Boko Baba Seed" , 0x46, 0x803C4CA5),
    ("Golden Feather" , 0x47, 0x803C4CA6),
    ("Knights Crest" , 0x48, 0x803C4CA7),
    ("Red Chu Jelly"  , 0x49, 0x803C4CA8),
    ("Green Chu Jelly", 0x4A, 0x803C4CA9),
    ("Blue Chu Jelly" , 0x4B, 0x803C4CAA)
]

songs = [
    "Winds Requiem", 
    "Ballad of the Gales", 
    "Command Melody", 
    "Earth God's Lyrics", 
    "Wind God's Aria", 
    "Song of Passing"
]
