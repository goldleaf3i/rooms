#script per plottare i valori delle distanze partendo da file in formato csv

import glob
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import csv

#prende la lista dei file csv nel percorso specificato e li ordina in ordine alfabetico, nella cartella specificata mi aspetto di avere 9 file csv, ovvero: cluster configuration, distanze medie e varianza delle distanze nei cluster generali e altri 3 file come questi ma per i sottografi di ciascun grafo raggruppati a seconda del cluster di appartenenza, sia sortati che non, per un totale di altri 6 file (ovviamente questa cosa si puo' cambiare a piacimento, io per il momento l'ho fatto cosi')
files = glob.glob("/home/mattia/Desktop/filecsv/*.csv")
files.sort()

data_dist = 0
data_var = 0

for i in range(len(files)):
	#legge un file csv
	reader=csv.reader(open(files[i],"rb"),delimiter=',')
	x=list(reader)
	
	#il primo, il quarto e il settimo file della lista di file ordinata sono le cluster configuration, quindi come tipo scelgo int, mentre invece gli altri file sono distanze medie e varianze delle distanze quindi scelgo float
	if(i == 0 or i == 3 or i == 6):
		result=np.array(x).astype('int')
	else:
		result=np.array(x).astype('float')
	
	#preparo percorso per output, e' uguale all'input solo che al posto di .csv metto .png
	tmp = files[i]
    out = tmp[0:-3] + "png"
	
	#i file che iniziano con "C_" sono relativi ai cluster generali, quindi sono degli array monodimensionali (escludendo la prima riga, che contiene solamente gli indici dei cluster), quindi per loro plotto un istogramma (per plottare una heatmap e' necessario un array bidimensionale) mentre invece i file che iniziano per "G_" sono relativi ai sottografi di ciascun grafo raggruppati a seconda del cluster di appartenenza, quindi sono delle matrici, quindi per loro plotto una heatmap; ovviamente gli indici di selezione vanno cambiati se cambia il percorso in cui sono salvati i file csv
	if(tmp[29:31] == "C_" and i == 0):
		data = result[1,:]		
		fig = plt.figure()
		ax = fig.add_subplot(111)
		fig.set_size_inches(12, 10)
		ind = np.arange(len(data))
		width = 0.30
		rect = ax.bar(ind, data, width, color='blue')
		ax.set_xlim(-width, len(ind)+width)
		ax.set_ylabel('Numero di sottografi')
		ax.set_xlabel('Indice del cluster')
		ax.set_title('Numero di sottografi di ciascun cluster generale')
		ax.set_xticks(ind + (width/2))
		xTickMarks = range(1, len(data)+1)
		xTickNames = ax.set_xticklabels(xTickMarks)
		plt.setp(xTickNames, rotation=0, fontsize=15)
		plt.savefig(out)
		plt.close()
	elif(tmp[29:31] == "C_" and i == 1):
		data_dist = result[1,:]
	elif(tmp[29:31] == "C_" and i == 2):
		data_var = result[1,:]
		fig = plt.figure()
		ax = fig.add_subplot(111)
		fig.set_size_inches(12, 10)
		ind = np.arange(len(data_dist))
		width = 0.30
		rect1 = ax.bar(ind, data_dist, width, color='green')
		rect2 = ax.bar(ind+width, data_var, width, color='red')
		ax.set_xlim(-width, len(ind)+width)
		ax.set_ylabel('Distanza media e varianza delle distanze')
		ax.set_xlabel('Indice del cluster')
		ax.set_title('Distanza media e varianza distanze dei sottografi di ciascun cluster generale')
		ax.set_xticks(ind + width)
		xTickMarks = range(1, len(data)+1)
		xTickNames = ax.set_xticklabels(xTickMarks)
		plt.setp(xTickNames, rotation=0, fontsize=12)
		ax.legend((rect1[0], rect2[0]), ('Media', 'Var'), loc = 'lower right')
		out = tmp[0:31] + "DistMedie" + tmp[31:]
		out = out[0:-3] + "png"
		plt.savefig(out)
		plt.close()
	elif(tmp[29:31] == "G_"):
		data = result[1:,1:]
		x_labels = list(result[0,1:])
		y_labels = list(result[1:,0])
		fig, ax = plt.subplots()
		heatmap = ax.pcolor(data, cmap = plt.cm.hot)
		fig = plt.gcf()
		fig.set_size_inches(21, 22)
		ax.set_yticks(np.arange(data.shape[0]) + 0.5, minor=False)
		ax.set_xticks(np.arange(data.shape[1]) + 0.5, minor=False)
		ax.invert_yaxis()
		ax.xaxis.tick_top()
		ax.set_xticklabels(x_labels, minor=False)
		ax.set_yticklabels(y_labels, minor=False)
		plt.xticks(rotation=90)
		min_value = np.amin(data) 
		max_value = np.amax(data)
		normalization = mpl.colors.Normalize(vmin = min_value, vmax = max_value)
		cax = fig.add_axes([0.95, 0.2, 0.02, 0.6])
		cb = mpl.colorbar.ColorbarBase(cax, cmap = plt.cm.hot, norm = normalization, spacing = 'proportional')
		ax.set_ylabel('Indice del grafo')
		plt.title('Indice del cluster', x = -22, y = 1.225)
		if(i == 3):
			ax.set_xlabel('Cluster configuration di ciascun grafo')
		elif(i == 4):
			ax.set_xlabel('Distanza media tra i sottografi di ciascun grafo raggruppati a seconda del cluster di appartenenza')
		elif(i == 5):
			ax.set_xlabel('Varianza delle distanze tra i sottografi di ciascun grafo raggruppati a seconda del cluster di appartenenza')
		elif(i == 6):
			ax.set_xlabel('Cluster configuration di ciascun grafo - sorted')
		elif(i == 7):
			ax.set_xlabel('Distanza media tra i sottografi di ciascun grafo raggruppati a seconda del cluster di appartenenza - sorted')
		elif(i == 8):
			ax.set_xlabel('Varianza delle distanze tra i sottografi di ciascun grafo raggruppati a seconda del cluster di appartenenza - sorted')
		plt.savefig(out)
		plt.close()
