import pickle
import networkx as nx  
    
pkl_file = open('name/data/genderdict.pkl', 'rb')
namedict = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('Collaboration/data/collaborationlist.pkl', 'rb')
collaborationlist = pickle.load(pkl_file)
pkl_file.close()

G=nx.Graph()
G.add_edges_from(collaborationlist)    

LCC=max(nx.connected_component_subgraphs(G), key=len)

for i in LCC.nodes():
    LCC.node[i]['gender']=namedict.get(i)

LCC.remove_edges_from(LCC.selfloop_edges())    
kcore=nx.algorithms.core.core_number(LCC)
nx.set_node_attributes(LCC, 'deg', kcore)

SumKcoreF={}
SumKcoreM={}

for i in LCC.nodes():
    if  LCC.node[i]['gender']=='female':
            SumKcoreF[i] =LCC.node[i]['deg']
    if  LCC.node[i]['gender']=='male':
            SumKcoreM[i] =LCC.node[i]['deg']
            

output = open('Collaboration/data/SumKcoreF.pkl', 'wb')
pickle.dump(SumKcoreF, output)
output.close()

output = open('Collaboration/data/SumKcoreM.pkl', 'wb')
pickle.dump(SumKcoreM, output)
output.close()
