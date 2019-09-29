# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import glob
import os
import string
import unicodedata
import json

datafiles = "./data/names/*.txt"  # les fichiers pour construire vos modèles
test_filename = './data/test-names-t2.txt'  # le fichier contenant les données de test pour évaluer vos modèles

names_by_origin = {}  # un dictionnaire qui contient une liste de noms pour chaque langue d'origine
all_origins = []  # la liste des 18 langues d'origines de noms

BOS = "~"  # character used to pad the beginning of a name
EOS = "!"  # character used to pad the end of a name


def find_files(path):
    """Retourne le nom des fichiers contenus dans un répertoire.
       glob fait le matching du nom de fichier avec un pattern - par ex. *.txt"""
    return glob.glob(path)

find_files(C:\Users\rimdh\OneDrive - Université Laval\IFT-7022\TP1\tp1_2019\data\names)

def get_origin_from_filename(filename):
    """Passe-passe qui retourne la langue d'origine d'un nom de fichier.
       Par ex. cette fonction retourne Arabic pour "./data/names/Arabic.txt". """
    return os.path.splitext(os.path.basename(filename))[0]


def unicode_to_ascii(s):
    """Convertion des caractères spéciaux en ascii. Par exemple, Hélène devient Helene.
       Tiré d'un exemple de Pytorch. """
    all_letters = string.ascii_letters + " .,;'"
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in all_letters
    )


def read_names(filename):
    """Retourne une liste de tous les noms contenus dans un fichier."""
    with open(filename, encoding='utf-8') as f:
        names = f.read().strip().split('\n')
    return [unicode_to_ascii(name) for name in names]


def load_names():
    """Lecture des noms et langues d'origine d'un fichier. Par la suite,
       sauvegarde des noms pour chaque origine dans le dictionnaire names_by_origin."""
    for filename in find_files(datafiles):
        origin = get_origin_from_filename(filename)
        all_origins.append(origin)
        names = read_names(filename)
        names_by_origin[origin] = names


def train_models():
    load_names()
    # Vous ajoutez à partir d'ici tout le code dont vous avez besoin
    # pour construire vos modèles N-grammes pour chacune des langues d'origines.
    #
    # Vous pouvez ajouter au fichier toutes les fonctions que vous jugerez nécessaire.
    # Merci de ne pas modifier les fonctions présentes dans ce fichier.
    #
    # À compléter - Fonction pour la construction des modèles unigrammes, bigrammes et trigrammes.
    #
    # Votre code à partir d'ici...


def most_probable_origin(name, n=3):
    # Retourne la langue d'origine la plus probable du nom.
    # n désigne la longueur des N-grammes. Par ex n=3 --> trigramme
    # À compléter...
    return "French"  # À modifier


def logprob(name, origin, n=3):
    # Retourne la valeur du logprob d'un nom étant donné une origine
    # Utilisez une fonction logarithme en base 2.
    # À compléter...
    return -35.6  # À modifier


def perplexity(name, origin, n=3):
    # Retourne la valeur de perplexité d'un nom étant donné une origine
    # À compléter...
    return 7.8  # À modifier


def load_test_names(filename):
    """Retourne un dictionnaire contenant les données à utiliser pour évaluer vos modèles.
       Le dictionnaire contient une liste de noms (valeurs) et leur origine (clé)."""
    with open(filename, 'r') as fp:
        test_data = json.load(fp)
    return test_data


def evaluate_models(filename, n=3):
    """Fonction utilitaire pour évaluer vos modèles. Aucune contrainte particulière.
       Je n'utiliserai pas cette fonction pour l'évaluation de votre travail. """
    test_data = load_test_names(filename)
    # À compléter - Fonction pour l'évaluation des modèles N-grammes.
    # ...


if __name__ == '__main__':
    # Vous pouvez modifier cette section comme bon vous semble
    load_names()
    print("Les {} langues d'origine sont:".format(len(all_origins)))
    print(all_origins)
    print("Les noms chinois sont:")
    print(names_by_origin["Chinese"])

    train_models()
    some_name = "Lamontagne"
    some_origin = most_probable_origin(some_name)
    logprob = logprob(some_name, some_origin)
    perplexity = perplexity(some_name, some_origin)
    print("\nLangue d'origine de {}: ".format(some_name), some_origin)
    print("logprob({}, {}):".format(some_name, some_origin), logprob)
    print("perplexity({}, {}):".format(some_name, some_origin), perplexity)

    test_names = load_test_names(test_filename)
    print("\nLes données pour tester vos modèles sont:")
    for org, name_list in test_names.items():
        print("\t", org, name_list)
    evaluate_models(test_filename, 3)
