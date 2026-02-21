from abc import ABC, abstractmethod

class Marker(ABC):
    def __init__(self, position):
        self.position = position

    def get_position(self):
        return self.position

    
class StaticMarker(Marker):
    def __init__(self, position):
        super().__init__(position)

    def get_type(self) -> str:
        return "static"


class DynamicMarker(Marker):
    def __init__(self, position):
        super().__init__(position)

    def get_type(self) -> str:
        return "dynamic"

    @abstractmethod
    def update_status(self, game_state):
        pass


class ObjectivePoints(StaticMarker):
    def __init__(self, position, value = 1):
        super().__init__(position)
        self.value = value


class Concentration(StaticMarker):
    def __init__(self, position, player, troops = ["ALL"]):
        super().__init__(position)
        self.player = player
        self.troops = troops 


class Scoutted(DynamicMarker):
    def __init__(self, position, player):
        super().__init__(position)
        self.player = player

    def update_status(self, game_state):
        return super().update_status(game_state)









