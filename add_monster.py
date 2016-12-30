from models import Monster, MonsterInstance, session


def add(name, monster_type):
    monster_type = (session.query(Monster)
                            .filter(Monster.name == monster_type)
                            .one())

    session.merge(MonsterInstance(
        name=name,
        monster_type=monster_type.name,
        str=monster_type.str,
        con=monster_type.con,
        int=monster_type.int,
        wis=monster_type.wis,
        cha=monster_type.cha,
        dex=monster_type.dex,
        HP=monster_type.HP,
        AC=monster_type.AC,
        speed=monster_type.speed,
        size=monster_type.size,
        type=monster_type.type,
        subtype=monster_type.subtype,
        alignment=monster_type.alignment,
        hit_dice=monster_type.hit_dice,
        stealth=monster_type.stealth,
        damage_vulnerabilities=monster_type.damage_vulnerabilities,
        damage_resistances=monster_type.damage_resistances,
        damage_immunities=monster_type.damage_immunities,
        condition_immunities=monster_type.condition_immunities,
        senses=monster_type.senses,
        languages=monster_type.languages,
        challenge_rating=monster_type.challenge_rating,
        special_abilities=monster_type.special_abilities,
        actions=monster_type.actions,
    ))

    session.commit()
