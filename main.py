import os 
from src.environment.EnvironmentState import EnvironmentManager
if __name__ == '__main__':

    from dotenv import load_dotenv
    load_dotenv()
    print("create manager")
    manager = EnvironmentManager()
    manager.map.to_string()
    print("\n\nMarker manager\n\n")
    print(manager.markers.to_string())
