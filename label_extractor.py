from argparse import ArgumentParser

import csv
import json


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--file", type=str, required=True)
    parser.add_argument("--ref", type=str, required=True)
    args = parser.parse_args()

    lines = []
    custom_labels = {}
    with open(f"out/{args.file}.aux", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            cmd = row[0]
            if "newlabel{" in cmd and ":" in cmd:
                lines.append(cmd.split("newlabel{")[1].split("}")[0])
                custom_labels[lines[-1]] = cmd.split("{{")[1].split("}")[0]

    with open(f"{args.ref}.bib", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 0:
                continue

            cmd = row[0]
            if "@" in cmd and "{" in cmd:
                lines.append(cmd.split("{")[1])

    file_name = f".vscode/labels-{args.file}.code-snippets"
    new_data = {}
    for line in lines:
        new_data[line] = {
            "prefix": line,
            "body": line,
        }

    with open(file_name, "w") as f:
        json.dump(new_data, f, indent=4)

    for cmd, num in custom_labels.items():
        out = "\\customlabel{" + cmd + "}{" + num + "}"
        print(out)
