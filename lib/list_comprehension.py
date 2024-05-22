#!/usr/bin/env python3

def return_evens(num_list):
    return[x for x in num_list if x % 2 == 0]

def make_exclamation(sentence_list):
    return[sentence + '!' for sentence in sentence_list]