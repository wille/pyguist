from lang import Language
import os

languages = []

with open("languages.yml") as f:
    content = f.readlines()
    
    extensions = []
    lang = None
    langc = None
    
    for line in content:
        if line.startswith("  - ."):
            extension = line.replace("  - .", "").strip()
            extensions.append(extension)
        elif line.startswith(" "):
            continue
        else:
            if not langc is None and not langc.lang is None:
                langc.extensions = extensions
            line = line.replace(":", "").strip()
            if len(line) > 0:
                langc = Language(line)
                languages.append(langc)
                extensions = []
            
for l in languages:
    pass

source = "."

for root, dirs, files in os.walk(source):
        relroot = os.path.abspath(os.path.join(source))

        for file in files:
            filename = os.path.join(root, file)
            
            for l in languages:
                for ext in l.extensions:
                    if filename.endswith("." + ext):
                        print("Found: " + filename + ", detected: " + l.lang + ", " + ext)