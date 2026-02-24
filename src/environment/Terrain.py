import yaml
import os 
import networkx as nx


class Tile:
    
    def __init__(self, name, inner_shield = 0, outter_shield = 0) -> None:
        self.name = name
        self.outter_shield = outter_shield
        self.inner_shield = inner_shield
    
    def set_inner_shield(self, shield_val:int):
        if shield_val >= 0:
            self.inner_shield = shield_val

    def set_outter_shield(self, shield_val:int):
        if shield_val >= 0:
            self.outter_shield = shield_val
    
    def get_shield(self):
        return self.inner_shield, self.outter_shield


class Map:

    def __init__(self, conf_all_tiles, conf_map) -> None:
        self.all_tile_filepath = conf_all_tiles
        self.current_map_filepath = conf_map
        self.scenario_name = ""
        self.TileMap = {}
        self.adjacency = nx.Graph() 
        self._load_all_tiles()
    
    def get_distance(self, tile_origin, tile_destiny):
        return nx.shortest_path_length(self.adjacency, source=tile_origin, target=tile_destiny)
    
    def get_shield(self, position):
        return self.TileMap[position].get_shield() 

    def _load_all_tiles(self):
        with open(self.all_tile_filepath, 'r') as f:
            self.all_tiles = yaml.load(f, Loader=yaml.SafeLoader)
        self.load_map()

    def add_tile(self, tile_name, inner_shield, outter_shield):
        self.TileMap[tile_name] = Tile(name = tile_name, inner_shield = inner_shield, outter_shield = outter_shield)

    def are_connected(self, tile_1, tile_2):
        return self.adjacency.has_edge(tile_1, tile_2)

    def add_path(self, tile_origin, tile_destiny):
        if isinstance(tile_destiny, str) and not self.are_connected(tile_origin, tile_destiny):
            self.adjacency.add_edge(tile_origin, tile_destiny)
        else:
            for destination in tile_destiny:
                if not self.are_connected(tile_origin, destination):
                    self.adjacency.add_edge(tile_origin, destination)

    def load_map(self):
        with open(self.current_map_filepath, 'r') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
    
        tile_list = data.get('Tiles', [])
        adj_list = data.get('Adjacency', [])
        if tile_list == [] or adj_list == []:
            raise RuntimeError("Impossible to load the Map")
        for tile_name in tile_list:
            tile_info = self.all_tiles.get(tile_name)
            self.add_tile(tile_name, **tile_info)

        for origin, adjacents in adj_list.items():
            self.add_path(origin, adjacents)
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

