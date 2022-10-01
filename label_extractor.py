from argparse import ArgumentParser

import csv
import json
import os


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--name", type=str, required=True)
    args = parser.parse_args()

    lines = []
    with open(f"out/{args.name}.aux", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            cmd = row[0]
            if "newlabel{" in cmd and ":" in cmd:
                lines.append(cmd.split("newlabel{")[1].split("}")[0])

    file_name = f".vscode/labels-{args.name}.code-snippets"
    new_data = {}
    for line in lines:
        new_data[line] = {
            "prefix": line,
            "body": line,
        }
    
    with open(file_name, "w") as f:
        json.dump(new_data, f, indent=4)
