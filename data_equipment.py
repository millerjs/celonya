from models import Item, session


def create_all():
    session.merge(Item(name="Armor - Padded",
                       category="Light Armor",
                       cost="5 gp",
                       ac="11 + Dex modifier -- Disadvantage",
                       strength=None,
                       stealth=None,
                       weight="8 lb."))

    session.merge(Item(name="Armor - Leather",
                       category="Light Armor",
                       cost="10 gp",
                       ac="11 + Dex modifier",
                       strength=None,
                       stealth=None,
                       weight="10 lb."))

    session.merge(Item(name="Armor - Studded leather",
                       category="Light Armor",
                       cost="45 gp",
                       ac="12 + Dex modifier",
                       strength=None,
                       stealth=None,
                       weight="13 lb."))

    session.merge(Item(name="Armor - Hide",
                       category="Medium Armor",
                       cost="10 gp",
                       ac="12 + Dex modifier (max 2)",
                       strength=None,
                       stealth=None,
                       weight="12 lb."))

    session.merge(Item(name="Armor - Chain shirt",
                       category="Medium Armor",
                       cost="50 gp",
                       ac="13 + Dex modifier (max 2)",
                       strength=None,
                       stealth=None,
                       weight="20 lb."))

    session.merge(Item(name="Armor - Scale mail",
                       category="Medium Armor",
                       cost="50 gp",
                       ac="14 + Dex modifier (max 2)",
                       strength=None,
                       stealth="Disadvantage",
                       weight="45 lb."))

    session.merge(Item(name="Armor - Breastplate",
                       category="Medium Armor",
                       cost="400 gp",
                       ac="14 + Dex modifier (max 2)",
                       strength=None,
                       stealth=None,
                       weight="20 lb."))

    session.merge(Item(name="Armor - Half plate",
                       category="Heavy Armor",
                       cost="750 gp",
                       ac="15 + Dex modifier (max 2)",
                       strength=None,
                       stealth="Disadvantage",
                       weight="40 lb."))

    session.merge(Item(name="Armor - Ring mail",
                       category="Heavy Armor",
                       cost="30 gp",
                       ac="14",
                       strength=None,
                       stealth="Disadvantage",
                       weight="40 lb."))

    session.merge(Item(name="Armor - Chain mail",
                       category="Heavy Armor",
                       cost="75 gp",
                       ac="16",
                       strength="Str 13",
                       stealth="Disadvantage",
                       weight="55 lb."))

    session.merge(Item(name="Armor - Splint",
                       category="Heavy Armor",
                       cost="200 gp",
                       ac="17",
                       strength="Str 15",
                       stealth="Disadvantage",
                       weight="60 lb."))

    session.merge(Item(name="Armor - Plate",
                       category="Heavy Armor",
                       cost="1,500 gp",
                       ac="18",
                       strength="Str 15",
                       stealth="Disadvantage",
                       weight="65 lb."))

    session.merge(Item(name="Armor - Shield",
                       category="Heavy Armor",
                       cost="10 gp",
                       ac="+2",
                       strength=None,
                       stealth=None,
                       weight="6 lb."))

    session.merge(Item(name='Abacus',
                       category='Gear',
                       cost='2 gp',
                       weight='2 lb.'))


    session.merge(Item(name='Acid (vial)',
                       category='Gear',
                       cost='25 gp',
                       weight='1 lb.'))


    session.merge(Item(name="Alchemist's fire (flask)",
                       category="Gear",
                       cost="50 gp",
                       weight="1 lb."))

    session.merge(Item(name='Arrows (20)',
                       category='Ammunition',
                       cost='1 gp',
                       weight='1 lb.'))


    session.merge(Item(name='Blowgun needles (5)',
                       category='Ammunition',
                       cost='1 gp',
                       weight='1 lb.'))


    session.merge(Item(name='Crossbow bolts (20)',
                       category='Ammunition',
                       cost='1 gp',
                       weight='1½ lb.'))


    session.merge(Item(name='Sling bullets (20)',
                       category='Ammunition',
                       cost='4 cp',
                       weight='1½ lb.'))


    session.merge(Item(name='Antitoxin (vial)',
                       category='Ammunition',
                       cost='50 gp',
                       weight='---'))

    session.merge(Item(name='Crystal',
                       category='Arcane Focus',
                       cost='10 gp',
                       weight='1 lb.'))


    session.merge(Item(name='Orb',
                       category='Arcane Focus',
                       cost='20 gp',
                       weight='3 lb.'))


    session.merge(Item(name='Rod',
                       category='Arcane Focus',
                       cost='10 gp',
                       weight='2 lb.'))


    session.merge(Item(name='Staff',
                       category='Arcane Focus',
                       cost='5 gp',
                       weight='4 lb.'))


    session.merge(Item(name='Wand',
                       category='Arcane Focus',
                       cost='10 gp',
                       weight='1 lb.'))


    session.merge(Item(name='Backpack',
                       category='Gear',
                       cost='2 gp',
                       weight='5 lb.'))


    session.merge(Item(name='Ball bearings (bag of 1,000)',
                       category='Gear',
                       cost='1 gp',
                       weight='2 lb.'))


    session.merge(Item(name='Barrel',
                       category='Gear',
                       cost='2 gp',
                       weight='70 lb.'))


    session.merge(Item(name='Basket',
                       category='Gear',
                       cost='4 sp',
                       weight='2 lb.'))


    session.merge(Item(name='Bedroll',
                       category='Gear',
                       cost='1 gp',
                       weight='7 lb.'))


    session.merge(Item(name='Bell',
                       category='Gear',
                       cost='1 gp',
                       weight='---'))


    session.merge(Item(name='Blanket',
                       category='Gear',
                       cost='5 sp',
                       weight='3 lb.'))


    session.merge(Item(name='Block and tackle',
                       category='Gear',
                       cost='1 gp',
                       weight='5 lb.'))


    session.merge(Item(name='Book',
                       category='Gear',
                       cost='25 gp',
                       weight='5 lb.'))


    session.merge(Item(name='Bottle, glass',
                       category='Gear',
                       cost='2 gp',
                       weight='2 lb.'))


    session.merge(Item(name='Bucket',
                       category='Gear',
                       cost='5 cp',
                       weight='2 lb.'))


    session.merge(Item(name='Caltrops (bag of 20)',
                       category='Gear',
                       cost='1 gp',
                       weight='2 lb.'))


    session.merge(Item(name='Candle',
                       category='Gear',
                       cost='1 cp',
                       weight='---'))


    session.merge(Item(name='Case, crossbow bolt',
                       category='Gear',
                       cost='1 gp',
                       weight='1 lb.'))


    session.merge(Item(name='Case, map or scroll',
                       category='Gear',
                       cost='1 gp',
                       weight='1 lb.'))


    session.merge(Item(name='Chain (10 feet)',
                       category='Gear',
                       cost='5 gp',
                       weight='10 lb.'))


    session.merge(Item(name='Chalk (1 piece)',
                       category='Gear',
                       cost='1 cp',
                       weight='---'))


    session.merge(Item(name='Chest',
                       category='Gear',
                       cost='5 gp',
                       weight='25 lb.'))


    session.merge(Item(name='Climbers kit',
                       category='Gear',
                       cost='25 gp',
                       weight='12 lb.'))


    session.merge(Item(name='Clothes, common',
                       category='Gear',
                       cost='5 sp',
                       weight='3 lb.'))


    session.merge(Item(name='Clothes, costume',
                       category='Gear',
                       cost='5 gp',
                       weight='4 lb.'))


    session.merge(Item(name='Clothes, fine',
                       category='Gear',
                       cost='15 gp',
                       weight='6 lb.'))


    session.merge(Item(name='Clothes, traveler',
                       category='Gear',
                       cost='2 gp',
                       weight='4 lb.'))


    session.merge(Item(name='Component pouch',
                       category='Gear',
                       cost='25 gp',
                       weight='2 lb.'))


    session.merge(Item(name='Crowbar',
                       category='Gear',
                       cost='2 gp',
                       weight='5 lb.'))

    session.merge(Item(name='Sprig of mistletoe',
                       category='Druidic Focus',
                       cost='1 gp',
                       weight='---'))


    session.merge(Item(name='Totem',
                       category='Druidic Focus',
                       cost='1 gp',
                       weight='---'))


    session.merge(Item(name='Wooden staff',
                       category='Druidic Focus',
                       cost='5 gp',
                       weight='4 lb.'))


    session.merge(Item(name='Yew wand',
                       category='Druidic Focus',
                       cost='10 gp',
                       weight='1 lb.'))


    session.merge(Item(name='Fishing tackle',
                       category='Gear',
                       cost='1 gp',
                       weight='4 lb.'))


    session.merge(Item(name='Flask or tankard',
                       category='Gear',
                       cost='2 cp',
                       weight='1 lb.'))


    session.merge(Item(name='Grappling hook',
                       category='Gear',
                       cost='2 gp',
                       weight='4 lb.'))


    session.merge(Item(name='Hammer',
                       category='Gear',
                       cost='1 gp',
                       weight='3 lb.'))


    session.merge(Item(name='Hammer, sledge',
                       category='Gear',
                       cost='2 gp',
                       weight='10 lb.'))


    session.merge(Item(name='Healers kit',
                       category='Gear',
                       cost='5 gp',
                       weight='3 lb.'))


    session.merge(Item(name='Amulet',
                       category='Holy Symbol',
                       cost='5 gp',
                       weight='1 lb.'))


    session.merge(Item(name='Emblem',
                       category='Holy Symbol',
                       cost='5 gp',
                       weight='---'))


    session.merge(Item(name='Reliquary',
                       category='Holy Symbol',
                       cost='5 gp',
                       weight='2 lb.'))


    session.merge(Item(name='Holy water (flask)',
                       category='Gear',
                       cost='25 gp',
                       weight='1 lb.'))


    session.merge(Item(name='Hourglass',
                       category='Gear',
                       cost='25 gp',
                       weight='1 lb.'))


    session.merge(Item(name='Hunting trap',
                       category='Gear',
                       cost='5 gp',
                       weight='25 lb.'))


    session.merge(Item(name='Ink (1 ounce bottle)',
                       category='Gear',
                       cost='10 gp',
                       weight='---'))


    session.merge(Item(name='Ink pen',
                       category='Gear',
                       cost='2 cp',
                       weight='---'))


    session.merge(Item(name='Jug or pitcher',
                       category='Gear',
                       cost='2 cp',
                       weight='4 lb.'))


    session.merge(Item(name='Ladder (10-foot)',
                       category='Gear',
                       cost='1 sp',
                       weight='25 lb.'))


    session.merge(Item(name='Lamp',
                       category='Gear',
                       cost='5 sp',
                       weight='1 lb.'))


    session.merge(Item(name='Lantern, bullseye',
                       category='Gear',
                       cost='10 gp',
                       weight='2 lb.'))


    session.merge(Item(name='Lantern, hooded',
                       category='Gear',
                       cost='5 gp',
                       weight='2 lb.'))


    session.merge(Item(name='Lock',
                       category='Gear',
                       cost='10 gp',
                       weight='1 lb.'))


    session.merge(Item(name='Magnifying glass',
                       category='Gear',
                       cost='100 gp',
                       weight='---'))


    session.merge(Item(name='Manacles',
                       category='Gear',
                       cost='2 gp',
                       weight='6 lb.'))


    session.merge(Item(name='Mess kit',
                       category='Gear',
                       cost='2 sp',
                       weight='1 lb.'))


    session.merge(Item(name='Mirror, steel',
                       category='Gear',
                       cost='5 gp',
                       weight='1/2 lb.'))


    session.merge(Item(name='Oil (flask)',
                       category='Gear',
                       cost='1 sp',
                       weight='1 lb.'))


    session.merge(Item(name='Paper (one sheet)',
                       category='Gear',
                       cost='2 sp',
                       weight='---'))


    session.merge(Item(name='Parchment (one sheet)',
                       category='Gear',
                       cost='1 sp',
                       weight='---'))


    session.merge(Item(name='Perfume (vial)',
                       category='Gear',
                       cost='5 gp',
                       weight='---'))


    session.merge(Item(name='Pick, miners',
                       category='Gear',
                       cost='2 gp',
                       weight='10 lb.'))


    session.merge(Item(name='Piton',
                       category='Gear',
                       cost='5 cp',
                       weight='1/4 lb.'))


    session.merge(Item(name='Poison, basic (vial)',
                       category='Gear',
                       cost='100 gp',
                       weight='---'))


    session.merge(Item(name='Pole (10-foot)',
                       category='Gear',
                       cost='5 cp',
                       weight='7 lb.'))


    session.merge(Item(name='Pot, iron',
                       category='Gear',
                       cost='2 gp',
                       weight='10 lb.'))


    session.merge(Item(name='Potion of healing',
                       category='Gear',
                       cost='50 gp',
                       weight='1/2 lb.'))


    session.merge(Item(name='Pouch',
                       category='Gear',
                       cost='5 sp',
                       weight='1 lb.'))


    session.merge(Item(name='Quiver',
                       category='Gear',
                       cost='1 gp',
                       weight='1 lb.'))


    session.merge(Item(name='Ram, portable',
                       category='Gear',
                       cost='4 gp',
                       weight='35 lb.'))


    session.merge(Item(name='Rations (1 day)',
                       category='Gear',
                       cost='5 sp',
                       weight='2 lb.'))


    session.merge(Item(name='Robes',
                       category='Gear',
                       cost='1 gp',
                       weight='4 lb.'))


    session.merge(Item(name='Rope, hempen (50 feet)',
                       category='Gear',
                       cost='1 gp',
                       weight='10 lb.'))


    session.merge(Item(name='Rope, silk (50 feet)',
                       category='Gear',
                       cost='10 gp',
                       weight='5 lb.'))


    session.merge(Item(name='Sack',
                       category='Gear',
                       cost='1 cp',
                       weight='1/2 lb.'))


    session.merge(Item(name='Scale, merchants',
                       category='Gear',
                       cost='5 gp',
                       weight='3 lb.'))


    session.merge(Item(name='Sealing wax',
                       category='Gear',
                       cost='5 sp',
                       weight='---'))


    session.merge(Item(name='Shovel',
                       category='Gear',
                       cost='2 gp',
                       weight='5 lb.'))


    session.merge(Item(name='Signal whistle',
                       category='Gear',
                       cost='5 cp',
                       weight='---'))


    session.merge(Item(name='Signet ring',
                       category='Gear',
                       cost='5 gp',
                       weight='---'))


    session.merge(Item(name='Soap',
                       category='Gear',
                       cost='2 cp',
                       weight='---'))


    session.merge(Item(name='Spellbook',
                       category='Gear',
                       cost='50 gp',
                       weight='3 lb.'))


    session.merge(Item(name='Spikes, iron (10)',
                       category='Gear',
                       cost='1 gp',
                       weight='5 lb.'))


    session.merge(Item(name='Spyglass',
                       category='Gear',
                       cost='1,000 gp',
                       weight='1 lb.'))


    session.merge(Item(name='Tent, two-person',
                       category='Gear',
                       cost='2 gp',
                       weight='20 lb.'))


    session.merge(Item(name='Tinderbox',
                       category='Gear',
                       cost='5 sp',
                       weight='1 lb.'))


    session.merge(Item(name='Torch',
                       category='Gear',
                       cost='1 cp',
                       weight='1 lb.'))


    session.merge(Item(name='Vial',
                       category='Gear',
                       cost='1 gp',
                       weight='---'))


    session.merge(Item(name='Waterskin',
                       category='Gear',
                       cost='2 sp',
                       weight='5 lb. (full)'))


    session.merge(Item(name='Whetstone',
                       category='Gear',
                       cost='1 cp',
                       weight='1 lb.'))


    session.merge(Item(name="Club",
                       cost="1 sp",
                       category='weapon',
                       damage="1d4 bludgeoning",
                       weight="2 lb.",
                       properties="Light"))

    session.merge(Item(name="Dagger",
                       cost="2 gp",
                       category='weapon',
                       damage="1d4 piercing",
                       weight="1 lb.",
                       properties="Finesse, light, thrown (range 20/60)"))


    session.merge(Item(name="Greatclub",
                       cost="2 sp",
                       category='weapon',
                       damage="1d8 bludgeoning",
                       weight="10 lb.",
                       properties="Two-handed"))

    session.merge(Item(name="Handaxe",
                       cost="5 gp",
                       category='weapon',
                       damage="1d6 slashing",
                       weight="2 lb.",
                       properties="Light, thrown (range 20/60)"))

    session.merge(Item(name="Light hammer",
                       cost="2 gp",
                       category='weapon',
                       damage="1d4 bludgeoning",
                       weight="2 lb.",
                       properties="Light, thrown (range 20/60)"))

    session.merge(Item(name="Mace",
                       cost="5 gp",
                       category='weapon',
                       damage="1d6 bludgeoning",
                       weight="4 lb.",
                       properties=None))

    session.merge(Item(name="Sickle",
                       cost="1 gp",
                       category='weapon',
                       damage="1d4 slashing",
                       weight="2 lb.",
                       properties="Light"))

    session.merge(Item(name="Spear",
                       cost="1 gp",
                       category='weapon',
                       damage="1d6 piercing",
                       weight="3 lb.",
                       properties="Thrown (range 20/60), versatile (1d8)"))


    session.merge(Item(name="Crossbow, light",
                       cost="25 gp",
                       category='weapon',
                       damage="1d8 piercing",
                       weight="5 lb.",
                       properties="Ammunition (range 80/320), loading, two-handed"))

    session.merge(Item(name="Dart",
                       cost="5 cp",
                       category='weapon',
                       damage="1d4 piercing",
                       weight="1/4 lb.",
                       properties="Finesse, thrown (range 20/60)"))

    session.merge(Item(name="Sling",
                       cost="1 sp",
                       category='weapon',
                       damage="1d4 bludgeoning",
                       weight=None,
                       properties="Martial Melee, Ammunition (range 30/120)"))


    session.merge(Item(name="Battleaxe",
                       cost="10 gp",
                       category='weapon',
                       damage="1d8 slashing",
                       weight="4 lb.",
                       properties="Versatile (1d10)"))

    session.merge(Item(name="Flail",
                       cost="10 gp",
                       category='weapon',
                       damage="1d8 bludgeoning",
                       weight="2 lb.",
                       properties=None))



    session.merge(Item(name="Greataxe",
                       cost="30 gp",
                       category='weapon',
                       damage="1d12 slashing",
                       weight="7 lb.",
                       properties="Heavy, two-handed"))

    session.merge(Item(name="Greatsword",
                       cost="50 gp",
                       category='weapon',
                       damage="2d6 slashing",
                       weight="6 lb.",
                       properties="Heavy, two-handed"))


    session.merge(Item(name="Lance",
                       cost="10 gp",
                       category='weapon',
                       damage="1d12 piercing",
                       weight="6 lb.",
                       properties="Reach, special"))

    session.merge(Item(name="Longsword",
                       cost="15 gp",
                       category='weapon',
                       damage="1d8 slashing",
                       weight="3 lb.",
                       properties="Versatile (1d10)"))

    session.merge(Item(name="Morningstar",
                       cost="15 gp",
                       category='weapon',
                       damage="1d8 piercing",
                       weight="4 lb.",
                       properties=None))

    session.merge(Item(name="Pike",
                       cost="5 gp",
                       category='weapon',
                       damage="1d10 piercing",
                       weight="18 lb.",
                       properties="Heavy, reach, two-handed"))

    session.merge(Item(name="Scimitar",
                       cost="25 gp",
                       category='weapon',
                       damage="1d6 slashing",
                       weight="3 lb.",
                       properties="Finesse, light"))

    session.merge(Item(name="Shortsword",
                       cost="10 gp",
                       category='weapon',
                       damage="1d6 piercing",
                       weight="2 lb.",
                       properties="Finesse, light"))

    session.merge(Item(name="War pick",
                       cost="5 gp",
                       category='weapon',
                       damage="1d8 piercing",
                       weight="2 lb.",
                       properties=None))

    session.merge(Item(name="Warhammer",
                       cost="15 gp",
                       category='weapon',
                       damage="1d8 bludgeoning",
                       weight="2 lb.",
                       properties="Versatile (1d10)"))

    session.merge(Item(name="Whip",
                       cost="2 gp",
                       category='weapon',
                       damage="1d4 slashing",
                       weight="3 lb.",
                       properties="Finesse, reach"))

    session.merge(Item(name="Blowgun",
                       cost="10 gp",
                       category='weapon',
                       damage="1 piercing",
                       weight="1 lb.",
                       properties="Ammunition (range 25/100), loading"))

    session.merge(Item(name="Crossbow, hand",
                       cost="75 gp",
                       category='weapon',
                       damage="1d6 piercing",
                       weight="3 lb.",
                       properties="Ammunition (range 30/120), light, loading"))

    session.merge(Item(name="Longbow",
                       cost="50 gp",
                       category='weapon',
                       damage="1d8 piercing",
                       weight="2 lb.",
                       properties="Ammunition (range 150/600), heavy, two-handed"))

    session.merge(Item(name="Shortbow",
                       cost="50 gp",
                       category='weapon',
                       damage="1d8 piercing",
                       weight="2 lb.",
                       properties="Ammunition (range 150/600), heavy, two-handed"))

    session.merge(Item(name="Net",
                       cost="1 gp",
                       category='weapon',
                       damage=None,
                       weight="3 lb.",
                       properties="Special, thrown (range 5/15)"))

    session.merge(Item(name="Quarterstaff",
                       cost="1 sp",
                       category='weapon',
                       damage='1d4 bludgeoning',
                       weight="4 lb.",
                       properties="Versatile (1d8)"))

    session.merge(Item(name="Javelin",
                       cost="5 sp",
                       category='weapon',
                       damage='1d6 piercing',
                       weight="2 lb.",
                       properties="Light, thrown (20/60)"))

    session.commit()
