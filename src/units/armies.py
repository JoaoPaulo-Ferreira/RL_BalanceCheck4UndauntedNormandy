import os
import yaml
import random 
from troops import * 

class Deck:
    def __init__(self):
        self.cards = []

    def shuffle(self):
        self.cards = random.shuffle(self.cards)
        


class Army:
    def __init__(self, conf_army, nation):
        self.nation = nation
        deck, supply = self.load_army(conf_army)
        self.deck = deck
        self.supply = supply


    def load_army(self, conf_army):
        with open(conf_army, 'r') as f:
            troops_dict = yaml.load(f, Loader=yaml.SafeLoader)
            nation_troops = troops_dict.get(self.nation, {})
            active_troops = nation_troops.get('Deck', {})
            self.deck = []
            for name, attr in active_troops.items():
                match name:
                    case "Sergeant":
                        self.deck.append(self.build_sergeant())

                
    def build_sergeant(self):
        return [Sergeant()]

    def build_leader(self, attr):
        squads = attr.get('squads', [])
        leader_list = []
        for s in squads:
            leader_list.append(Leader(squad=s))
        return leader_list

    def build_rifleman(self, attr):
        rifleman_list = []
        squads = attr.get('squads', [])
        position = attr.get('position', False)
        count = attr.get('count', 1)

        for squads_idx in range(len(squads)):
            for i in range(count):
                unit = Rifleman(squad=squads[squads_idx])
                if position:
                    unit.set_position(position[squads_idx])
                rifleman_list.append(unit)
        return rifleman_list 


    def build_scouts(self, attr):
        scouts_list = []
        squads = attr.get('squads', [])
        position = attr.get('position', False)
        count = attr.get('count', 1)

        for squads_idx in range(len(squads)):
            for i in range(count):
                unit = Scouts(squad=squads[squads_idx])
                if position:
                    unit.set_position(position[squads_idx])
                scouts_list.append(unit)
        return scouts_list 

    def build_fog(self, attr):
        count = attr.get('count', 1)
        fog_list = []
        for i in range(count):
            fog_list.append(Fog())
        return fog_list
       


# army1_filepath

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    nation_army = Army(os.getenv('army1_filepath'), nation="USA")
