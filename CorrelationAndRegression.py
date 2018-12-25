import pickle

pkl_file = open('name/Deg-coll-F.pkl', 'rb')
DegF= pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('name/Deg-coll-M.pkl', 'rb')
DegM= pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('name/SumClusteringF.pkl', 'rb')
ClusF= pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('name/SumClusteringM.pkl', 'rb')
ClusM= pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('name/SumEigenvectorF.pkl', 'rb')
EigF= pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('name/SumEigenvectorM.pkl', 'rb')
EigM= pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('name/SumEfficiencyF.pkl', 'rb')
EffF= pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('name/SumEfficiencyM.pkl', 'rb')
EffM= pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('name/SumKcoreF.pkl', 'rb')
KcoF= pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('name/SumKcoreM.pkl', 'rb')
KcoM= pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('name/deg.pkl', 'rb')
deg= pickle.load(pkl_file)
pkl_file.close()


import numpy as np
def fun(di):
    ar=np.array(list(di.values()))
    m=np.mean(ar)
    s=np.std(ar)
    for i in di.keys():
        di[i]=(di.get(i)-m)/s
fun(DegF)
fun(DegM)
fun(ClusF)
fun(ClusM)
fun(EigF)
fun(EigM)
fun(EffF)
fun(EffM)
fun(KcoF)
fun(KcoM)
fun(deg)


datacollF=[]
datacollM=[]
for i in DegF.keys():
    if i in ClusF.keys():
        if i in EigF.keys():
            if i in EffF.keys():
                if i in KcoF.keys():
                    if i in deg.keys():
                        datacollF.append((i,deg[i],DegF[i],ClusF[i],EigF[i],EffF[i],KcoF[i]))
for i in DegM.keys():
    if i in ClusM.keys():
        if i in EigM.keys():
            if i in EffM.keys():
                if i in KcoM.keys():
                    if i in deg.keys():
                        datacollM.append((i,deg[i],DegM[i],ClusM[i],EigM[i],EffM[i],KcoM[i]))
                        
import csv

Data = [('Name','Citation_Count','Degree_Centrality','Clustering_Coefficient','Eigenvector_Centrality','Efficiency','K_core')]
#Data = [('Name','CC','DC','Clus','Eig','Eff','K')]

Data = Data+datacollF

with open('RP/Female.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(Data)

csvFile.close()


Data = [('Name','Citation_Count','Degree_Centrality','Clustering_Coefficient','Eigenvector_Centrality','Efficiency','K_core')]

#Data = [('Name','CC','DC','Clus','Eig','Eff','K')]

Data = Data+datacollM

with open('RP/Male.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(Data)

csvFile.close()

import pandas as pd
df = pd.read_csv('RP/Male.csv')

housing_model = ols("""Citation_Count ~ Degree_Centrality + Efficiency""", data=df).fit()
housing_model_summary = housing_model.summary()
HTML(
(housing_model_summary
    .as_html()
    .replace('<th>  Adj. R-squared:    </th>', '<th style="background-color:#aec7e8;"> Adj. R-squared: </th>')
    .replace('<th>coef</th>', '<th style="background-color:#ffbb78;">coef</th>')
    .replace('<th>std err</th>', '<th style="background-color:#c7e9c0;">std err</th>')
    .replace('<th>P>|t|</th>', '<th style="background-color:#bcbddc;">P>|t|</th>')
    .replace('<th>[0.025</th>    <th>0.975]</th>', '<th style="background-color:#ff9896;">[0.025</th>    <th style="background-color:#ff9896;">0.975]</th>'))
)

df.corr(method='pearson')

dff = pd.read_csv('RP/Female.csv')

dff.corr(method='pearson')

housing_model = ols("""Citation_Count ~ Degree_Centrality + Efficiency""", data=dff).fit()
housing_model_summary = housing_model.summary()
from IPython.display import HTML, display
HTML(
(housing_model_summary
    .as_html()
    .replace('<th>  Adj. R-squared:    </th>', '<th style="background-color:#aec7e8;"> Adj. R-squared: </th>')
    .replace('<th>coef</th>', '<th style="background-color:#ffbb78;">coef</th>')
    .replace('<th>std err</th>', '<th style="background-color:#c7e9c0;">std err</th>')
    .replace('<th>P>|t|</th>', '<th style="background-color:#bcbddc;">P>|t|</th>')
    .replace('<th>[0.025</th>    <th>0.975]</th>', '<th style="background-color:#ff9896;">[0.025</th>    <th style="background-color:#ff9896;">0.975]</th>'))
)
