import yaml

def get_yaml_data(filename, key):
    with open('data/' + filename + '.yml', 'r', encoding='utf-8') as f:
        return yaml.load(f)[key].values()