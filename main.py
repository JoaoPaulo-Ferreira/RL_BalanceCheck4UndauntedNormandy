from src.environment.EnvironmentState import EnvironmentManager

if __name__ == '__main__':

    from dotenv import load_dotenv
    load_dotenv()
    print("create manager")
    manager = EnvironmentManager()
    manager.map.to_string()
    print("\n\nMarker manager\n\n")
    manager.markers.to_string()
    try:
        manager.map.get_terrain_shield("12B", "6A")
        manager.map.get_terrain_shield("", "")
    except:
        pass
    manager.map.get_terrain_shield("12B", "7B")


