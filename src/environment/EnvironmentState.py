import yaml
import os 
import networkx as nx

from src.environment.Terrain import Map
from src.environment.Markers import ObjectivePoints, Concentration, Scoutted  

class EnvironmentManager:
    def __init__(self) -> None:
        self.map = Map()
        self.objective_points = 0
        self.Concentration = 0
        self.Scoutted = 0
        self._load_all_tiles()

    def _load_all_tiles(self):
        with open(os.getenv('tiles_filepath'), 'r') as f:
            self.all_tiles = yaml.load(f, Loader=yaml.SafeLoader)

    def load_map(self, conf_path):
        with open(conf_path, 'r') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
    
        tile_list = data.get('Tiles', [])
        adj_list = data.get('Adjacency', [])
        if tile_list == [] or adj_list == []:
            raise RuntimeError("Impossible to load the Map")
        print(tile_list)
        print(adj_list)
        print('Loading Map -> Tiles...')
        for tile_name in tile_list:
            tile_info = self.all_tiles.get(tile_name)
            self.map.add_tile(tile_name, **tile_info)

        print('Tiles loaded.\n')
        print('Loading Map -> Adjacency...')
        print(adj_list)
        print(adj_list.items())
        for origin, adjacents in adj_list.items():
            print(f"Added adj between {origin} {adjacents}")
            self.map.add_path(origin, adjacents)
        if nx.is_connected(self.map.adjacency):
            print('Adjacency loaded.\n')
        else:
            raise RuntimeError("Tiles not reachable inside Map")

    # def to_string(self):
    #     print("Terrain Tiles\n")
    #     for tile_name in self.TileMap.keys():
    #         tile = self.TileMap[tile_name]
    #         print(f"{tile.name}\n\toutter_shield={tile.outter_shield}\n\tinner_shield={tile.inner_shield}")
    #
    #     print("Adjacency graph\n")
    #     for x,y in self.adjacency.edges():
    #         print(f"{x} and {y} are adjacents")
    #
if __name__ == '__main__':

    from dotenv import load_dotenv
    load_dotenv()
    print("create manager")
    manager = EnvironmentManager()
    manager.load_map(os.getenv('map1_filepath'))
