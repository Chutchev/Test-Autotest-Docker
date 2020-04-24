import behave2cucumber
import json
import os

if __name__ == '__main__':
    with open(os.path.abspath('./reports/behave.json')) as behave_json_file:
        with open(os.path.abspath('./reports/cucu.json'), 'w+') as cucumber_json_file:
            cucumber_json = behave2cucumber.convert(json.load(behave_json_file))
            json.dump(cucumber_json, cucumber_json_file)
