#!/usr/bin/env python3

import requests

template_url = "https://raw.githubusercontent.com/Aethersailor/Custom_OpenClash_Rules/main/cfg/Custom_Clash.ini"
clash_template = "Custom_Clash.ini"

try:
    response = requests.get(template_url)
    response.raise_for_status()
    content = response.text.splitlines()

    modified_lines = []
    old_string = "raw.githubusercontent.com"
    new_string = "gh-proxy.com/raw.githubusercontent.com"
    for line in content:
        if old_string in line:
            modified_line = line.replace(old_string, new_string)
            modified_lines.append(modified_line)
        else:
            modified_lines.append(line)


    with open(clash_template, "w", encoding="utf-8") as file:
        for line in modified_lines:
            file.write(line + '\n');

    print(f"File Save success")
except requests.exceptions.RequestException as error_code:
    print(f"Download failed, error code is: {error_code}")
