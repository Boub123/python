#!/usr/bin/env python
# -*- coding: utf-8 -*-
###Fichier d'encodage avec arg à la suite(chaine de caractére ou fichier)
##importation des bibliothèques d'encodage.
import base64

#premier test pour encoder du texte ecrit en dur
#encoding code
chaine1 = "je suis partis"
encoded = base64.b64encode(b'chaine1')
print(encoded)

#et aprés je recupère le texte encodé pour le décoder en base64.
###decodng code
data1 = base64.b64decode(encoded)
print('Le texte encodé est décodé : ' + data1)


### écrire le texte dans le terminal j'ai éssayer de faire en sorte de pouvoir choisir un encodage, y'en a qui ne marche pas.
mon_texte = input("Donnez le texte que vous voulez encoder puis decoder : ")
encodage_1 = input("Avec quel encodage voulez-vous encoder votre texte ? : ")
decodage = input("Avec quel encodage voulez-vous décoder votre texte ? : ")
print("\nJ'encoder le texte suivant : " + mon_texte)
# A partir d'ici, on encode
mon_encodage = mon_texte.encode(encodage_1)
print("\nChoix de l'encodage de mon_texte à l'aide de " + encodage_1)
print("Voilà les valeurs des octets obtenus : ")
for octet in mon_encodage:
    print(octet, end='-')
# A partir d'ici, on tente de décoder
mon_decodage = mon_encodage.decode(decodage)
print("\n\n l'encodage choisi " + decodage)
print("Si le résultat est interprétable, cela donne ")
print(mon_decodage)
input("Pause. Appuyer sur ENTREE")