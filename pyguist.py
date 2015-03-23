from lang import Language
import os
import argparse

argparse = argparse.ArgumentParser()
argparse.add_argument("-d", "--directory", dest = "source")

args = argparse.parse_args()

global source
source = args.source or "."

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

array = {}
total = 0

for root, dirs, files in os.walk(source):
        relroot = os.path.abspath(os.path.join(source))

        for file in files:
            filename = os.path.join(root, file)
            
            for l in languages:
                for ext in l.extensions:
                    if filename.endswith("." + ext):
                        with open(filename) as f:
                            lines = len(f.readlines())
                            total += lines
                        
                        if not l.lang in array:
                            array[l] = 0
                        array[l] += lines
                        
                        l.files += 1
                        
                        
                        
for language in array:
    per = round(100.0 * array[language] / total, 2)
    print(language.lang + ", Files: " + str(language.files) + ", " + str(per) + "%")                        
                        
                        
                        
                        
                        