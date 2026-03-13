from streamlit import *
set_page_config(page_title="Complexe Scolaire Cardinal Malula", layout="wide")

def main():
    title("Complexe Scolaire Cardinal Malula")
    menu = ["Découvrir le cardinal", "1. Biographie", "2. Pensée", "3. Perspective", "4. Principe", "5. Ecole", "6. Remerciement", "8. Image", "9. Citation"]
    choice = sidebar.selectbox("Menu", menu)

    if choice == "1. Biographie":
        show_biographie()
    elif choice == "2. Pensée":
        show_pensee()
    elif choice == "3. Perspective":
        show_perspective()
    elif choice == "4. Principe":
        show_principe()
    elif choice == "5. Ecole":
        show_ecole()
    elif choice == "6. Remerciement":
        show_remerciement()
    elif choice == "8. Image":
        show_image()
    elif choice == "9. Citation":
        show_citation()


def show_biographie():
    markdown("# Biographie")
    write ("""  Né à Léopoldville le 17 décembre 1917, Joseph-Albert Malula est l'un des cardinaux les plus importants de l'histoire moderne de l'Église catholique en Afrique noire. Il est considéré comme l’un des fondateurs des Églises d’Afrique et une figure de la patristique africaine, l’« émule des saints Athanase, des Cyprien et des Augustin », «le père du rite zaïrois ou le pionnier par excellence de l’africanisation de l’Église sur le continent noir ».[réf. nécessaire] Cette considération dont fait l’objet Joseph Malula est partagée par exemple par Zoa du Cameroun qui le qualifie comme « l’un des plus grands de ceux que ce siècle aura produit sur notre continent africain »[réf. nécessaire], ou par Laurent Monsengwo du Congo qui estime qu’il est « un géant de l’histoire du Zaïre et de l’Afrique »[réf. nécessaire] . 
                
                Il est reconnu comme un personnage passionné pour la profondeur subversive de la Parole de Jésus, solide dans la foi, et un humaniste doté d'une grande culture littéraire[réf. nécessaire]. L'un des projets mobilisateurs de son ministère fut de contribuer à la restauration du dialogue entre la dimension universelle et locale de l'Église catholique 
                                    \n\n""")

    markdown("## 1. <u>jeunesse</u>", unsafe_allow_html=True)
    write ("""\n Joseph Albert Malula voit le jour le 17 décembre 1917 dans une famille catholique. Son père, Remacle Ngalula de Bena Kabindi, originaire de la province de Kasaï dans le centre du Congo, a reçu une formation de menuisier à la Colonie scolaire de Boma, dans l’ouest du Congo, école tenue alors par les Frères des écoles chrétiennes. Sa mère, Jeanne Bolumbu, vient du nord du pays (Équateur). Accueillie au pensionnat des Sœurs de la Charité de Moanda, elle apprend à lire, à écrire et à coudre. C’est dans la province du Bas-Congo, durant leurs années de formation, que Remacle et Joanne se rencontrent et se marient à la mission catholique de Kangu au Mayombe avant de s'installer à Léopoldville
En 1934, à la suite de l'érection du nouveau vicariat apostolique du Mayombe et de sa séparation du vicariat de Léopoldville, Malula est transféré au séminaire de Bolongo dans le nord du Congo[1].

En 1937 , il entame des études post-secondaires au grand séminaire du Christ-Roi de Kabwe, au centre du pays. Il y étudie trois ans la philosophie et cinq la théologie.

C’est durant ces années[Lesquelles ?] qu’il a commencé à se poser des questions aussi fondamentales que celle du rapport entre l’Église et la vie d’un peuple, celle du rôle du prêtre dans la vie d’un peuple ou encore celle sur le fait colonial[réf. nécessaire].

Durant sa formation, il développa rapidement un goût très prononcé pour la lecture se plongeant dans les écrits des pères de l’Église, particulièrement d’Augustin, de Cyprien. Après Pascal, il découvre les grands philosophes modernes[Lesquels ?]. Mais la rencontre décisive sera l’œuvre de Saint Thomas d'Aquin dont il découvre la rigueur et l’esprit de méthode. Il s’appliquera plus tard à la même rigueur ; mais il saura réagir au côté systématique et doctrinal du thomisme[réf. nécessaire].

En 1944, Joseph achève ses études de théologie. Après une année de stage au petit séminaire de Bokoro, il est ordonné prêtre le 9 juin 1946 au stade Reine-Astrid de Léopoldville en compagnie de son condisciple et ami, Eugène Moke.
        \n\n """)

    markdown ("## 2. <u>Resumer de son Parcour</u>", unsafe_allow_html=True)
    write ("""\n joseph-Albert Malula est né le 17 décembre 1917 à Léopoldville (Aujourd'hui kinshasa). après sa formation au seminaire, il est ordonné prêtre le 9 juin 1946. il consacre sa vie au service de l'église et de l'éducation des fidèles.

En 1959, il est nommé évêque auxiliaire de Léopoldville et reçoit la consécration épiscopale le 20 septembre 1959. Quelques années plus tard, en 1964, il dévient archêveque de kinshasa, ce qui fait de lui l'un des principaux responsables de l'église catholiqueau congo.
 
Le 28 avril 1969, le pape paul VI le crée cardinal, faisant de lui le premier cardinal congolais. Á travers cette personnalité, il participe aux grandes décisions de l'église africaine au plus haut niveau.

Le cardinal Malula a marqué l'histoire de l'église en Afrique par son engagement pour la dignité humaine, la justice et l'inculturation de l'évangile dans la culture africaine. il a encouragé les chrétiens africains à vivre leur foi tout en respectant leur identité culturelle.
il meurt le 14 juin 1989, laissant un héritage spirituel et intellectuel important pour l'église et pour la société congolaise.       
         """)



