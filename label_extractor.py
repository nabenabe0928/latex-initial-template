from argparse import ArgumentParser

import csv
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
                lines.append(["- " + cmd.split("newlabel{")[1].split("}")[0]])

    os.makedirs("labels/", exist_ok=True)
    with open(f"labels/{args.name}.md", "w") as f:
        writer = csv.writer(f)
        writer.writerows(lines)
