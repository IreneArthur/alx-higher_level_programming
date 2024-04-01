#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sente = None
    else:
        sent_length = len(sentence)
        sente = sentence[:1]
    return (sent_length, sente)
