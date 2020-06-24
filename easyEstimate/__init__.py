import datetime
from pathlib import Path
from string import ascii_lowercase
import pandas as pd
from joblib import load
version = "0.4.8"

if __name__ == '__main__':
    base = "./"
else:
    base = Path(__file__).parent
    base = str(base) + "/"

LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}

appart = load(base + "Appartement_Estimation_2019_Cat_Boost.joblib")


# maison = load(base + "Maison_Estimation_2019.joblib")

def version():
    return version

def alphabet_position(word):
    text = ""
    try:
        for character in word.lower():
            if character in LETTERS:
                text = text + LETTERS[character]
            else:
                text = text + character
        return float(text)
    except AttributeError:
        return word


def estimer(numero, type_voie, voie, code_postal, surface, nbr_piece, nature=2, surface_terrain=0):
    """
    La fonction estimer permet d'estimer le prix d'une maison ou d'un appartement à partir des élèments suivants:
    Le numero       : numero dans la voie de l'habitation
    Le type de voie : le type de la voie avec des abréviations bien difinies si erreur la liste des abréviations s'affiche
    La voie         : le nom de la voie sans la mention type
    Le code postal  : aucun control n'est effectué sur le code postal
    La surface      : la surface loi carrez de l'habitation en mètre carré
    Le nbr de pièces: le nombre de pièce de l'habitation
    La nature       : la nature de l'habitation 1 pour une maison, 2 pour un appartement, 2 est la valeur par défaut
    Surface terrain : Pour les maison la surface du terrain, par défaut à 0
    :param numero:
    :param type_voie:
    :param voie:
    :param code_postal:
    :param surface:
    :param nbr_piece:
    :param nature:
    :param surface_terrain:
    :return: the estimation of the price based on the parameters
    """
    repertoire = pd.read_csv(base + "repertoire_code_adr.csv")
    abrev = repertoire["Type de voie"].unique()
    if (type_voie.upper() in abrev):
        code_dep = int(code_postal) // 1000
        code_commune = repertoire[(repertoire["Code postal"] == code_postal)]["Code commune"].mean()
        if (repertoire[(repertoire["Type de voie"] == type_voie.upper()) & (repertoire["Voie"] == voie.upper()) & (
                repertoire["Code postal"] == code_postal)]["Code voie"].empty):
            code_voie = 0
            print(
                "[WARN]", datetime.datetime.now(),
                "La voie demandée n'a pas été trouvée, une voie par défaut a été choisie ce qui affectera l'estimation")
        else:
            code_voie = repertoire[
                (repertoire["Type de voie"] == type_voie.upper()) & (repertoire["Voie"] == voie.upper()) & (
                        repertoire["Code postal"] == int(code_postal))]["Code voie"].median()
        if (int(nature) == 2):
            habitation = pd.DataFrame(
                [[int(numero), alphabet_position(type_voie), code_voie, int(code_postal), code_dep,
                  code_commune, int(surface), 0, 2, int(surface), int(nbr_piece)]],
                columns=['No voie', 'Type de voie', 'Code voie', 'Code postal',
                         'Code departement', 'Code commune', 'Surface Carrez du 1er lot',
                         'Surface Carrez du 2eme lot', 'Code type local', 'Surface reelle bati',
                         'Nombre pieces principales'])
            response = appart.predict(habitation)[0] // 1
            x = habitation.to_string(header=False,
                                     index=False,
                                     index_names=False).split('\n')
            vals = [','.join(ele.split()) for ele in x]
            print("[INFO]", datetime.datetime.now(), "Estimation", response, "Habitation", vals)
            return response
        elif (nature == 1):
            habitation = pd.DataFrame([[numero, alphabet_position(type_voie), code_voie, code_postal, code_dep,
                                        code_commune, surface, surface, nbr_piece, surface_terrain]])
            # return maison.predict(habitation)[0]//1
            return -1
    else:
        print("[ERROR]", datetime.datetime.now(), "Le type de la voie n'a pas été reconnu")
        return -1


if __name__ == '__main__':
    print("La valeur de votre habitation est :", estimer(20, "rue", "alphonse pluchet", 92220, 55, 4, 2, 0), "Euros")
