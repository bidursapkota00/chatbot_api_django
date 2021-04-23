import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import os.path
import numpy
import tflearn
import tensorflow
from tensorflow.python.framework import ops
import random
import json
import pickle

def ml(sentence):

    with open("./helloworld/intents.json") as file:
        data = json.load(file)
    try:
        with open('data.pickle', 'rb') as f:
            words, labels, training, output = pickle.load(f)
    except:
        words = []
        labels = ["greeting", "goodbye", "age", "name", "service", "location"]
        docs_x = []
        docs_y = []

        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                words.extend(wrds)
                docs_x.append(wrds)
                docs_y.append(intent["tag"]) 

            # if intent["tag"] not in labels:
            #     labels.append(intent["tag"])

        # print(labels)

        words = [stemmer.stem(w.lower()) for w in words if w != "?"]
        # print(words)
        words = sorted(list(set(words)))
        # print(words)
        labels = sorted(labels)
        # print(labels)

        training = []
        output = []
        # print(words)
        out_empty = [0 for _ in range(len(labels))]
        # print(out_empty)
        for x, doc in enumerate(docs_x):
            bag = []
            wrds = [stemmer.stem(w) for w in doc]
            # print(wrds)
            # for w in words:
            i = 0
            while(i < len(words)) :
                if words[i] in wrds:
                    bag.append(1)
                    i = i+1
                else:
                    bag.append(0)
                    i = i+1

            output_row = out_empty[:]
            output_row[labels.index(docs_y[x])] = 1
            # print(output_row)
            # print(bag)
            training.append(bag)
            output.append(output_row)

        training = numpy.array(training)
        output = numpy.array(output)

        with open('data.pickle', 'wb') as f:
            pickle.dump((words, labels, training, output), f)

    # print(len(training))


    # tensorflow.reset_default_graph()
    ops.reset_default_graph()
    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation='softmax')
    net = tflearn.regression(net)

    model = tflearn.DNN(net)
    
    if os.path.isfile('ai_model.tflearn.index'):
        model.load('ai_model.tflearn')
    else:
        model.fit(training, output, n_epoch=10000, batch_size=8, show_metric=True)
        model.save('ai_model.tflearn')

    def bag_of_words(s, words):
        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w==se:
                    bag[i] = 1
        
        return numpy.array(bag)

    
    if sentence == '' :
        return 'please write message before sending'
    else:
        results = model.predict([bag_of_words(sentence, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        if results[results_index] > 0.7:
            for tg in data['intents']:
                if tg['tag'] == tag:
                    responses = tg['responses']

            return(random.choice(responses))

        else:
            return('I didnt get that try again.')


