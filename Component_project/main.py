from __future__ import annotations

import os
import re
import pandas as pd


from nltk.corpus import wordnet as wn
from vertexai.preview.language_models import ChatModel
from vertexai.preview.language_models import InputOutputTextPair
# nltk.data.path.append('C:/Users/Steph/AppData/Roaming/nltk_data')

def write_dataframe_to_csv(df, filename):
    df.to_csv(filename, index=False)
def science_tutoring(temperature: float = 0.2) -> None:
    chat_model = ChatModel.from_pretrained('chat-bison@001')

    # TODO developer - override these parameters as needed:
    parameters = {
        # Temperature controls the degree of randomness in token selection.
        'temperature': temperature,
        # Token limit determines the maximum amount of text output.
        'max_output_tokens': 256,
        # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        'top_p': 0.95,
        # A top_k of 1 means the selected token is the most probable among all tokens.
        'top_k': 40,
    }

    chat = chat_model.start_chat(
        context='My name is Miles. You are an astronomer, knowledgeable about the solar system.',
        examples=[
            InputOutputTextPair(
                input_text='How many moons does Mars have?',
                output_text='The planet Mars has two moons, Phobos and Deimos.',
            ),
        ],
    )

    response = chat.send_message(
        'How many planets are there in the solar system?', **parameters,
    )
    print(f'Response from Model: {response.text}')
    # [END aiplatform_sdk_chat]

    return response


def filter_for_artificial_nouns(synset):
    """Returns True if the synset is an artificial noun, False otherwise."""
    """Can make similar functions for https://wordnet.princeton.edu/documentation/lexnames5wn#:-:text=noun"""

    return synset.lexname() == 'noun.artifact'


def remove_anything_after_dot(word):
    """Removes anything after a "." in a word.

    Args:
      word: A string.

    Returns:
      A string with anything after a "." removed.
    """

    dot_index = word.find('.')
    if dot_index != -1:
        return word[:dot_index]
    else:
        return word


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Get all synsets in WordNet
    synsets = wn.all_synsets()  # Can also get nouns from nouns = wn.all_synsets('n')

    # Filter the synsets for artificial nouns
    artificial_noun_synsets = list(
        filter(filter_for_artificial_nouns, synsets),
    )
    # Print the number of artificial noun synsets
    print(len(artificial_noun_synsets))

    # Example usage:
    artificial_noun_names = [
        remove_anything_after_dot(
            synset.name(),
        ) for synset in artificial_noun_synsets
    ]
    artificial_noun_definition = [
        synset.definition()
        for synset in artificial_noun_synsets
    ]

    import csv

    with open('GFG.csv', 'w') as f:
        df = pd.DataFrame({'name': artificial_noun_names, 'definition': artificial_noun_definition}).dropna(how='all')
        write_dataframe_to_csv(df, f)
    #artificial_noun_synsets.to_csv("test.csv")
    #print(artificial_noun_names)
    #print(artificial_noun_definition)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
