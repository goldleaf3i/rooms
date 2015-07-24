#!/usr/bin/python

# COPIATO DA CARTELLLA DI SVILUPPO 15/9/14

################################################# INIZIO FORMATO salvataggi da file JAVA2012 (MapCREATOR) #################################################
# UFFICI - mappe in Java2012
java_2012_uffici ='''WALLLEFTRIGHT( Colours.WHITE , true, "WallVertical", "_", "_"),
DOORUPDOWN( Colours.WHITE, true, "DoorHorizontal", "_", "_"), 
DOORLEFTRIGHT(Colours.WHITE, true, "DoorVertical", "_", "_"), 
CORRIDOR( Colours.GREEN, false, "Corridor", "C", "C" ), 
SERVICEROOM (Colours.YELLOW, false, "Service", "S", "S"), 
OFFICE( Colours.ORANGE, false, "Office", "M", "M"),
GROUPOFFICE( Colours.RED, false, "GroupOffice", "B", "B"),
OPENSPACE( Colours.RED2, false, "Openspace", "O", "H"), 
MEETINGROOM( Colours.RED3, false, "MeetingRoom", "R", "B"),
CONFERENCEROOM( Colours.ORANGE2, false, "ConferenceRoom", "F", "H"),
HALL( Colours.LIGHTBLUE, false, "Hall", "H", "H"), 
CANTEEN( Colours.LIGHTBLUE2, false, "Canteen", "N", "H"),
DELUXEOFFICE( Colours.PURPLE, false, "DeluxeOffice", "D", "B"),
STAFFROOM( Colours.GREY2, false, "Staff", "K", "M"),'''

# SCUOLE - mappe in Java2012
java_2012_scuole ='''  EMPTY( Colours.WHITE , false, "Empty", "_", "_"), 
  WALLUPDOWN( Colours.WHITE , true, "WallHorizontal", "_", "_"), 
  WALLCORNERUPR( Colours.WHITE , true,"WallCornerUpRight", "_", "_"),
  WALLCORNERUPL( Colours.WHITE , true, "WallCornerUpLeft", "_", "_"),  
  WALLCORNERDOWNR( Colours.WHITE , true, "WallCornerDownRight", "_", "_"), 
  WALLCORNERDOWNL( Colours.WHITE , true, "WallCornerDownLeft", "_", "_"), 
  WALLLEFTRIGHT( Colours.WHITE , true, "WallVertical", "_", "_"),
  DOORUPDOWN( Colours.WHITE, true, "DoorHorizontal", "_", "_"), 
  DOORLEFTRIGHT(Colours.WHITE, true, "DoorVertical", "_", "_"), 
  CORRIDOR( Colours.GREEN, false, "Corridor", "C", "C" ), 
  SERVICEROOM (Colours.YELLOW, false, "Service", "S", "S"), 
  CLASSROOM( Colours.ORANGE, false, "Class", "M", "M"),
  LAB( Colours.RED, false, "Lab", "B", "B"),
  AUDITORIUM( Colours.RED2, false, "Auditorium", "A", "H"), 
  STAFF( Colours.ORANGE2, false, "Staff", "P", "M"),
  HALL( Colours.LIGHTBLUE, false, "Hall", "H", "H"), 
  CANTEEN( Colours.LIGHTBLUE2, false, "Canteen", "N", "H"),
  GYM( Colours.PURPLE, false, "Gym", "G", "H"),
  OFFICE( Colours.GREY2, false, "Office", "K", "S"),
  ENTRANCE (Colours.GREY, false, "Entrance", "E", "E");
'''

# ABITAZIONI - mappe in Java2012
java_2012_abitazioni =''' EMPTY( Colours.WHITE , false, "Empty", "_", "_"), 
  WALLUPDOWN( Colours.WHITE , true, "WallHorizontal", "_", "_"), 
  WALLCORNERUPR( Colours.WHITE , true,"WallCornerUpRight", "_", "_"),
  WALLCORNERUPL( Colours.WHITE , true, "WallCornerUpLeft", "_", "_"),  
  WALLCORNERDOWNR( Colours.WHITE , true, "WallCornerDownRight", "_", "_"), 
  WALLCORNERDOWNL( Colours.WHITE , true, "WallCornerDownLeft", "_", "_"), 
  WALLLEFTRIGHT( Colours.WHITE , true, "WallVertical", "_", "_"),
  DOORUPDOWN( Colours.WHITE, true, "DoorHorizontal", "_", "_"), 
  DOORLEFTRIGHT(Colours.WHITE, true, "DoorVertical", "_", "_"), 
  CORRIDOR( Colours.GREEN, false, "Corridor", "C", "C" ), 
  SQCORRIDOR( Colours.GREEN2, false, "SquareCorridor", "C2", "C"),
  SMALLROOM( Colours.YELLOW, false, "SmallRoom", "S", "S"), 
  HALL( Colours.LIGHTBLUE, false, "Hall", "H", "H"), 
  BIGROOM( Colours.RED, false, "BigRoom", "B", "B"),
  MEDIUMROOM( Colours.ORANGE, false, "MediumRoom", "M", "M"),
  ENTRANCE (Colours.GREY, false, "Entrance", "E", "E");
'''

