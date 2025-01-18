---
tags:
  - 100_Days_of_Code
  - programming
  - python
---
# Day 24: Intermediate - Files, Directories and Paths

## Notes

### Files

inside `my_file.txt`:

```txt
Hello world, I am Jude!
```

#### Read

```python
file = open('my_file.txt')
contents = file.read()
file.close()

print(contents)
```

##### Recommended approach

```python
with open('my_file.txt') as file:
    contents = file.read()

print(contents)
```

#### Write

```python
with open('my_file.txt', mode="w") as file: 
    contents = file.write("New text.") 
    
print(contents)
```

The text on `my_file.txt` will bee overwritten with "New text."

inside `my_file.txt`:

```txt
New text.
```

#### Add

```python
with open('my_file.txt', mode="a") as file: 
    file.write("\nNew text.") 
```

inside `my_file.txt`:

```txt
Hello world, I am Jude!
New text.
```

### Creating a new file

NOTE: `new_file.txt` is not in the directory

```python
with open('new_file.txt', mode="a") as file: 
    file.write("\nNew text.") 
```

inside `new_file.txt`:

```txt

New text.
```

### Paths

**Absolute File path** - is always relative to the root of the computer

**Relative File path** - is relative to your current working directory

![[vlcsnap-2025-01-18-17h25m44s850.png|400]]

#### Navigating into subdirectories

##### If working dir in `Project`

Relative file path: ./talk.ppt

##### If working dir in `Work`

Relative file path: ./Project/talk.ppt

#### Navigating into parent directories

##### If your working dir in `Project`  

Relative path: ../report.doc
