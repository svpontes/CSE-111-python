from english import get_determiner, get_noun, get_preposition_phrase, get_verb
import pytest



def test_get_determiner():
    single_determiners = ["a", "one", "the"]

    for _ in range(4):

        cap_word = get_determiner(1)

        assert cap_word in single_determiners


    plural_determiners = ["two", "some", "many", "the"]

    for _ in range(4):

        cap_word = get_determiner(2)

        assert cap_word in plural_determiners

pytest.main(["-v", "--tb=line", "-rN", __file__])
"""
#================================================

def test_get_preposition_phrases():
    preposition = []
    single_determiners =[]
    plural_determiners= []
    single_noun = []
    plural_noun = []

    for i in range(1,2):
        word_list = get_preposition_phrase(i)
        word_string = word_list.split()
        prep = word_string[0]
        deter= word_string[1]
        noun = word_string[2]

        assert len(word_string) == 3
        assert prep in preposition
        if i == 1:
            assert deter in plural_determiners
            assert noun in single_noun
        if i == 2:
            assert deter in plural_determiners
            assert noun in plural_determiners

def test_get_propositional_phrase():
    #test a frase preposicao com quantidade 1/ singular

    phrase = get_preposition_phrase(1)
    words = phrase.split()
    count_words = len(words)

    print(count_words)
    print(words)"""