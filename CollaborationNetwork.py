import os
import json

def funcol():
    coll_list=[]
    for root, dirs, files in os.walk('aps-dataset-metadata-2016'):
         for name in files:
            try:
                 if name.endswith((".json")):
                    with open(os.path.join(root,name), 'r') as f:
                        data = json.load(f)
                        if 'authors'in data:
                            s=data.get('authors')
                            firstlist=[]
                            lastlist=[]
                            fulllist=[]
                            for i in range(0,len(s)):
                                if 'firstname' in s[i]:
                                    fi=s[i].get('firstname')
                                    if fi.isspace() or fi=='':
                                            firstlist.append('NNN')
                                    else:
                                        firstlist.append(fi)
                                else: 
                                    firstlist.append('NNN')
                                if 'surname' in s[i]:
                                    su=s[i].get('surname')
                                    if su:
                                        lastlist.append(su)
                                    else:
                                        lastlist.append('NNN')
                                else: 
                                    lastlist.append('NNN')
                            for w in range(0,len(lastlist)):
                                fulllist.append(firstlist[w]+'+'+lastlist[w])
                            for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            coll_list.append((fulllist[h],fulllist[l]))
            except :
                continue
    return coll_list
            
collaborationlist=funcol()
collaborationlist=set(collaborationlist)
  

import pickle

output = open('Collaboration/data/collaborationlist.pkl', 'wb')
pickle.dump(collaborationlist, output)
output.close()