def show_pensee():

    markdown ("# Pensée")
    write ("""Les pensées du Cardinal Malula étaient profondément influencées par son expérience personnelle et son engagement dans la vie religieuse et politique de la République Démocratique du Congo. Il a été un fervent défenseur de l'identité congolaise et des valeurs africaines au sein de la communauté catholique. Malula a également été impliqué dans des pratiques d'inculturation, cherchant à rendre la foi catholique authentiquement africaine. Son travail a été largement documenté, avec plus de 750 documents publiés en plusieurs volumes. Malula a été un penseur et un acteur clé dans la lutte pour l'indépendance et l'autonomie congolaise, et ses discours et actions ont eu un impact significatif sur le pays et la communauté catholique.
        \n\n """)

    markdown ("## 1. <u>la dignité de l'homme africain et l'inculturation de la foi</u>", unsafe_allow_html=True)
    write ("""Malula pensais que l'église devait défendre la dignité eet la liberté du peuples africain. pour lui, chaque personne est créée à l'image de Dieu et mérite respect, justice et consideration.
il croyait que la foi chrétienne devait s'éxprimee à travers la culture africaine. il encourageait les chrétiens à vivre l'évangile sans renoncer à lleurs traditions positives. c'est dans cette esprit qu'il a soutenu le développement des communautés ecclésiales vivantes (CEV).
\n\n """)

    markdown("## 2. <u>l'imporrtance de l'éducation et l'église au services de la société</u> ", unsafe_allow_html=True)
    write ("""Le cardinal Malula pensait que l'éducation est essentielle pour le développement de l'homme et de la société. selon lui, l'école doit former non seulement l'intelligence, mais aussi la conscience morale et spirituelle.
Pour Malula, l'église ne devait pas rester silencieusement face aux injustices. Elle devait défendre la vérité, la justice et la paix, même lorsque cela demandait du courage face au pouvoir politique.         
   """)



