import behave2cucumber
import json
import os

if __name__ == '__main__':
    with open(os.path.abspath('./reports/behave.json')) as behave_json:
        behave2cucumber.convert(json.load(behave_json))