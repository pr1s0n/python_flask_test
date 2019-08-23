import pathlib
import yaml

BASE_DAR = pathlib.Path(__file__).parent.parent
config_path = BASE_DAR / 'conf' / 'polls.yaml'
def get_config(path):
	with open(path) as f:
		config = yaml.safe_load(f)
	return config
config = get_config(config_path)