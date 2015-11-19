# intestazione

# fine intestazione

class label(object) :

  def __init__(self, name, buildingtype, mytype, letter, size = None, function = None, description = None, color = None) :
    '''
    Inspired by http://www.wbdg.org/design/secondary.php
    Divido in 3 categorie: funzionali (F), corridoi (C), di servizio (S) + ENTRANCE (E)
    Le stanze di servizio si dividono in amministrativi (A, servizi S, igienici I) S:{A,S,I}
    Funzionali: dove vengono effettuate le core-activities della tipologia
    Corridoi: connettono stanze / no attività.
    Servizio: di supporto alla core activities (es: mense o amministrativi)
    Divido le stanze in 4 categorie di dimensione: S M B C
    S SMALL
    M MEDIUM
    B BIG
    U/C COLLECTIVE (es: openspace)
    N Not relevant
    La stanza "centrale" della tipologia è la FUNZIONALE MEDIA (es: classe o ufficio)
    QUesto mapping di base da poi il mapping specifico di tipologia.
    Fonte di base: http://www.wbdg.org/design/buildingtypes.php + https://en.wikipedia.org/wiki/Architects%27_data + libri specifici di tipologia.
    '''
    self.name = name
    self.buildingtype = buildingtype
    self.mytype = mytype
    self.letter = letter
    self.size = size
    self.function = function
    self.description = description
    if color :
      self.color = color
    else :
      # TODO: trovati un random color
      pass

  def toxml(self) :
    pass
