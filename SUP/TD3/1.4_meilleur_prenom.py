
# Created by Ewen BRUN
def score(word):
    '''returns the score of a word based on letters order '''
    s = 0
    letters = ['-','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in word:
        s += letters.index(letter)
    return s

def prenoms_solo():
    """retourne la liste des prenoms"""
    f = open('Sup1.txt','r')
    liste = list()
    prenoms_seuls = list()
    for ligne in f:
        liste.append(ligne.lower().strip('\n').split('\t'))
    for i in range(0,len(liste)-1):
        prenoms_seuls.append(liste[i][1])
    return prenoms_seuls

# Core Engine
prenoms = prenoms_solo()
lst = list()

f = open('Prenoms.txt','w')
for e in prenoms:
    f.write(e+' '+str(score(e))+'\n')
    lst.append([score(e),e])

lst.sort()
# Prints the 5 bests names
print('='*46)
for i in range(5):
    print(i+1,'Meilleur prenom :',lst[-i-1][1],'avec un score de',lst[-i-1][0])
print('='*46)