def show_perspective():
    markdown ("# Perspective")
    write ("""La vision de Cardinal Malula s’inscrit dans un contexte de crise morale, économique et spirituelle.
Il a souligné :
« Les jeunes vivent dans une société où on dit tout est fait sans pudeur. »
« Mieux vaut être crucifié pour la vérité que de crucifier la vérité. »
« Une église jeune dans un pays jeune ne peut négliger le jeune. »

Il insiste sur le fait que l’avenir appartient aux jeunes, à condition qu’ils soient bien formés. Une jeunesse bien éduquée garantit l’avenir. À l’inverse, une jeunesse sacrifiée entraîne la répétition des erreurs des adultes.
> Problème majeur : l’éducation de qualité de la jeunesse, surtout à Kinshasa, ville jeune par excellence. """)

    markdown ("## 1. <u>Vision</u>", unsafe_allow_html=True)
    write ("""Le Cardinal Malula propose deux grandes lignes : les axes de formation et les principes pour l’éducation.
a) Axes de formation (3 axes)

1. Humaine : Épanouissement de l’homme pour qu’il puisse assumer ses responsabilités dans la société.
Développement de qualités essentielles : loi de l’effort, connaissance de soi, gestion du temps, docilité, sincérité, confiance.

2. Chrétienne et morale : S’identifier au Christ, vivre dans l’amour et la vertu pour devenir une personne bonne et juste.

3. Spirituelle : Un homme sans spiritualité est comme un navire sans boussole.
La vie spirituelle élève l’esprit et donne la priorité aux valeurs essentielles. Elle se manifeste par le sacrement et l’amour. """)

    markdown ("## 2. <u>Point de vue</u>", unsafe_allow_html=True)
    write ("""Cardinal Malula propose quatre perspectives pour la jeunesse et la société :

1. Jeunesse croyante : La foi est conviction et adhésion, preuve d’une réalité invisible.
Importance de réfléchir et d’approfondir sa foi.

2. Jeunesse dynamique : Courageuse, active et apostolique. Capable de résister aux courants dominants sans se laisser entraîner par la masse.

3. Leadership éthique : Leadership basé sur des valeurs.
« Politique sans éthique est une pantalonnade. »

4. Implication et éducation de l’humain authentique : Former des hommes authentiques, responsables et spirituellement et moralement solides. """)



def show_principe():
    markdown ("# Principe")
    markdown ("## 1. <u>Principes pour l'éducation\n</u>", unsafe_allow_html=True)
    write ("""1. Émergence : c’est le Refus de la médiocrité. La Volonté de progresser vers l’excellence et l’amour de la valeur.
Les jeunes doivent viser compétences, excellence, élégance et suivre l’éminence de Cardinal Malula.

2. Science : c’est l’Antidote contre la fatalité. L’Analyse rigoureuse, recul, discernement. 
La vraie science sert le progrès.

3. Conscience : « Science sans conscience n’est que ruine de l’âme. » C’est la Voix intérieure révélant la vérité sur soi-même et le sens du devoir et de la responsabilité.
Le vrai progrès se mesure par la pureté, la vérité et une conscience droite.

4. Transparence : Les modèles authentiques sont essentiels pour les jeunes. Une élite véritable doit rayonner la vérité et la pureté
\n\n  """)

    markdown("## <u>2. Africanisation de l’Église  et Engagement social \n</u>", unsafe_allow_html=True)
    write ("""Malula plaçait l’Église au service de la nation congolaise, prônant une insertion harmonieuse de la foi chrétienne dans le projet de société postcoloniale 
Dictionary of African Christian Biography
. Il défendait l'idée d’une Église africaine et autonome, capable de dialoguer avec Rome tout en valorisant les valeurs culturelles africaines. Sa célèbre formule «Hier les missionnaires étrangers ont christianisé l’Afrique, aujourd’hui les négro-africains vont africaniser le christianisme» illustre bien son principe de contextualisation de la liturgie et de la pastorale 

. Cette vision se traduisait notamment par la création du rite zaïrois, utilisant le lingala et des expressions culturelles locales dans la liturgie

Le cardinal Malula considérait que l’Église devait jouer un rôle éthique et critique face au pouvoir politique, notamment lors de la dictature de Mobutu. Il défendait la justice distributive, la dignité humaine et le respect des droits des pauvres, dénonçant les abus de pouvoir et les politiques oppressives 

. Ses sermons et homélies ne se limitaient pas à la spiritualité mais comportaient des commentaires sociaux et politiques, visant à encourager l’unité et la responsabilité civique

 """)




