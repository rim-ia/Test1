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