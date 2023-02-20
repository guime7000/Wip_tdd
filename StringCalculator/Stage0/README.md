Je dois fournir une fonction calculate qui prend une chaîne de caractère EXPRESSION en entrée et renvoie un entier.

EXPRESSION peut contenir 0, 1, 2 ou plus nombres entiers séparés par une virgule. 

La fonction calculate renvoie alors la somme des nombres contenus dans EXPRESSION.
Pour les étapes 1 et 2, les entrées invalides ne sont pas gérées.
Exemple: 

- calculate("") renvoie 0 (cas particulier de la chaîne vide)

- calculate("0") renvoie 0

- calculate("123") renvoie 123

- calculate("1,4") renvoie 5

- calculate("1,2,3") renvoie 6

- calculate("1,2,3,4,5") renvoie 15