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

for i in G.nodes():
    G.node[i]['gender']=namedict.get(i)
    
degree_centrality=nx.degree_centrality(G)
nx.set_node_attributes(G, 'deg', degree_centrality)

SumDegF={}
SumDegM={}

for i in G.nodes():
    if  G.node[i]['gender']=='female':
                SumDegF[i]=(G.node[i]['deg'])
    if  G.node[i]['gender']=='male':
                SumDegM[i]=(G.node[i]['deg'])
            

output = open('Collaboration/data/Deg-coll-F.pkl', 'wb')
pickle.dump(SumDegF, output)
output.close()

output = open('Collaboration/data/Deg-coll-M.pkl', 'wb')
pickle.dump(SumDegM, output)
output.close()
