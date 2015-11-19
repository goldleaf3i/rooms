********************************
Il codice di tsne è completo e funzionante, prende come input due file ".txt":
1) la matrice M di similarità tra i sottografi
2) l'array A di etichette dei cluster di ogni sottografo; l'elemento A(i) è l'etichetta del cluster del sottografo i,
questo sottografo nella matrice di similarità M corrisponde alla riga-colonna i.
********************************
In plotAll.py in fondo ho aggiunto il codice che dalla directory corrente prende in input tutti i file:
"grafo_i_topological.xml": è xml di tipo topological generato con l'applicazione floorplans
e un file
"tipologiaEdilizia.xml": è xml a https://github.com/goldleaf3i/rooms/blob/master/XML%20standard/labels/school.xml
e https://github.com/goldleaf3i/rooms/blob/master/XML%20standard/labels/office.xml

e per ogni grafo_i chiama la funzione loadXML2('grafo_i_topological.xml', 'tipologiaEdilizia.xml') che restituisce la
matrice di quel grafo, con la diagonale fatta dalle etichette delle stanze. Alla fine stampa la matrice in formato ".csv".

loadXML2 è una funzione che si trova in loadGraph.py che parsa i file xml "topological",
esiste anche loadXML che parsa i file xml "non topological"
********************************
Ho cambiato myDictionaries.py per considerare le nuove etichette.
In sostanza nel dizionario labels_java2012toMatlab_Dict ho aggiunto:
'Y':10,
'I':11,
'L':12,
'Z':13,
'G':14,
'Q':15,
'T':16,
'W':17,
'A':18,
'J':19,
'U':20
Il mapping di sopra serve ed è così anche in MATLAB.
Nel dizionario labels_RC_java2012 ho aggiunto:
'Y':'R',
'I':'R',
'L':'C',
'Z':'R',
'G':'R',
'Q':'R',
'T':'R',
'W':'C',
'A':'R',
'J':'R',
'U':'R'
Nel dizionario labelsPriority_java2012toMatlab_Dict ho aggiunto:
'Y': 3,
'I': 3,
'L': 1,
'Z': 3,
'G': 3,
'Q': 3,
'T': 3,
'W': 1,
'A': 3,
'J': 3,
'U': 3
********************************
Bisognerebbe considerare il plot dei grafi di connessione tra i cluster, quelli con i nodi etichettati dai cluster.
Le etichette dei cluster in Matlab sono progressive {1,2,3,4,...,numero_totale_cluster}.
********************************
All'indirizzo
https://bitbucket.org/goldleaf3i/generativespectralgraphs/src/f77b2230028e2e4f722cf85b6c564e25787dd177/script%20python%20per%20plot%20grafi/GraphMetrics/?at=master
c'è il codice che fa plot dei grafi rappresentati con Betweenness, Closeness, Local clustering.
--------------------------------------------------------------------
In share/GraphTool.py c'è la funzione
graph = createGraphTool(topologicalMap)
che converte l'oggetto topologicalMap in un oggetto graph utilizzato da graph-tool

In share/GraphTool.py c'è la funzione
plotGraphTool(graph, filename), dove filename è in nome del grafo (esempio 'graph1'),
che plotta il grafo con Betweenness, Closeness, Local clustering, utilizzando le funzioni
plotGraphToolBetweenness(graph, pos, filename)
plotGraphToolCloseness(graph, pos, filename)
plotGraphToolLocalClustering(graph, pos, filename)
rispettivamente
--------------------------------------------------------------------
In share/IGraph.py c'è la funzione
createIGraph(topologicalMap)
che converte l'oggetto topologicalMap in un oggetto graph utilizzato da igraph

In share/IGraph.py c'è la funzione
plotIGraph(graph, filename)
che plotta il grafo normale e senza metriche locali sui nodi tramite igraph
--------------------------------------------------------------------
In share/rooms.py ho cambiato leggermente la classe topologicalMap passando al costruttore
tool=ToolDict[0]
per dirgli di creare un oggetto grafo nel formato di graph-tool oppure nel formato di igraph, la creazione di questo oggetto
viene fatta nella funzione della classe topologicalMap 
createGraph(self)
--------------------------------------------------------------------
In utils.py c'è il dizionario
ToolDict = {
    0: 'igraph',
    1: 'graph-tool',
 }
che viene utilizzato nella funzione plot/plotGraph/plotAdiacency(filename, tool=ToolDict[0]) per decidere
quale tool utilizzare per plottare (graph-tool oppure igraph).
plotAdiacency viene richiamata da plot/plotAll/plotGraphs(direct) per plottare tutti i grafi in formato ".txt"
presenti nel path corrente.
--------------------------------------------------------------------
share/labelDictionaries.py sarebbe il myDictionaries, l'ho solo rinominato.
--------------------------------------------------------------------
