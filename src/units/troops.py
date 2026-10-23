import numpy as np


def dice_roll(size):
    return np.random.Generator.integers(low=1, high=6, size=size, endpoint=True)


class unit:
    def __init__(self, name, squad="", position="", initiative=0, shield=0, actions=[]):
        self.name = name
        self.squad = squad
        self.position = position
        self.initiative = initiative
        self.shield = shield
        self.actions = actions

    def set_position(self, new_position):
        self.position = new_position

    def set_actions(self, actions_list):
        self.actions = actions_list

    def set_squad(self):
        pass

    def set_suppress(self):
        pass

    def __eq__(other_unit):

        outcome = []
        if hasattr(self, squad):
            outcome.apppend(self.squad == other_unit.squad)

        if hasattr(self, )



class Scouts:
    def __init__(self, initiative=6, squad="A", actions=["scout", "attack", "recon", "conceal"], can_act=True):
        self.initiative = initiative
        self.squad = squad
        self.actions = actions
        self.can_act = can_act
        self.shield = 5
        self.postion = None

    def set_position(self, position):
        self.postion = position

    def attack(self, enemy_shield):
        return np.any(dice_roll(1) > enemy_shield) 


class Rifleman:
    def __init__(self, initiative=5, squad="A", actions=["move", "attack", "control"], can_act=True):
        self.initiative = initiative 
        self.squad = squad
        self.actions = actions
        self.can_act = can_act
        self.shield = 4
        self.postion = None

    def set_position(self, position):
        self.postion = position

    def attack(self, enemy_shield):
        return np.any(dice_roll(1) > enemy_shield) 


class Leader:
    def __init__(self, initiative=7, squad="A", actions=["bolster", "inspire"]):
        self.initiative = initiative 
        self.squad = squad


class Gunners:
    def __init__(self, initiative=3, squad="A", actions=["move", "attack", "suppress"], can_act=True):
        self.initiative = initiative
        self.squad = squad
        self.actions = actions
        self.can_act = can_act
        self.shield = 4
        self.postion = None

    def set_position(self, position):
        self.postion = position

    def attack(self, enemy_shield):
        return np.any(dice_roll(2) > enemy_shield) 

    def supress(self, enemy_shield):
        return np.any(dice_roll(4) > enemy_shield) 


class Snipers:
    def __init__(self, initiative=4, actions=["stalk", "attack"], can_act=True):
        self.initiative = initiative
        self.actions = actions
        self.can_act = can_act
        self.shield = 6
        self.postion = None

    def set_position(self, position):
        self.postion = position


class Sergeant:
    def __init__(self, initiative=9, actions=["bolster", "command"]):
        self.initiative = initiative
        self.actions = actions


class Guide:
    pass


class Montar:
    pass


class Fog:
    def __init__(self):
        self.initiative = 1

