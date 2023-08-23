#!/usr/bin/env python3

def return_evens(sequence):
        return [num for num in sequence if num % 2 == 0]


def make_exclamation(sentence_list):
        return [sentence + "!" for sentence in sentence_list]
