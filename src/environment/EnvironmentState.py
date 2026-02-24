import os 

from src.environment.Terrain import Map
from src.environment.Markers import MarkerManager 


class EnvironmentManager:
    def __init__(self) -> None:
        self.map = Map(os.getenv('tiles_filepath'), os.getenv('map1_filepath'))
        self.markers = MarkerManager(os.getenv('map1_filepath'))

