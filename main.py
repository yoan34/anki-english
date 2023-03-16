import requests
import json

from utils.deck import create_all_decks


# createDeck('testscript')
# createDeck('testscript::subpaquet')

create_all_decks()



presentation = """
Je veux que tu réponds "OK" à ce message et que tu attends le prochain car c'est juste pour te donner le contexte de ma vie.

Je vie à Castanet-Tolosan avec ma compagne Laetitia de 27 ans qui est éducatrice de jeune enfant, ma fille Inaya qui va faire
3 ans le 6 avril et notre nouveau bébé Eliot qui est née le 25 Janvier 2023.

Concernant moi, Yoan: J'aime cuisinier, faire du vélo le long du canal du midi, courir. J'étudie le Yoga et les pratique yoguique pour essayer de
m'améliorer dans ma vie personnel. j'ai 28 ans, cheveux rasé, barbe rasé, je suis jeune développeur informatique travaillant à Toulouse dans une entreprise qui
s'appelle OneStock. Je vie à Castanet-Tolosan avec ma compagne Laetitia, et nos enfants Inaya et Eliot.

Laetitia: Elle a 27 ans, elle travail dans une crèche en tant qu'éducatrice de jeune enfant.Elle a de long cheveux chatain, ne se maquille pas ce
qui la rend plus belle en faisant resortir l'éclat de son visage. Elle aime beaucoup lire, en ce moment sur le féminisme et
elle adore peindre des femmes, se promener en famille.

Inaya: Elle fera 3 ans en avril, c'est une fille gentil et dynamique qui adore raconter des histoires et jouer dehors dans les parcs et manger pleine de
fruits mais aussi des bonbons! Elle a de long cheveux chatain avec un jolie sourire. Elle va 4 jours par semaine chez une nounou qui s'apelle Emmanuelle.

Eliot: Jeune arrivé, bientot 2 mois, il est très calme et ne cri pas beaucoup, il a des cheveux noir et commence déjà à bien sourire.

Emmanuelle: C'est la nounou de Inaya qui vie à Castanet-Tolosan, elle garde également une fille Manon qui a 3 ans, et Eléanore, un bébé de 7mois. Inaya
adore passer du temps la-bas à s'amuser avec eux. Ils vont souvent au RAM, un endroit ou il découvre d'autre jeux/activités/copains pour s'amuser.

Les parents de Laetitia s'apelle Pierre et Véronique, ils vivent en Aveyron à Salmiech, un petit village. Ils ont une belle et grande maison avec un jardin
magnifique, un bassin avec des poissons. Nous passons 2 jours par mois pour les voir et profiter de la famille. Pierre est mécanicien, il passe une grande
partie de sa journée au travail et rentre tard le soir, c'est un très bon bricoleur au cheveux court. Véronique travail dans une phamarcie pour faire le ménage.

Laetitia à une soeur qui s'apelle Emelyn et habite en Aveyron à Baraqueville, elle a acheté une maison avec son copain Mathieu et vive avec leur chien, Teyga.
Emelyn travail dans un magasin et Mathieu et menuisier.

Les parents de Yoan s'appelle Céline et Michel, michel est le beau père de Yoan, car son vrai père s'appelle Gérard mais il est séparé depuis que Yoan à 3 ans de
sa mère Céline. Ils vivent à Pexiora un petit village. Ils ont une jolie maison avec un super terrain qu'ils ont acheté l'année dernière de 700m carré.
Céline adore cuisinier et fait une formation de naturopathie, elle a des douleurs chaque jour au dos et fume des cigarretes. Michel travail à l'usine,
cheveux court, il fait beaucoup de salle de musculation, adore écouter la musique rock, c'est un bricoleur.Il passe beaucoup de temps sur Youtube, il est
très rigolo.
Yoan à une soeur Jessica qui vie seul dans un appartement près de Carcassonne. Elle à des addiction à combattre, l'alcool et elle fume beaucoup de majiuana.
J'espère qu'elle s'en sortira bientot!

Gérard est un homme qui vie dans un camion depuis 20 ans, il adore la nature et fume de la marijuana. Il passe beaucoup de temps à bricoler sur son camion et
réparer des choses informatiques. Il recherche dieux à travers ses lectures, ses expériences acquises. C'étais un ancien fétard!

Contexte actuel de notre vie: Moi (Yoan) et Laetitia cherchions un appartement à Castanet-Tolosan à acheter pour s'installer depuis que Eliot et arrivé.
Je travail depuis 3 mois à OneStock, une société de retail informatique et j'essaye de gagner en confiance et responsabilité, quant à Laetitia, elle a 
décidé de s'occuper de Eliot au mois pour toute l'année 2024.
J'ai fini ma présentation, j'aimerai simplement que tu retienne bien, et analyse bien se contexte pour que tu m'aide à faire certaine exercice, es-tu prêt
à m'aider? Répond moi en français à part quand je te demande de traduire en anglais. Je veux simplement que tu me réponde par oui pour ce message. Après 
tu pourras être plus élaboré.
"""

print(len(presentation.split()))