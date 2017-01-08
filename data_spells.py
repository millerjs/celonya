from models import Spell, session

import json


def create_all():
    with open('data_spells.json', 'r') as f:
        spells = json.loads(f.read())

    for name, spell in spells.items():
        if not spell.get('name'):
            continue

        session.merge(Spell(
            name=name,
            str=spell.get('strength', None),
            casting_time=spell.get('casting_time', ''),
            components=spell.get('components', ''),
            description=spell.get('description', ''),
            duration=spell.get('duration', ''),
            level=spell.get('level', None),
            range=spell.get('range', ''),
            school=spell.get('school', ''),
        ))

    session.commit()


if __name__ == '__main__':
    create_all()
