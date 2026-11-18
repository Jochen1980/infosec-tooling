#!/usr/bin/python3

"""Aufstellung aller Dokumente mit Erstellungs- und Änderungsdatum (CER-351)"""

import os
import re
from datetime import datetime
from packaging.version import Version, parse


def sort_date(date_string):
    """Sort date strings"""
    try:
        return datetime.strptime(date_string, '%d.%m.%Y')
    except ValueError:
        return datetime(1970, 1, 1)


def main():
    """Main function"""
    re_genehmigt = re.compile('\\|.*[Gg]enehmigt.*\\| *?(.+?) *?\\|')
    re_version = re.compile('^- .*?(\\d+\\.\\d+) vom (\\d\\d\\.\\d\\d\\.\\d\\d\\d?\\d?).*')

    filepaths = []

    richtlinien_root = "../richtlinien"
    richtlinien = []
    os.walk(richtlinien_root)
    for path, _, files in os.walk(richtlinien_root):
        for file in files:
            if file.endswith(".md") and "template" not in file.lower():
                filepaths.append(os.path.join(path, file))

    filepaths.append("../informationssicherheitsleitlinie.md")
    filepaths.append("../risikomanagement.md")

    for filepath in filepaths:
        with open(filepath, encoding='utf-8') as md:
            richtlinie = {"pfad": filepath[3:]}
            data = md.readlines()
        richtlinie["titel"] = data[0].rstrip()[2:]
        richtlinie["version"] = ""
        richtlinie["version_datum"] = ""
        richtlinie["genehmigt"] = ""
        version = Version("0.0")
        valid1 = False
        valid2 = False
        for line in data[1:]:
            m1 = re.match(re_genehmigt, line)
            if m1:
                richtlinie["genehmigt"] = m1.group(1)
                valid1 = True
            m2 = re.match(re_version, line)
            if m2:
                line_version = parse(m2.group(1))
                if line_version > version:
                    version = line_version
                    richtlinie["version"] = m2.group(1)
                    richtlinie["version_datum"] = m2.group(2)
                    valid2 = True

        if not valid1 or not valid2:
            print(f'Warning: Incomplete information for document: {filepath}')

        richtlinien.append(richtlinie)

    richtlinien = sorted(richtlinien, key=lambda k: sort_date(k['version_datum']), reverse=True)
    with open('../dokumente.md', 'w', encoding='utf-8') as o:
        o.write('# Dokumentenübersicht\n\n')
        o.write('Autogenerierte Liste '
                f'(Stand: {datetime.strftime(datetime.now().date(), "%d.%m.%Y")}).\n\n')
        o.write('| Dokument | Datum | Genehmigungen |\n')
        o.write('| --- | --- | --- |\n')
        for r in richtlinien:
            o.write(f'| [{r["titel"]}]({r["pfad"]}) | {r["version_datum"]} | {r["genehmigt"]} |\n')


if __name__ == '__main__':
    main()
