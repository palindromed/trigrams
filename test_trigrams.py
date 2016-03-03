# -*- coding: utf-8 -*-
import pytest

TEST_LIST = ['One', 'night--it', 'was', 'on', 'the', 'twentieth', 'of',
             'March', 'One', 'night--it']

TEST_OUTPUT = {('on', 'the'): ['twentieth'], ('night--it', 'was'): ['on'],
               ('of', 'March'): ['One'], ('One', 'night--it'): ['was'],
               ('twentieth', 'of'): ['March'], ('was', 'on'): ['the'],
               ('the', 'twentieth'): ['of'],
               ('March', 'One'): ['night--it']}

TEST_STRING = 'The - dog ! ran (away) [from] ?'

STRING_OUTPUT = 'The  dog  ran away from '


def test_list_words():
    from trigrams import list_words
    assert list_words(TEST_LIST) == TEST_OUTPUT


def test_remove_punctuation():
    from trigrams import remove_punctuation
    assert remove_punctuation(TEST_STRING) == STRING_OUTPUT
