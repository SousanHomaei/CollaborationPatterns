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

clustering=nx.clustering(LCC)

nx.set_node_attributes(LCC, 'deg', clustering)

SumClusteringF={}
SumClusteringM={}

for i in LCC.nodes():
    if  LCC.node[i]['gender']=='female':
            SumClusteringF[i]= LCC.node[i]['deg']
    if  LCC.node[i]['gender']=='male':
            SumClusteringM[i]= LCC.node[i]['deg']

output = open('Collaboration/data/SumClusteringF.pkl', 'wb')
pickle.dump(SumClusteringF, output)
output.close()

output = open('Collaboration/data/SumClusteringM.pkl', 'wb')
pickle.dump(SumClusteringM, output)
output.close()
