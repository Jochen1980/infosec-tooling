'''

A small tool that generates a compact representation of the SOA
and includes a justification for inclusion or exclusion as
required by ISO27001. '''

import re
import subprocess
import sys
import yaml

# load process oriented structure
with open("../assets/soa_processes.yml","r") as file:
    process_structure = yaml.safe_load(file)
    file.close()

# laod soa rating
with open('../assets/soa_rating.yml',"r") as file:
    rating = yaml.safe_load(file)
    file.close()

# load soa rationale
with open('../assets/soa_rationale.yml',"r") as file:
    rationale = yaml.safe_load(file)
    file.close()

# load compact header
with open('../assets/soa_compact_header.md',"r") as file:
    DOCUMENT_HEADER = "".join(file.readlines())
    file.close()

# load "Erklärung zur Anwendbarkeit"
with open("../erklaerung-zur-anwendbarkeit.md","r", encoding="utf-8") as file:
    lines = file.readlines()
    file.close()

# regular expressions for parsing chapters, comments, tickets
pattern_chapter = re.compile(r"^(#+)\s(A?\d+(.*?))\s(.*?)$")
pattern_comments = re.compile(r"^>.*?assets/c.png.*?`(.+?)`")
pattern_tickets = re.compile(r"^>.*?((CER|OS|CEPH|COM)-?\d+)",re.IGNORECASE)
pattern_empty = re.compile(r"^\s*$")

# state mapping
stat_map = { 0 : "ausgeschlossen",
             1 : "nicht vorhanden",
             2 : "in Bearbeitung",
             3 : "definiert",
             4 : "etabliert",
             5 : "überwacht",
             6 : "verbessert"
             }
# GIT informations
GIT_COMMIT = str(subprocess.check_output("git log -n 1 | head -n 3", shell=True), "UTF-8")
GIT_BRANCH = str(subprocess.check_output("git branch --list | grep '*' | cut -f 2 -d ' '",
                                         shell=True),"UTF-8")

# MD table header for each process
TABLE_HEADER = "| Maßnahme | Beschreibung | Status | Gründe für die Einbeziehung bzw. den Ausschluss | Ticket(s) | Kommentare |\n" + \
               "|----------|--------------|--------|-------------------------------------------------|-----------|------------|"

# helper functions
create_anker = lambda a : a.lower().replace(' ','-').replace('(' ,'').replace(')',''). \
    replace('/','').replace('.','').replace(',','')
yt_link = lambda ticket : f"[{ticket}](https://yt.bi.denbi.de/issue/{ticket})"

# dict containing all controls
controls = {}

# parse "Erklärung zur Anwendbarkeit"
for line in lines:
    ''' 
    Creates a "control" dict for each control (starting with ###).
    A control dict consists of:
    - the number of the control
    - short description of the control
    - a list of comments belonging to the control
    - a list of tickets belonging to the control
    - a state 
    '''
    m = pattern_chapter.match(line)
    if m:
        g = m.groups()
        if len(g[0]) == 2:  # chapter
            pass
        elif len(g[0]) == 3:  # control
            control = {}  # new dict for control
            control['number'] = g[1]
            control["description"] = g[3]
            control["comments"] = set()
            control["tickets"] = []
            # check if rating for this control is set
            if g[1] in rating:
                control["state"] = rating[g[1]]
                if control["state"] not in (1,2,3,4,5,6):
                    sys.exit(f"Key Error : '{control['state']}' is an unsupported value for rating control {g[1]}")
            else: # use default if not
                control["state"] = 5
            # check if rationale for control is set
            if g[1] in rationale:
                control["reason"] = rationale[g[1]]
            # add control dict to dict of controls, with number of control as key
            controls[g[1]] = control
    else:
        # comments
        comment_match = pattern_comments.match(line)
        if comment_match:
            control["comments"].add(comment_match.group(1).lower())
        # tickets
        ticket_match = pattern_tickets.match(line)
        if ticket_match:
            control["tickets"].append(yt_link(ticket_match.group(1)))
            if "CER" in ticket_match.group(2).upper():
                control["state"] = 2

# Generate MarkDown document

# general document header first
print(DOCUMENT_HEADER,"\n")
# additional git information, i.e. to clearify what's the base
# for the generated document
print (f"```\n{GIT_COMMIT}Branch: {GIT_BRANCH}```")

# iterate over all processes
for process in process_structure['processes']:
    # print process header
    print(f"\n## {process['name']}\n")
    print(TABLE_HEADER)
    # print table line for each process
    for control_number in process["controls"]:
        control = controls[control_number]
        print (f"| [{control['number']}](erklaerung-zur-anwendbarkeit.md#{create_anker(control['number']+' '+control['description'])}) | {control['description']} | {stat_map[control['state']]} | {control['reason']} | {','.join(control['tickets'])} | {','.join(control['comments'])} |")

