import yaml
import os 
import networkx as nx


class Tile:
    
    def __init__(self, name, inner_s = 0, outter_s = 0) -> None:
        self.name = name
        self.outter_shield = outter_s
        self.inner_shield = inner_s
    
    def set_inner_shield(self, shield_val:int):
        if shield_val >= 0:
            self.inner_shield = shield_val

    def set_outter_shield(self, shield_val:int):
        if shield_val >= 0:
            self.outter_shield = shield_val
    
    def get_inner_shield(self):
        return self.inner_shield

    def get_outter_shield(self):
        return self.outter_shield

class Map:
    def __init__(self) -> None:
        self.scenario_name = ""
        self.TileMap = {}
        self.adjacency = 0
    
    def get_distance(self, tile_origin, tile_destiny):
        return nx.shortest_path_length(self.adjacency, source=tile_origin, target=tile_destiny)

    def load_map(self, conf_path):
        with open(conf_path, 'r') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
    
        map_name = data.get('Name', 'Default_name')
        tile_list = data.get('Tiles', [])
        adj_list = data.get('Adjacency', [])
        if tile_list == [] or adj_list == []:
            raise RuntimeError("Impossible to load the Map")

        print('Loading Map -> Tiles...')
        for tile_name, tile_att in tile_list.items():
            outter_shield = tile_att.get('outter_s', -1)
            inner_shield = tile_att.get('inner_s', outter_shield)
            self.TileMap[tile_name] = Tile(name=tile_name, inner_s = inner_shield, outter_s = outter_shield)
            print(tile_list)

        print('Tiles loaded.\n')
        print('Loading Map -> Adjacency...')
        self.adjacency = nx.Graph()
        print(adj_list)
        for origin, adjacents in adj_list.items():
            for destiny in adjacents:
                self.adjacency.add_edge(origin, destiny)
        
        if nx.is_connected(self.adjacency):
            print('Adjacency loaded.\n')
        else:
            raise RuntimeError("Tiles not reachable inside Map")
        

    def to_string(self):
        print("Terrain Tiles\n")
        for tile_name in self.TileMap.keys():
            tile = self.TileMap[tile_name]
            print(f"{tile.name}\n\toutter_shield={tile.outter_shield}\n\tinner_shield={tile.inner_shield}")

        print("Adjacency graph\n")
        for x,y in self.adjacency.edges():
            print(f"{x} and {y} are adjacents")

if __name__ == '__main__':

    from dotenv import load_dotenv
    load_dotenv()
    map = Map()
    map.load_map(os.getenv('file_path'))
    map.to_string()
    print(map.get_distance('A1', 'B2'))
    print(map.get_distance('A1', 'C1'))
