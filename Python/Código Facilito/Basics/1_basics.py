# Dado de los valores ingresados por el usuario (base, altura) calcular y mostrar en pantalla el área de un triángulo.
"""
base = int(input("Ingrese cuanto mide la base de su triangulo: \n"))
altura = int(input("¿cuanto es la altura de su triangulo? \n"))
print("El área del triangulo es de ", (base*altura)//2, " centímetros cuadrados")
"""

# Convertir la cantidad de dólares ingresados por un usuario a pesos colombianos y mostrar el resultado en pantalla.
"""
base = int(input("Cantidad de dólares a convertir: "))
print("El equivalente a sus ", base, " U$D, sería de ", base*3896.4, " COP")
"""

# Convertir los grados centígrados ingresados por un usuario a grados Fahrenheit y mostrar el resultado en pantalla.
"""
grados_centigrados = int(input("Ingrese temperatura \n"))
print("Equivale a ", grados_centigrados*33.8, "F°")
"""

# Mostrar en pantalla la cantidad de segundos que tiene un lustro.
"""
lustros = int(input("¿Cuantos lustros desea convertir a segundos?\n"))
años = lustros*5
print("En un lustro hay ", años*365*24*3600, "segundos")
"""

# Calcular la cantidad de segundos que le toma a la luz viajar del sol a Marte y mostrar el resultado en pantalla.
"""
print(227940000000/299792458)
"""

# Calcular el número de vueltas que da una llanta en 1 km, dado que el diámetro de la llanta es de 50 cm, mostrar el resultado en pantalla.
"""
print(1/0.0005, " vueltas")
"""

# Calcular y mostrar en pantalla la longitud de la sombra de un edificio de 20 metros de altura cuando el ángulo que forman los rayos del sol con el suelo es de 22º.


# Mostrar en pantalla True o False si la edad ingresada por dos usuarios es la misma.
"""
first_user = int(input("Edad usuario 1: \n"))
second_user = int(input("Edad usuario 2: \n"))
print(first_user is second_user)
"""
# Mostrar en pantalla la cantidad de meses transcurridos desde la fecha de nacimiento de un usuario.


# Mostrar en pantalla el promedio de un alumno que ha cursado 5 materias (Español, Matemáticas, Economía, Programación, Ingles).
"""
español, matemáticas, economía, programación, ingles = int(input("español: ")), int(input("matemáticas: ")), int(input("economía: ")), int(input("programación: ")), int(input("ingles: "))
print((español + matemáticas + economía + programación + ingles)//5)
"""
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#Dado un diccionario, el cual almacena las calificaciones de un alumno, siendo las llaves los nombres de las materia y los valores las calificación, mostrar en pantalla el promedio del alumno. Hecho.
"""
calificaciones = {'calculo':10, 'dibujo':5, 'matematica':4, 'lengua':7, 'programacion':9}
lista = calificaciones.values()
print(sum(lista)/len(lista))
"""

# A partir del diccionario del ejercicio anterior, mostrar en pantalla la materia con mejor promedio.
"""
for indice in (calificaciones):
	print(calificaciones)
clasificaciones = {'hola': 120, 'hola2': 23, 'hola3': 321, 'hola4': 2, 'hola5': 100}
materia = []
puntos = []

for key, item in clasificaciones.items():
    materia.append(key)
    puntos.append(item)

maxPuntos = max(puntos)
posMaxPuntos = puntos.index(maxPuntos)

print("Mejor clasificacion " + str(maxPuntos) + " en " + materia[posMaxPuntos])
"""

# Crear una lista la cual almacene 10 números positivos ingresados por el usuario, mostrar en pantalla: la suma de todos los números, el promedio, el número mayor y el número menor. Hecho.
"""
lista = []

while (len(lista) < 10):
	numeros_usuario = int(input("Ingrese un número: "))
	if (numeros_usuario <= 0):
		numeros_usuario = int(input("Ingrese un número válido: "))
	else:
		lista.append(numeros_usuario)
	
else:
	print("La suma de todos los números es: ", sum(lista), "\n")
	print("El promedio de los números es: ", sum(lista)/len(lista), "\n")
	print("El número maximo es: ", max(lista), "\n")
	print("El número mínimo es: ", min(lista), "\n")
"""

# Dado una lista de frases ingresadas por el usuario, mostrar en pantalla todas aquellas que sean palíndromo. Hecho.
"""
cantidad = int(input("Cuantas palabras quiere ingresar?\n"))

for i in range(cantidad):
	palabra = str(input("Ingrese su palabra: "))
	if (palabra == palabra[::-1]):
		print(palabra, "es un palindromo\n")
"""

