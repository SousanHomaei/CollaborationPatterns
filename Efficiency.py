import pickle
import networkx as nx  

from itertools import permutations

def efficiency(G, u, v):
    
    try:
        eff = 1 / nx.shortest_path_length(G, u, v)
    except NetworkXNoPath:
        eff = 0
    return eff

def global_efficiency(G):
    
    n = len(G)
    denom = n * (n - 1)
    if denom != 0:
        g_eff = sum(efficiency(G, u, v) for u, v in permutations(G, 2)) / denom
    else:
        g_eff = 0
    return g_eff

    
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

SumEfficiencyF={}
SumEfficiencyM={}

for i in LCC.nodes():
    x=global_efficiency(nx.ego_graph(LCC,i))
    if  LCC.node[i]['gender']=='female':
            SumEfficiencyF[i]=x
    if  LCC.node[i]['gender']=='male':
            SumEfficiencyM[i]=x
            
output = open('Collaboration/data/SumEfficiencyF.pkl', 'wb')
pickle.dump(SumEfficiencyF, output)
output.close()

output = open('Collaboration/data/SumEfficiencyM.pkl', 'wb')
pickle.dump(SumEfficiencyM, output)
output.close()
