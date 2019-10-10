# -*- coding: utf-8 -*-
import sys
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
training_questions_fn = "./data/questions-t3.txt"
test_questions_fn = "./data/test-questions-t3.txt"


def run_question_classification(training_fn, test_fn):
    accuracy_train, accuracy_test = train_and_test_classifier(training_fn, test_fn)
    print("Accuracy on training set: {0:.4f}".format(accuracy_train))
    print("Accuracy on test set: {0:.4f}".format(accuracy_test))


def train_and_test_classifier(training_fn, test_fn):
    questions, labels = load_dataset(training_fn)
    print("Nb questions d'entraînement:", len(questions))
    test_questions, test_labels = load_dataset(test_fn)
    print("Nb questions de test:", len(test_questions))

    # Insérer ici votre code pour la classification des questions.
    # Votre code...
    vectorizer = CountVectorizer()

    X_train = vectorizer.fit_transform(questions)
    Y_train = labels
    X_test = vectorizer.transform(test_questions)

    # MNB CLASSIFICATION
    mnb = MultinomialNB()
    mnb.fit(X_train, Y_train)
    mnb_prediction = mnb.predict(X_test)

    scores = cross_val_score(mnb, X_train,Y_train, cv=5)  # K = 5 Validation croisée sur 5 folds

    accuracy_train = scores.mean() # A modifier
    accuracy_test = accuracy_score(test_labels, mnb_prediction )  # A modifier

    f = open('output.txt', 'w')
    old_stdout = sys.stdout
    sys.stdout = f

    print("Question;Prédit;Réel")
    for i in range(0,len(test_questions)):
        print(test_questions[i] +";" + mnb_prediction[i] +";"+ test_labels[i] )

    sys.stdout = old_stdout

    #avoir les labels de facon unique
    x = np.array(Y_train)
    liste_label = list(np.unique(x))

    print(classification_report(test_labels, mnb_prediction, target_names=liste_label))

    return accuracy_train, accuracy_test


def load_dataset(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        labels, questions = zip(*[tuple(s.split(' ', 1)) for s in lines])
    return questions, labels


if __name__ == '__main__':
    run_question_classification(training_questions_fn, test_questions_fn)

