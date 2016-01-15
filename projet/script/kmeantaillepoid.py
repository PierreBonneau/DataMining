"""
script provenant de tulip utilisant en entrée un graph tulip généré à partir des fichier csv de l'entrepot de donné et générant une visualisation de  graph sur tulip et un fichier csv contenant les id des protéines et les numéros de cluster

"""
# Powered by Python 2.7

# To cancel the modifications performed by the script
# on the current graph, click on the undo button.

# Some useful keyboards shortcuts : 
#   * Ctrl + D : comment selected lines.
#   * Ctrl + Shift + D  : uncomment selected lines.
#   * Ctrl + I : indent selected lines.
#   * Ctrl + Shift + I  : unindent selected lines.
#   * Ctrl + Return  : run script.
#   * Ctrl + F  : find selected text.
#   * Ctrl + R  : replace selected text.
#   * Ctrl + Space  : show auto-completion dialog.

from tulip import *
import scipy.cluster.vq as sp
import scipy.spatial.distance as spj
from math import sqrt

# the updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# the pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# the runGraphScript(scriptFile, graph) function can be called to launch another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# the main(graph) function must be defined 
# to run the script on the current graph

tab_n=[]
tab2=[]

def main(graph): 
	id_ = graph.getIntegerProperty("id")
	id_fonction = graph.getStringProperty("id_fonction")
	id_interaction = graph.getStringProperty("id_interaction")
	id_seq = graph.getStringProperty("id_seq")
	longueur = graph.getIntegerProperty("longueur")
	masse = graph.getIntegerProperty("masse")
	kmean=graph.getIntegerProperty("kmean")
	nom = graph.getStringProperty("nom")
	sequence = graph.getStringProperty("sequence")
	organisme = graph.getStringProperty("organisme")
	viewBorderColor = graph.getColorProperty("viewBorderColor")
	viewBorderWidth = graph.getDoubleProperty("viewBorderWidth")
	viewColor = graph.getColorProperty("viewColor")
	viewFont = graph.getStringProperty("viewFont")
	viewFontAwesomeIcon = graph.getStringProperty("viewFontAwesomeIcon")
	viewFontSize = graph.getIntegerProperty("viewFontSize")
	viewLabel = graph.getStringProperty("viewLabel")
	viewLabelBorderColor = graph.getColorProperty("viewLabelBorderColor")
	viewLabelBorderWidth = graph.getDoubleProperty("viewLabelBorderWidth")
	viewLabelColor = graph.getColorProperty("viewLabelColor")
	viewLabelPosition = graph.getIntegerProperty("viewLabelPosition")
	viewLayout = graph.getLayoutProperty("viewLayout")
	viewMetric = graph.getDoubleProperty("viewMetric")
	viewRotation = graph.getDoubleProperty("viewRotation")
	viewSelection = graph.getBooleanProperty("viewSelection")
	viewShape = graph.getIntegerProperty("viewShape")
	viewSize = graph.getSizeProperty("viewSize")
	viewSrcAnchorShape = graph.getIntegerProperty("viewSrcAnchorShape")
	viewSrcAnchorSize = graph.getSizeProperty("viewSrcAnchorSize")
	viewTexture = graph.getStringProperty("viewTexture")
	viewTgtAnchorShape = graph.getIntegerProperty("viewTgtAnchorShape")
	viewTgtAnchorSize = graph.getSizeProperty("viewTgtAnchorSize")
	kmean_d(graph,masse,longueur, kmean, nom,organisme)
	#create_arbre(graph,masse,longueur,kmean )

def kmean_d(graph,masse,longueur,kmean,nom,organisme):
	viewColor = graph.getColorProperty("viewColor")
	for n in graph.getNodes():
		tmp_tab=[float(masse[n]),float(longueur[n])]
		tab_n.append(tmp_tab)
		tab2.append(n)
	k=15
	
	centroid,label=sp.kmeans2(tab_n,k)	
	
	for i in range (len(tab2)):
		kmean[tab2[i]]=label[i]
	tab_fic=[]	
	grp_cluster=open("grp_cluster","w")
	
	for k in graph.getNodes():
		grp_cluster.write(str(nom[k])+"; ")
		grp_cluster.write(str(kmean[k])+"; ")
		grp_cluster.write(str(organisme[k]))
		grp_cluster.write("\n")

	for j in graph.getNodes():
		for f in range(len(tab_fic)):
			if kmean[j]==0 and f==0:
			
				viewColor[j]=tlp.Color.Red
			elif kmean[j]==1 and f==1:
							
				
				viewColor[j]=tlp.Color.Blue
			elif kmean[j]==2 and f==2:
			
				viewColor[j]=tlp.Color.Green
				
			elif kmean[j]==3 and f==3:
						
			
				viewColor[j]=tlp.Color.Violet
				
			elif kmean[j]==4 and f==4:
				
				viewColor[j]=tlp.Color.White
				
			elif kmean[j]==5 and f==5:
							
				viewColor[j]=tlp.Color.Yellow
			elif kmean[j]==6 and f==6:
							
			
				viewColor[j]=tlp.Color.Black
				
			elif kmean[j]==7 and f==7:
						
			
				viewColor[j]=tlp.Color.Pink
			elif kmean[j]==8 and f==8:
							
				
				viewColor[j]=tlp.Color.Brown
			elif kmean[j]==9 and f==9:
			
				viewColor[j]=tlp.Color.Violet
			elif kmean[j]==10 and f==10:
		
				viewColor[j]=tlp.Color.Green
			elif kmean[j]==11 and f==11:
						
				
				viewColor[j]=tlp.Color.Yellow
			elif kmean[j]==12 and f==12:
					
				
				viewColor[j]=tlp.Color.Black
			elif kmean[j]==13 and f==13:
							
				
				viewColor[j]=tlp.Color.Cyan
			elif kmean[j]==14 and f==14:
				
				viewColor[j]=tlp.Color.Amaranth
			elif kmean[j]==15 and f==15:
			
				viewColor[j]=tlp.Color.Blue
			
		
	
#def create_subgraph(graph, var3 ,var2 , var ):
#	for n in graph.getNodes():
#		
#		if var[n]==0:
#			graph.addSubGraph(name="cluster"+str(var[n]))
#		if var[n] !=0:
#			graph.addSubGraph(name="cluster"+str(var[n]))
					
	
