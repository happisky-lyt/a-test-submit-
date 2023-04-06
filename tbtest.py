import os

path = 'labels/'
dirs = os.listdir(path)

count = {'20': 0, '25': 0, '30': 0, '35': 0, '40': 0, '45': 0, '50': 0, '55': 0, '60': 0, '65': 0, '70': 0,
         '75': 0, '80': 0, '85': 0, '90': 0, '95': 0, '100': 0, '105': 0, '110': 0, '115': 0, '120': 0}

for i in range(len(dirs)):
    if dirs[i][-3:] != 'xml':
           key = dirs[i].split('_')[1]
           with open(os.path.join(path, dirs[i]), 'r') as f:
               num_obj = len(f.readlines())
               f.close()
           count[key] += num_obj

print(count)
print(f'The number of objects: {sum(count.values())}')  