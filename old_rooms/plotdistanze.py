#script per plottare i valori delle distanze partendo da file in formato csv

import glob
import matplotlib.pyplot as plt
import numpy as np
import csv

#prende la lista dei file csv nel percorso specificato e li ordina in ordine alfabetico, nella cartella specificata mi aspetto di avere 6 file csv, ovvero: cluster configuration, distanze medie e varianza delle distanze nei cluster generali e altri tre file come questi ma per i sottografi di ciascun grafo raggruppati a seconda del cluster di appartenenza (ovviamente questa cosa si puo' cambiare a piacimento, io per il momento l'ho fatto cosi')
files = glob.glob("/home/mattia/Desktop/filecsv/*.csv")
files.sort()

for i in range(len(files)):
	#legge un file csv
	reader=csv.reader(open(files[i],"rb"),delimiter=',')
	x=list(reader)
	
	#il primo e il quarto file della lista di file ordinata sono le cluster configuration, quindi come tipo scelgo int, mentre invece gli altri file sono distanze medie e varianze delle distanze quindi scelgo float
	if(i == 0 or i == 3):
		result=np.array(x).astype('int')
	else:
		result=np.array(x).astype('float')
	
	#preparo percorso per output, e' uguale all'input solo che al posto di .csv metto .png
	tmp = files[i]
    out = tmp[0:-3] + "png"
	
	#i file che iniziano con "C_" sono relativi ai cluster generali, quindi sono degli array monodimensionali (escludendo la prima riga, che contiene solamente gli indici dei cluster), quindi per loro plotto un istogramma (per plottare una heatmap e' necessario un array bidimensionale) mentre invece i file che iniziano per "G_" sono relativi ai sottografi di ciascun grafo raggruppati a seconda del cluster di appartenenza, quindi sono delle matrici, quindi per loro plotto una heatmap; ovviamente gli indici di selezione vanno cambiati se cambia il percorso in cui sono salvati i file csv
	if(tmp[29:31] == "C_"):
		data = result[1,:]
		plt.bar(range(1,len(data)+1), data)
		plt.savefig(out)
		plt.close()
	elif(tmp[29:31] == "G_"):
		data = result[1:,1:]
		x_labels = list(result[0,1:])
		y_labels = list(result[1:,0])
		fig, ax = plt.subplots()
		heatmap = ax.pcolor(data, cmap=plt.cm.hot)
		fig = plt.gcf()
		fig.set_size_inches(8, 11)
		ax.set_yticks(np.arange(data.shape[0]) + 0.5, minor=False)
		ax.set_xticks(np.arange(data.shape[1]) + 0.5, minor=False)
		ax.invert_yaxis()
		ax.xaxis.tick_top()
		ax.set_xticklabels(x_labels, minor=False)
		ax.set_yticklabels(y_labels, minor=False)
		plt.xticks(rotation=90)
		plt.savefig(out)
		plt.close()