#C - H - E - S - M - B - K- Y - (R-F-N)

# codice colore per le label di java2012
Java2012_colorDict = {
'C':'#317344',
'S':'#5690A5',
'H':'#C4BF5C',
'B':'#1C3754',
'M':'#276686',
'E':'#B08F42',
'R':'#919191',
'F':'#919191', 
'N':'#919191',
'D':'#6118B2', 
'O':'#6D406D', 
'K':'#A43941', 
"|":"#FF0DFF", 
'X':'#6D406D', 
'P':'#955CA4',
'Y':'#6D406D',
'N12' : '#fe992c',
'N13' : '#f68722',
'N10' : '#f17047',
'N11' : '#fdbc6b',
'N16' : '#7d54a6',
'N17' : '#a0839a',
'N14' : '#d9a49a',
'N15' : '#af91c5',
'N18' : '#f3f099',
'N19' : '#d9af62',
'N8' : '#f16767',
'N9' : '#e41f21',
'N0' : '#a6cee3',
'N1' : '#60a1cb',
'N2' : '#2b80b1',
'N3' : '#7dba99',
'N4' : '#99d277',
'N5' : '#51af42',
'N6' : '#6b9e4a',
'N7' : '#db9b87'
} 
# mapping da label a R (room) o C (corridor) come da paper di IAS 
# openspace va mappato ad un altra cosa (va contestualizato in quanto e' un caso particolare di stanza di collegamento / funzionale
#  secondo me prevale funzionale)
# e anche Empty ma questo per uan questione di analisi e non semantica (Empty e' una stanza di tipo collegamento)
labels_RC_java2012 = {
'C': 'C',
'C2': 'C',
'S': 'R',
'H':'C',
'B':'R',
'M':'R',
'E':'C',
'R':'R',
'F':'R',
'N':'R',
'D':'R',
'O':'R', 
'K':'R',
"|":'R',
'X':'C',
'P':'R',
'Y':'R',
'N12' : 'R',
'N13' : 'R',
'N10' : 'R',
'N11' : 'R',
'N16' : 'R',
'N17' : 'R',
'N14' : 'R',
'N15' : 'R',
'N18' : 'R',
'N19' : 'R',
'N8' : 'R',
'N9' : 'R',
'N0' : 'R',
'N1' : 'R',
'N2' : 'R',
'N3' : 'R',
'N4' : 'R',
'N5' : 'R',
'N6' : 'R',
'N7' : 'R'
}  
################################################# FINE FORMATO SALVATAGGI JAVA-2012 (MapCreator) #################################################

################################################# INIZIO FORMATO SALVATAGGI DA JAVA2012 -> MATLAB-ADIACENZE (spectralGraph) #################################################
# le matrici di adiacenza hanno queste label sulla diagonale.
# lo stesso formato e' usato anche su gSpan
labels_java2012toMatlab_Dict = {
'C': 100,
'S': 2,
'H':105,
'B':4,
'M':3,
'E':1000,
'R':5,
'F':6,
'N':7,
'D':8,
'O':1, 
'K':0 ,
"|":10000,
'X':110,
'P':9,
'Y':10,
'N12' : 23,
'N13' : 24,
'N10' : 21,
'N11' : 22,
'N16' : 27,
'N17' : 28,
'N14' : 25,
'N15' : 26,
'N18' : 29,
'N19' : 30,
'N8' : 19,
'N9' : 20,
'N0' : 11,
'N1' : 12,
'N2' : 13,
'N3' : 14,
'N4' : 15,
'N5' : 16,
'N6' : 17,
'N7' : 18
} 
 
 # priorita per le connessioni.
labelsPriority_java2012toMatlab_Dict = {
'C': 1,
'S': 4,
'H': 1,
'B': 2,
'M': 3,
'E': 1,
'R': 3,
'F': 2,
'N': 1,
'D': 2,
'O': 3, 
'K': 3 ,
"|": 10000,
'X': 1,
'P': 3,
'Y': 3} 
################################################# INIZIO FORMATO SALVATAGGI DA JAVA2012 -> MATLAB-ADIACENZE (spectralGraph) #################################################


