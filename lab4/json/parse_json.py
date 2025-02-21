import json

with open("sample-data.json") as f:
    data = json.load(f)["imdata"]

print("DN                                   Speed   MTU")
print("-" * 50)

for item in data:
    attr = item["l1PhysIf"]["attributes"]
    print(attr["dn"], attr.get("speed", "N/A"), attr.get("mtu", "N/A"))
