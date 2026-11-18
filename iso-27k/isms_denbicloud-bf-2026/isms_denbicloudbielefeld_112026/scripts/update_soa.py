
import re
import yaml

f = open("../erklaerung-zur-anwendbarkeit.md", encoding="utf-8")
lines = f.readlines()
f.close()

f = open('../assets/soa_rating.yml')
rating = yaml.safe_load(f)
f.close()

f = open('../assets/soa_rationale.yml')
rationale = yaml.safe_load(f)
f.close()

pattern_control = re.compile(r"^(#{4})\s(A?\d+(.*?))\s(.*?)$")
pattern_reason_head = re.compile(r"^|(.*?)|#")
pattern_reason_tail = re.compile(r"^")


def get_rationale(control_id):
    for prefix in rationale:
        if control_id.startswith(prefix):
            return rationale[prefix]


def splitter(text,splitlen,separator):
    start = 0
    newtext = ""
    while (start < len(text)):
        newtext = text[start:len]
    return newtext


for line in lines:
    print(line.rstrip())
    m = pattern_control.match(line)
    if m:
        g = m.groups()
        reason = get_rationale(g[1])
        # depending on  mode the out
        print(f"| {reason} |\n| --- |")

