import os
import json
from collections import defaultdict
import networkx as nx
import pickle

pkl_file = open('name/data/genderdict.pkl', 'rb')
namedict = pickle.load(pkl_file)
pkl_file.close()

def funcol():
    S = defaultdict(list)
    for root, dirs, files in os.walk('aps-dataset-metadata-2016'):
         for name in files:
            try:
                 if name.endswith((".json")):
                    with open(os.path.join(root,name), 'r') as f:
                        data = json.load(f)
                        date=data.get('date')
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
                            
                            if date<="1975-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[1975].append((fulllist[h],fulllist[l]))

                            if date<="1980-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[1980].append((fulllist[h],fulllist[l]))

                            if date<="1985-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[1985].append((fulllist[h],fulllist[l]))

                            if date<="1990-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[1990].append((fulllist[h],fulllist[l]))
                                            
                            if date<="1995-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[1995].append((fulllist[h],fulllist[l]))
                                            
                            if date<="2000-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[2000].append((fulllist[h],fulllist[l]))
                                            
                            if date<="2005-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[2005].append((fulllist[h],fulllist[l]))
                                            
                            if date<="2010-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[2010].append((fulllist[h],fulllist[l]))
                                            
                            if date<="2017-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[2016].append((fulllist[h],fulllist[l]))
            except :
                continue
    return S

collaborationlist=funcol()

def per5year(year):
    G=nx.Graph()
    G.add_edges_from(collaborationlist[year])
    LCC=max(nx.connected_component_subgraphs(G), key=len)

    for i in LCC.nodes():
        LCC.node[i]['gender']=namedict.get(i)

    NumF=0
    NumM=0

    for i in LCC.nodes():
        if  LCC.node[i]['gender']=='female':
            NumF=NumF+1
        if  LCC.node[i]['gender']=='male':
            NumM=NumM+1

    return (year,NumF,NumM,NumM/NumF)

MaleToFemaleRatio=[]
for i in collaborationlist.keys():
    MaleToFemaleRatio.append(per5year(i))

output = open('CollaborationProject/data/MaleToFemaleRatio.pkl', 'wb')
pickle.dump(MaleToFemaleRatio, output)
output.close()
