"""1. В программу передаётся текст и папка.
    Среди всех текстовых файлов в папке и вложенных папках
    найти файлы, содержащие указанный текст.
"""
import os.path
import os
import re

NEW_YORK = "New York"
T_BONE = "T-bone"
RIB_EYE = "ribeye"


def find_text(dir, text):
    files: list = []
    for r, d, f in os.walk(dir):
        for file in f:
            if file.endswith(".txt"):
                with open(r + r"\\" + file, mode="r", encoding="utf-8") as fp:
                    if re.search(f"{text}", fp.read(), re.IGNORECASE):
                        files.append(r + "\\" + file)

    return files

if __name__=="__main__":
    for i in find_text("root", "new york"):
        print("New York in:", i)

    for i in find_text("root", "ribeye"):
        print("Ribeye in:", i)

    for i in find_text("root", "t-bone"):
        print("T-Bone in:",i)
