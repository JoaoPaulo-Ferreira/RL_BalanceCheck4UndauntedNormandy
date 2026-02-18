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
        # self.tiles_file = os.getenv('tiles_filepath')
        self.all_tiles = []
        self._load_all_tiles()
    
    def get_shortests_distance(self, tile_origin, tile_destiny):
        return nx.shortest_path_length(self.adjacency, source=tile_origin, target=tile_destiny)

    def _load_all_tiles(self):
        with open(os.getenv('tiles_filepath'), 'r') as f:
            self.all_tiles = yaml.load(f, Loader=yaml.SafeLoader)

    def load_map(self, conf_path):
        with open(conf_path, 'r') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
    
        map_name = data.get('Name', 'Default_name')
        tile_list = data.get('Tiles', [])
        adj_list = data.get('Adjacency', [])
        markers = data.get('Markers', [])
        if tile_list == [] or adj_list == [] or markers == []:
            raise RuntimeError("Impossible to load the Map")
        print(self.all_tiles)
        print(tile_list)
        print(adj_list)
        print(markers)
        print("all_tiles:\n", self.all_tiles)
        print('Loading Map -> Tiles...')
        for tile_name in tile_list:
            # print(f"tile_name: {tile_name}")
            # print(f"self.all_tiles.get('tile_name'): {self.all_tiles.get(tile_name)}")
            tile_info = self.all_tiles.get(tile_name)
            # print('tile_info: ', tile_info)
            outter_shield = tile_info.get('outter_shield')
            inner_shield = tile_info.get('inner_shield')
            self.TileMap[tile_name] = Tile(name=tile_name, inner_s = inner_shield, outter_s = outter_shield)
            # self.TileMap[tile] = Tile(name=tile_list, inner_s = inner_shield, outter_s = outter_shield)

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
    map.load_map(os.getenv('map1_filepath'))
    map.to_string()
    print(map.get_shortests_distance('11B', '2B'))
    print(map.get_shortests_distance('7A', '6A'))
