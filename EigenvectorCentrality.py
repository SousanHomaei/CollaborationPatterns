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

eigenvector=nx.eigenvector_centrality(LCC)

nx.set_node_attributes(LCC, 'deg', eigenvector)

SumEigenvectorF={}
SumEigenvectorM={}

for i in LCC.nodes():
    if  LCC.node[i]['gender']=='female':
            SumEigenvectorF[i]=LCC.node[i]['deg']
    if  LCC.node[i]['gender']=='male':
            SumEigenvectorM[i]=LCC.node[i]['deg']
            
output = open('Collaboration/data/SumEigenvectorF.pkl', 'wb')
pickle.dump(SumEigenvectorF, output)
output.close()

output = open('Collaboration/data/SumEigenvectorM.pkl', 'wb')
pickle.dump(SumEigenvectorM, output)
output.close()
