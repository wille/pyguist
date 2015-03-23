# pyguist

Python script to calculate percentage of different programming languages in a folder

Idea from github linguist, uses languages.yml from linguist

## Synopsis

```
python pyguist.py [--short] <--directory>
```

If not **--directory** is set, will use current directory as working dir
If **--short** is set, will print results like

```
Language:Files:Percentage
XML:1:0.47
YAML:1:97.23
Python:1:2.29
```

If not **--short** is set, will print results like

```
Markdown, Files: 1, 0.83%
XML, Files: 1, 0.47%
YAML, Files: 1, 96.61%
Python, Files: 1, 2.08%
```