def show_ecole():
    markdown ("# Ecole")
    markdown("## 1. <u>Localisation et infrastructure</u>", unsafe_allow_html=True)
    write ("""Situé dans la commune de Limete, le complexe se trouve dans la concession de la maison des Sœurs de Sainte Thérèse de l’Enfant Jésus de Kinshasa. Il est composé de trois grandes directions :
Maternelle : encadre les enfants de 3 à 5 ans avec 13 salles de classe et des éducatrices qualifiées.
Primaire (Primaire 1 & 2) : chaque direction dispose de 24 classes, fonctionnant en vacations matinales (7h30-12h30) et après-midi (12h45-17h00) pour une gestion optimale des effectifs.
Humanités : couvre le secondaire de la 7e à la 6e humanités avec des sections scientifiques (math-physique et bio-chimie), littéraires et commerciales, visant à préparer les élèves au monde universitaire de manière approfondie  
\n\n """)

    markdown ("## 2. <u>Organisation et Ressources Humaines \n</u>", unsafe_allow_html=True)
    write ("""Le complexe regroupe plus de 200 agents et suit un organigramme structuré comprenant :
1.Le conseil d’administration
2.La coordination
3.Les directions éducatives (maternelle, primaire et humanités)
Cet environnement favorise un climat de travail serein et un rendement de qualité pour les élèves et le personnel 
\n\n """)

    markdown ("## 3. <u> Philosophie et Objectifs Éducatifs \n</u>", unsafe_allow_html=True)
    write("""Le Complexe Scolaire Cardinal Malula vise à :
-Fournir un bagage intellectuel solide pour affronter le monde universitaire et professionnel.
-Encourager le développement des talents à travers des activités ludiques, sportives et artistiques.
-Offrir un accompagnement et un encadrement de qualité pour les élèves prometteurs.
-Le Complexe est donc non seulement un lieu d’enseignement académique mais aussi un centre de formation intégrale des jeunes, en accord avec sa vision centrée sur l’excellence et l’épanouissement des élèves. 
\n\n """)

    markdown ("## 4. <u>information sur le complexe cardinale Malula \n</u>", unsafe_allow_html=True)
    write ("""Composition
Le complexe scolaire cardinal Malula est une grande institution estudiantine de la ville Province de Kinshasa. Situé à la commune de Limete, dans la concession de la maison des Sœurs de Sainte Thérèse de l’Enfant Jésus de Kinshasa.

Composé de 3 grandes directions, notamment la maternelle, les primaires 1 et 2, puis la direction des humanités.

• La direction de la maternelle encadre trois tranches d’âge, à savoir les 3 ans, les 4 ans et les 5 ans. Avec un total de 13 salles de classes, chaque salle de classe est dirigée par des éducatrices assidues et dévouées à leurs tâches.

• Les directions du Primaire (1 & 2), disposant d’une grande capacité d’accueil, le complexe scolaire cardinal Malula a opté pour une gestion de deux directions de primaire qui fonctionnent de manière autonome. Composée de 24 classes par direction, les études se donnent suivant les vacations avant et après-midi, soit de 7h30 à 12h30 et de 12h45 à 17h00’. 
\n\n """)

    markdown("## 5. <u>Origine \n</u>", unsafe_allow_html=True)
    write ("""Son Eminence le Cardinal Joseph Albert MALULA avait fondé, au nom de l’Eglise catholique de l’archidiocèse de Kinshasa, le Complexe Scolaire Cardinal Malula pour scolariser l’homme noir qui, depuis longtemps, était humilié et considéré comme incapable de s’assumer et de gérer son avenir. C’était aussi pour donner à la société congolaise un modèle, une élite intégralement formée tant sur le plan intellectuel, moral que spirituel. Oui, le Cardinal MALULA a donc visé la formation de l’homme et de tout l’homme dont la devise est « Le meilleur est ma destinée ».
IMPLANTATION
En 1966, Son Eminence le Cardinal Joseph Albert MALULA a fondé l’école maternelle dénommée « Notre Dame des Anges ». Celle-ci ouvrit ses portes pour la première fois sur l’avenue des Tropiques n°590, dans une maison d’habitation, dans la commune de Limete, avec deux classes de cinquante enfants de sexe féminin.

En 1968, le Cardinal ayant constaté que l’espace devenait de plus en plus exigu par rapport à la sollicitation des parents attirés par la qualité de l’enseignement dispensé, décida de transférer l’école dans l’enceinte de sa résidence d’Archevêque au quartier du 20 mai, à côté du stade Tata Raphaël, dans la commune de Kalamu.

Cette même année, l’école primaire mixte vu le jour et elle reçut aussi les premiers apprenants de « Notre dame des anges », toujours dans l’enceinte de l’Archevêché.

En 1968, le Cardinal ayant constaté que l’espace devenait de plus en plus exigu par rapport à la sollicitation des parents attirés par la qualité de l’enseignement dispensé, décida de transférer l’école dans l’enceinte de sa résidence d’Archevêque au quartier du 20 mai, à côté du stade Tata Raphaël, dans la commune de Kalamu. Cette même année, l’école primaire mixte vu le jour et elle reçut aussi les premiers apprenants de « Notre dame des anges », toujours dans l’enceinte de l’Archevêché.


En 1976, pour répondre à la demande accrue des parents, l’école secondaire vu le jour dans l’enceinte du couvent des Sœurs deSainte Thérèse de l’Enfant Jésus de Kinshasa sur la route du Motel FIKIN, dans la commune de Limete, et l’école primaire y fut transféré également. Le petit poisson est devenu grand. Il constitue aujourd’hui le grand Complexe Scolaire Cardinal Malula.
 """)


