import re 

with open('new_text.txt','r') as f:
    lines = f.readlines()

with open('new_text_output.txt','w') as f:
    for line in lines:
        if line.strip():
            f.write(line)