# Mostrar en pantalla la palabra que más se repita junto con la cantidad de veces que lo hace del capituló número uno de Frankenstein
capitulo_1 = """I am by birth a Genevese, and my family is one of the most distinguished
of that republic.  My ancestors had been for many years counsellors
and syndics, and my father had filled several public situations
with honour and reputation.  He was respected by all who knew him
for his integrity and indefatigable attention to public business.
He passed his younger days perpetually occupied by the affairs of
his country; a variety of circumstances had prevented his marrying
early, nor was it until the decline of life that he became a husband
and the father of a family.

As the circumstances of his marriage illustrate his character, I
cannot refrain from relating them.  One of his most intimate
friends was a merchant who, from a flourishing state, fell,
through numerous mischances, into poverty.  This man, whose name
was Beaufort, was of a proud and unbending disposition and could not
bear to live in poverty and oblivion in the same country where he
had formerly been distinguished for his rank and magnificence.
Having paid his debts, therefore, in the most honourable manner,
he retreated with his daughter to the town of Lucerne, where he lived
unknown and in wretchedness.  My father loved Beaufort with the
truest friendship and was deeply grieved by his retreat in these
unfortunate circumstances.  He bitterly deplored the false pride
which led his friend to a conduct so little worthy of the affection
that united them.  He lost no time in endeavouring to seek him out,
with the hope of persuading him to begin the world again through
his credit and assistance. Beaufort had taken effectual measures to
conceal himself, and it was ten months before my father discovered
his abode.  Overjoyed at this discovery, he hastened to the house,
which was situated in a mean street near the Reuss.  But when he entered,
misery and despair alone welcomed him.  Beaufort had saved but a
very small sum of money from the wreck of his fortunes, but it
was sufficient to provide him with sustenance for some months,
and in the meantime he hoped to procure some respectable employment
in a merchant's house.  The interval was, consequently, spent in
inaction; his grief only became more deep and rankling when he had
leisure for reflection, and at length it took so fast hold of his
mind that at the end of three months he lay on a bed of sickness,
incapable of any exertion.

His daughter attended him with the greatest tenderness, but she saw
with despair that their little fund was rapidly decreasing and that
there was no other prospect of support.  But Caroline Beaufort
possessed a mind of an uncommon mould, and her courage rose to
support her in her adversity.  She procured plain work; she plaited
straw and by various means contrived to earn a pittance scarcely
sufficient to support life.

Several months passed in this manner.  Her father grew worse;
her time was more entirely occupied in attending him; her means of
subsistence decreased; and in the tenth month her father died in
her arms, leaving her an orphan and a beggar.  This last blow
overcame her, and she knelt by Beaufort's coffin weeping bitterly,
when my father entered the chamber.  He came like a protecting spirit
to the poor girl, who committed herself to his care; and after the
interment of his friend he conducted her to Geneva and placed her
under the protection of a relation.  Two years after this event
Caroline became his wife.

There was a considerable difference between the ages of my parents,
but this circumstance seemed to unite them only closer in
bonds of devoted affection.  There was a sense of justice
in my father's upright mind which rendered it necessary that
he should approve highly to love strongly.  Perhaps during former
years he had suffered from the late-discovered unworthiness of one
beloved and so was disposed to set a greater value on tried worth.
There was a show of gratitude and worship in his attachment to my mother,
differing wholly from the doting fondness of age, for it was inspired
by reverence for her virtues and a desire to be the means of,
in some degree, recompensing her for the sorrows she had endured,
but which gave inexpressible grace to his behaviour to her.
Everything was made to yield to her wishes and her convenience.
He strove to shelter her, as a fair exotic is sheltered by the gardener,
from every rougher wind and to surround her with all that could tend to
excite pleasurable emotion in her soft and benevolent mind.  Her health,
and even the tranquillity of her hitherto constant spirit, had been shaken
by what she had gone through.  During the two years that had elapsed
previous to their marriage my father had gradually relinquished all
his public functions; and immediately after their union they sought
the pleasant climate of Italy, and the change of scene and interest
attendant on a tour through that land of wonders, as a restorative
for her weakened frame.

From Italy they visited Germany and France.  I, their eldest child,
was born at Naples, and as an infant accompanied them in their rambles.
I remained for several years their only child.  Much as they were attached
to each other, they seemed to draw inexhaustible stores of affection from
a very mine of love to bestow them upon me.  My mother's tender caresses
and my father's smile of benevolent pleasure while regarding me are my
first recollections.  I was their plaything and their idol, and something
better--their child, the innocent and helpless creature bestowed on them
by heaven, whom to bring up to good, and whose future lot it was in
their hands to direct to happiness or misery, according as they
fulfilled their duties towards me.  With this deep consciousness of
what they owed towards the being to which they had given life,
added to the active spirit of tenderness that animated both, it may
be imagined that while during every hour of my infant life I
received a lesson of patience, of charity, and of self-control,
I was so guided by a silken cord that all seemed but one train of
enjoyment to me. For a long time I was their only care.  My mother
had much desired to have a daughter, but I continued their single
offspring.  When I was about five years old, while making an
excursion beyond the frontiers of Italy, they passed a week on the
shores of the Lake of Como.  Their benevolent disposition often
made them enter the cottages of the poor.  This, to my mother, was
more than a duty; it was a necessity, a passion--remembering what
she had suffered, and how she had been relieved--for her to act in
her turn the guardian angel to the afflicted.  During one of their
walks a poor cot in the foldings of a vale attracted their notice
as being singularly disconsolate, while the number of half-clothed
children gathered about it spoke of penury in its worst shape.
One day, when my father had gone by himself to Milan, my mother,
accompanied by me, visited this abode.  She found a peasant and his
wife, hard working, bent down by care and labour, distributing a
scanty meal to five hungry babes.  Among these there was one which
attracted my mother far above all the rest.  She appeared of a
different stock.  The four others were dark-eyed, hardy little
vagrants; this child was thin and very fair.  Her hair was the
brightest living gold, and despite the poverty of her clothing,
seemed to set a crown of distinction on her head.  Her brow was
clear and ample, her blue eyes cloudless, and her lips and the
moulding of her face so expressive of sensibility and sweetness
that none could behold her without looking on her as of a distinct
species, a being heaven-sent, and bearing a celestial stamp in all
her features. The peasant woman, perceiving that my mother fixed
eyes of wonder and admiration on this lovely girl, eagerly
communicated her history.  She was not her child, but the daughter
of a Milanese nobleman.  Her mother was a German and had died on
giving her birth.  The infant had been placed with these good
people to nurse:  they were better off then.  They had not been
long married, and their eldest child was but just born.  The father
of their charge was one of those Italians nursed in the memory of the
antique glory of Italy--one among the schiavi ognor frementi,
who exerted himself to obtain the liberty of his country.  He became
the victim of its weakness.  Whether he had died or still lingered
in the dungeons of Austria was not known.  His property was confiscated;
his child became an orphan and a beggar.  She continued with her foster
parents and bloomed in their rude abode, fairer than a garden rose among
dark-leaved brambles.  When my father returned from Milan, he found
playing with me in the hall of our villa a child fairer than pictured cherub
--a creature who seemed to shed radiance from her looks and whose form and
motions were lighter than the chamois of the hills.  The apparition
was soon explained.  With his permission my mother prevailed on her
rustic guardians to yield their charge to her.  They were fond of
the sweet orphan.  Her presence had seemed a blessing to them, but
it would be unfair to her to keep her in poverty and want when Providence
afforded her such powerful protection.  They consulted their village priest,
and the result was that Elizabeth Lavenza became the inmate of my parents'
house--my more than sister--the beautiful and adored companion of all
my occupations and my pleasures.

Everyone loved Elizabeth.  The passionate and almost reverential
attachment with which all regarded her became, while I shared it,
my pride and my delight.  On the evening previous to her being
brought to my home, my mother had said playfully, "I have a pretty
present for my Victor--tomorrow he shall have it."  And when,
on the morrow, she presented Elizabeth to me as her promised gift,
I, with childish seriousness, interpreted her words literally and
looked upon Elizabeth as mine--mine to protect, love, and cherish.
All praises bestowed on her I received as made to a possession of
my own.  We called each other familiarly by the name of cousin.
No word, no expression could body forth the kind of relation
in which she stood to me--my more than sister, since till death
she was to be mine only."""

