import os
py_files = [i for i in os.listdir() if i.endswith(".py")]

with open('One.py', 'w') as output:
    for i in py_files:
         with open(i,'r') as q:
            output.write('##'*69 + '\n' + '\n')
            output.write(str(q.read()).strip() + '\n'+ '\n')