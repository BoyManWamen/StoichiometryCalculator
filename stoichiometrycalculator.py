import re
import sys
# Format : 3O-5H+10He
atomicMasses = {
  "H" : 1,
  "He" : 4,
  "Li" : 6.941,
  "Be" : 9,
  "B" : 10.811,
  "C" : 12.0107,
  "N" : 14.0067,
  "O" : 16,
  "F" : 18.9984,
  "Ne" : 20.1797,
  "Na" : 22.9897,
  "Mg" : 24.305,
  "Al" : 26.9815,
  "Si" : 28.0855,
  "P" : 30.9738,
  "S" : 32.065,
  "Cl" : 35.453,
  "K" : 39.0983,
  "Ar" : 39.948,
  "Ca" : 40.078,
  "Sc" : 44.9559,
  "Ti" : 47.876,
  "V" : 50.9415,
  "Cr" : 51.9961,
  "Mn" : 54.938,
  "Fe" : 55.845,
  "Ni" : 58.6934,
  "Co" : 58.9332,
  "Cu" : 63.546,
  "Zn" : 65.39,
  "Ga" : 69.723,
  "Ge" : 72.64,
  "As" : 74.9216,
  "Se" : 78.96,
  "Br" : 79.904,
  "Kr" : 83.8,
  "Rb" : 85.4678,
  "Sr" : 87.62,
  "Y" : 88.9059,
  "Zr" : 91.224,
  "Nb" : 92.9064,
  "Mo" : 95.94,
  "Tc" : 98,
  "Ru" : 101.07,
  "Rh" : 102.9055,
  "Pd" : 106.42,
  "Ag" : 107.8682,
  "Cd" : 112.411,
  "In" : 114.818,
  "Sn" : 118.71,
  "Sb" : 121.76,
  "I" : 126.9045,
  "Te" : 127.6,
  "Xe" : 131.293,
  "Cs" : 132.9055,
  "Ba" : 137.327,
  "La" : 138.9055,
  "Ce" : 140.116,
  "Pr" : 140.9077,
  "Nd" : 144.24,
  "Pm" : 145,
  "Sm" : 150.36,
  "Eu" : 151.964,
  "Gd" : 157.25,
  "Tb" : 158.9253,
  "Dy" : 162.5,
  "Ho" : 164.9303,
  "Er" : 167.259,
  "Tm" : 168.9342,
  "Yb" : 173.04,
  "Lu" : 174.967,
  "Hf" : 178.49,
  "Ta" : 180.9479,
  "W" : 183.84,
  "Re" : 186.207,
  "Os" : 190.23,
  "Ir" : 192.217,
  "Pt" : 195.078,
  "Au" : 196.9665,
  "Hg" : 200.59,
  "Tl" : 204.3833,
  "Pb" : 207.2,
  "Bi" : 208.9804,
  "Po" : 209,
  "At" : 210,
  "Rn" : 222,
  "Fr" : 223,
  "Ra" : 226,
  "Ac" : 227,
  "Pa" : 231.0359,
  "Th" : 232.0381,
  "Np" : 237,
  "U" : 238.0289,
  "Am" : 243,
  "Pu" : 244,
  "Cm" : 247,
  "Bk" : 247,
  "Cf" : 251,
  "Es" : 252,
  "Fm" : 257,
  "Md" : 258,
  "No" : 259,
  "Rf" : 261,
  "Lr" : 262,
  "Db" : 262,
  "Bh" : 264,
  "Sg" : 266,
  "Mt" : 268,
  "Rg" : 272,
  "Hs" : 277        
}

def stoichiometrycalculator():
  chemicalEquation = input("Balanced Equation (Format: (Reactant)-(Product)+(Product) ): ")

  chemicalEquation = chemicalEquation.replace("-"," ")
  chemicalEquation = chemicalEquation.replace("+"," ")
  chemicalEquation = chemicalEquation.split(" ")

  moleculesMassInGrams = {}
  coefficients = {}

  for molecules in chemicalEquation:
    string = 0
    moleculesAndCoefficientsWithSubscripts = re.split('(\d)' and r"([A-Z][a-z]*[2-9]*)",molecules)
    for elements in moleculesAndCoefficientsWithSubscripts:
      if re.search(r"^[2-9]+[2-9]?$",elements):
          element = int(elements)
          coefficients[str(molecules)] = element
      elif re.search(r"^[A-Z][a-z]*$",elements):
          string += atomicMasses[str(elements)]
      elif re.search(r"^[A-Z][a-z]?[2-9]{1}$",elements):
          d = 0
          for i in elements:
              if i in "123456789":
                  d = int(i)
              else:
                  continue
          string += (atomicMasses[elements.replace(str(d),"")] * d)
      else:
        continue
    if len(coefficients) > 0:
      string *= int(coefficients[str(molecules)])
    moleculesMassInGrams[str(molecules)] = string

  counter = 0
  for molecules in range(len(chemicalEquation)):
    string = ("Mass of {} in Grams: {}").format(chemicalEquation[counter],moleculesMassInGrams[chemicalEquation[counter]])
    print(string)
    counter += 1

  exit = input("Press a to exit or r to continue: ")
  if exit == "a":
    sys.exit()
  elif exit == "r":
    stoichiometrycalculator()
  elif exit == "":
    stoichiometrycalculator()

stoichiometrycalculator()
