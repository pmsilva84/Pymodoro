import json
from pathlib import Path


# Path setup
ROOT_FILE = Path(__file__).parent
JSON_FILE = ROOT_FILE / "timers.json"


if __file__ == "__main__":
    
    basic_podomodoro_values = {
                "focusTime" : 25,
                "shortRest" : 5,
                "longRest" : 15,
                "Sequence": ["focusTime","shortRest","focusTime","shortRest","focusTime","longRest"]
            }

    with open(JSON_FILE,"w") as arquivo:
                data = json.dump(basic_podomodoro_values,arquivo,ensure_ascii= False,indent=2)

    with open(JSON_FILE,"r") as arquivo:
                data = json.load(arquivo)

    print(data["focusTime"])
    print(data["shortRest"])
    print(data["longRest"])
  