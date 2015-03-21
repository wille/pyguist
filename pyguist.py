from lang import Language

languages = []

with open("languages.yml") as f:
    content = f.readlines()
    
    extensions = []
    lang = None
    langc = None
    
    for line in content:
        if line.startswith("  - "):
            extension = line.replace("  - .", "")
            extensions.append(extension)
        elif line.startswith(" "):
            continue
        else:
            if not langc is None:
                langc.extensions = extensions
            line = line.replace(":", "").strip()
            if len(line) > 0:
                langc = Language(line)
                print("Creating language: " + line)
                languages.append(langc)
                extensions = []
            
for l in languages:
    pass