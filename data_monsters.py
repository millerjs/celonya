from models import Monster, session

import json


def dict_to_rst(data):
    if isinstance(data, list):
        return '\n'.join(map(dict_to_rst, data))

    return '\t'.join([
        '**%s**: %s' % (key, val)
        for key, val in data.items()
    ])


def create_all():
    with open('data_monsters.json', 'r') as f:
        monsters = json.loads(f.read())

    for monster in monsters:
        if not monster.get('name'):
            continue

        session.merge(Monster(
            str=monster.get('strength', None),
            con=monster.get('constitution', None),
            int=monster.get('intelligence', None),
            wis=monster.get('wisdom', None),
            cha=monster.get('charisma', None),
            dex=monster.get('dexterity', None),
            HP=monster.get('hit_points', None),
            AC=monster.get('armor_class', None),
            speed=monster.get('speed', None),
            name=monster.get('name', None),
            size=monster.get('size', None),
            type=monster.get('type', None),
            subtype=monster.get('subtype', None),
            alignment=monster.get('alignment', None),
            hit_dice=monster.get('hit_dice', None),
            stealth=monster.get('stealth', None),
            damage_vulnerabilities=monster.get('damage_vulnerabilities', None),
            damage_resistances=monster.get('damage_resistances', None),
            damage_immunities=monster.get('damage_immunities', None),
            condition_immunities=monster.get('condition_immunities', None),
            senses=monster.get('senses', None),
            languages=monster.get('languages', None),
            challenge_rating=monster.get('challenge_rating', None),
            special_abilities=dict_to_rst(monster.get('special_abilities', [])),
            actions=dict_to_rst(monster.get('actions', [])),
        ))

    session.commit()


if __name__ == '__main__':
    create_all()