def show_remerciement ():
    markdown ("# <u>Remerciement</u>", unsafe_allow_html=True)
    write ("""Je tiens à vous exprimer ma plus sincère gratitude pour le temps que vous avez consacré à lire mon travail. Votre attention et votre soutien signifient beaucoup pour moi et encouragent mes efforts. Chaque lecture, chaque retour et chaque geste d’intérêt sont pour moi une source précieuse de motivation. Merci infiniment pour votre participation et votre confiance.

Et pour remercier l'école Complexe Scolaire Cardinal Malula ainsi que tous les enseignants qui m'ont poussé à donner le meilleur de moi-même, je tiens à exprimer ma profonde reconnaissance pour leur accompagnement, leur patience et leur engagement envers notre réussite. Grâce à leur dévouement et à leur savoir-faire, j'ai pu développer mes compétences et atteindre des objectifs que je n'aurais pas pu envisager seul.
  """)
    markdown ("### <u>Je vous remercie</u>", unsafe_allow_html=True)

def show_image ():
    markdown ("# <u>Image</u>", unsafe_allow_html=True)
    image ("cardinal.jpg", caption= "Cardinal Malula")
    image("Ecole.jpg", caption="Cardinal Malula")

def show_citation ():
    markdown ("# <u>Citation</u>", unsafe_allow_html=True)
    image ("citation1.jpg", caption= "Citation Malula", width= 400)
    image ("citation2.jpg", caption= "Citation Malula", width= 400)
    image ("citation 3.jpg", caption= "Citation Malula", width= 400)
    image ("citation4.jpg", caption= "Citation Malula", width= 400)
    image ("citation 5.jpg", caption= "Citation Malula", width= 400)






if __name__ == "__main__":
    main()



