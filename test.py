
import base64
from encodings import mbcs
###J'éssayer d'ouvrir un fichier txt pour ensuite lire et encoder le contenu....
####Ce ci est un bout de  code que j'ai trouver pour ensuite l'implementer
#Première solution : open > lire > decode et encode > écrire

f = open("texte.txt")
txt = f.read().decode(mbcs) # txt est une unicode décodée depuis un fichier en ANSI
fic = open("resultat.txt")
fic.write(encoded = base64.b64encode(b'txt'))  # écrire en base64 dans ce resultat
