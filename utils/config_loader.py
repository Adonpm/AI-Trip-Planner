import yaml

def load_config(config_path:str = "config/config.yaml") -> dict:
    '''Loads config file and returns as a dictionary'''
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        print(config)
    return config
