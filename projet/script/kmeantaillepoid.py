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
	kmean_d(graph,masse,longueur, kmean)
	create_arbre(graph,masse,longueur,kmean )

def kmean_d(graph,masse,longueur,kmean):
	viewColor = graph.getColorProperty("viewColor")
	for n in graph.getNodes():
		tmp_tab=[float(masse[n]),float(longueur[n])]
		tab_n.append(tmp_tab)
		tab2.append(n)
	k=sqrt(len(tab2)/2)
	print int(k)
	centroid,label=sp.kmeans2(tab_n,int(k))	
	
	for i in range (len(tab2)):
		kmean[tab2[i]]=label[i]
	for j in graph.getNodes():
		if kmean[j]==0:
			viewColor[j]=tlp.Color.Red
		if kmean[j]==1:
			viewColor[j]=tlp.Color.Blue
		if kmean[j]==2:
			viewColor[j]=tlp.Color.Green
		if kmean[j]==3:
			viewColor[j]=tlp.Color.Violet
		if kmean[j]==4:
			viewColor[j]=tlp.Color.White
		if kmean[j]==5:
			viewColor[j]=tlp.Color.Yellow
		if kmean[j]==6:
			viewColor[j]=tlp.Color.Black
		if kmean[j]==7:
			viewColor[j]=tlp.Color.Pink
		if kmean[j]==8:
			viewColor[j]=tlp.Color.Brown
	
	return k
	
def create_subgraph(graph, var3 ,var2 , var ):
	for n in graph.getNodes():
		
		if var[n]==0:
			graph.addSubGraph(name="cluster"+str(var[n]))
		if var[n] !=0:
			graph.addSubGraph(name="cluster"+str(var[n]))
					
	
