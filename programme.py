#!/bin/env python3

import sys, exercice, re

def tri(l):
    """
    Cette fonction récursive tri la liste passée en argument.
    """
    if type(l[0])==int:
        l.sort()
    else:
        for i in l:
            tri(i)

def profondeur(l):
    """
    Cette fonction renvoie la profondeur de la liste passée en argument.
    """
    def _profondeur(l,p):
        nonlocal prof
        for i in l:
            if type(i)==int:
                if p>prof:
                    prof = p
            else:
                _profondeur(i,p+1)
    prof=float("-inf")
    _profondeur(l,1)
    return(prof)

def minmax(l):
    """
    Cette fonction récursive retourne le minmax de la liste passée en argument.
    """
    if type(l[0])==int:
        maxi.append(max(l))
    else:
        for i in l:
            minmax(i)

if __name__=="__main__":
    # programme principal
    if len(sys.argv)==1:
      while True:
          line = input("? ").rstrip("\n").strip()
          if line=="":
              break
          exercice.lline = re.split(r' +',line.rstrip("\n"))
          exercice.i = 0
          l = exercice.mklist()                      # récupération de la liste
          tri(l)
          print(f"{l=}")
    elif len(sys.argv)==2:
      f = open("listes.txt", "r")
      for line in f:
          lline = re.split(r' +',line.rstrip("\n"))
          l = exercice.build(lline)                     
          print(f"{l=}")
          print(f"{profondeur(l)=}")
    else:
        exercice.i = 1
        l = exercice.construire()                   # récupération de la liste
    maxi = []
    minmax(l)
    print(min(maxi))
