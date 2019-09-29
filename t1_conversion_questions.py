# -*- coding: utf-8 -*-
import re

questions_fn = "./data/questions-t1.txt"
results_filename = "./t1_results.txt"

# Mettre dans cette partie les expressions régulières
# que vous utilisez pour analyser les questions
# et en faire la conversion en affirmations
#
# Vos regex...
#

def run_task1(filename):
    questions = load_questions(filename)
    results = convert_all_questions(questions)
    save_results(results)


def convert_all_questions(questions):
    results = []
    for question in questions:
        sentence = convert(question)
        results.append((question, sentence))
    return results


def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        raw_questions = f.readlines()
    questions = [x.strip() for x in raw_questions]
    return questions


def convert(question):
    # Insérer ici votre code pour le traitement des questions et leur conversion.
    # Vous pouvez ajouter autant de fonctions que vous souhaitez.
    # Voir fichier data/results-reference-t1.txt pour des exemples de conversion.
    #
    # IMPORTANT : Ne pas modifier les autres fonctions existantes de ce fichier
    #             afin de faciliter mon travail de correction.
    #             En cas de doute, me consulter.
    # Votre code...
    return "la terre est ronde."  # À modifier - retourner l'affirmation générée par cette fonction


def save_results(results):
    with open(results_filename, 'w') as output_file:
        for question, sentence in results:
            output_file.write("Q: " + question + "\n")
            output_file.write("A: " + sentence + "\n")
            output_file.write("\n")


if __name__ == '__main__':
    # Vous pouvez modifier cette section
    print("Conversion des questions du fichier {} ".format(questions_fn))
    run_task1(questions_fn)
    print("Conversion complétée")
