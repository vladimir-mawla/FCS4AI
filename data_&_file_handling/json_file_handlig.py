# JSON

import json
from pathlib import Path

user = {
    "name": "John",
    "age": 22,
    "skills": ["python", "ml"],
    "active": True,
}
# Writing

# Takes a python dictionary, converts it into JSON, and writes it to a file
path = Path("data/user.json")
path.write_text(json.dumps(user, indent=4))

# Reading JSON
# When we read JSON back, Python converts it into a dictionary again, 
# so we can use it with python
loaded = json.loads(path.read_text())

print(loaded["skills"])


# Modifying and saving again

loaded["age"] = 23
path.write_text(json.dumps(loaded, indent=4))