import yaml
import os 
from collections import defaultdict
    

class Concentration:
    def __init__(self, nation, troops = ["ALL"]):
        self.nation = nation 
        self.troops = troops 
    
    def to_string(self):
        return f"Concentration marker from nation {self.nation} for troops {self.troops}"

class Scoutted:
    def __init__(self, nation):
        self.nation = nation

    def to_string(self):
        return f"Scoutted marker from nation {self.nation}"


class Controlled:
    def __init__(self, nation, control_status) -> None:
        self.nation = nation
        self.controlled = control_status

    def update_status(self, game_state):
        pass

    def to_string(self):
        return f"Controlled marker from nation {self.nation} with controlled status {self.controlled}"

class Aim:
    def __init__(self, nation):
        self.nation = nation

    def update_status(self, game_state):
        pass

    def to_string(self):
        return f"Aim marker for nation {self.nation}"

class Objective:
    def __init__(self, value) -> None:
        self.value = value

    def to_string(self):
        return f"Objective marker value {self.value}"

class MarkerManager:
    def __init__(self, conf_filepath):
        self.conf_filepath = conf_filepath
        self._markers_by_tile = defaultdict(lambda : defaultdict(list)) 
        with open(self.conf_filepath, 'r') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
            self.starting_game_markers(data.get('Markers', {}))


    def starting_game_markers(self, in_markers_dict):

        objective_markers = in_markers_dict.get("Objective", {})
        for position, value in objective_markers.items():
            marker = Objective(value)
            self._markers_by_tile[position]["Objective"].append(marker)

        concentration_markers = in_markers_dict.get("Concentration", {})
        for nation, markers in concentration_markers.items():
            for position, troop in markers.items():
                marker = Concentration(nation, troop)
                self._markers_by_tile[position]["Concentration"].append(marker)

        scoutted_markers = in_markers_dict.get("Scoutted", {})
        for nation, position_list in scoutted_markers.items():
            for position  in position_list:
                marker = Scoutted(nation)
                self._markers_by_tile[position]["Scoutted"].append(marker)

        controlled_markers = in_markers_dict.get("Controlled", {})
        for nation, position_list in controlled_markers.items():
            for position in position_list:
                marker = Controlled(nation, True)
                self._markers_by_tile[position]["Controlled"].append(marker)


    def to_string(self):
        for position, types_dict in self._markers_by_tile.items():
            print(f"{position}:")
            for marker_type, markers in types_dict.items():
                print(f"\t{marker_type}:")
                for m in markers:
                    print('\t\t', m.to_string())


