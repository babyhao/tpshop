import yaml

def data_with_key(key):
    with open('data/test_data.yml', encoding='utf-8') as f:
        return yaml.load(f, yaml.FullLoader)[key].values()