# Remplazar cada letra de una frase dada por el usuario por la posición que le corresponde en el abecedario y mostrar el nuevo string en pantalla. (Los espacios no se remplazan) . Ejemplo: frase : 'Hola' salida : 815121 H(8) o(15) l(12) a(1)
"""
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(abecedario[15])
frase = str(input("Ingrese una frase: "))
for index in range(frase):
	frase[index]
"""

# Mostrar en pantalla la cantidad de vocales que existe en una frase dada por el usuario. Hecho.
"""
frase = str(input("Ingrese una frase: "))
cont = 0
frase = frase.lower()
for i in range(len(frase)):
	if (frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u"):
		cont += 1
print("El usuario ingresó", cont, "vocal/es")
"""

# Mostrar en pantalla la frecuencia de aparición de vocales en una frase dada por el usuario. Hecho
"""
a, e, i, o, u, frase = 0, 0, 0, 0, 0,str(input("Ingrese una frase: "))
frase = frase.lower()

for index in range(len(frase)):

	if (frase[index] == "a"):
		a += 1
	elif (frase[index] == "e"):
		e += 1
	elif (frase[index] == "i"):
		i += 1
	elif (frase[index] == "o"):
		o += 1	
	elif (frase[index] == "u"):
		u += 1
		
if (a == 0 and e == 0 and i == 0 and o == 0 and u == 0):
	print("No se ingresaron vocales")
else:
	print("El usuario ingresó\n", a," letras a\n", e," letras e\n", i," letras i\n", o," letras o\n", u," letras u\n")
"""


# Eliminar todas las vocales de una frase dado por el usuario y mostrar el nuevo string en pantalla.
"""
frase = str(input("Ingrese una frase: "))
a = len(frase)
for i in len(frase):
	if (frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u"):
		continue
	else:
		string += frase[i] 

print(string)	
"""


# Listar todos los números pares del 0 al 100. Hecho.
"""
for i in range(2,100,2):
	print(i)
"""
