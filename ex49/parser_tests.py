from nose.tools import *
from ex48.lexicon import Lexicon
from ex48 import parser

lexicon = Lexicon()

def test_sentence_obj():
    s = parser.Sentence(('noun', 'bear'), ('verb', 'eat'), ('noun', 'door'))
    assert_equal(s.subject, 'bear')
    assert_equal(s.verb, 'eat')
    assert_equal(s.object, 'door')


def test_peek():
	word_list = lexicon.scan('bear')
	assert_equal(parser.peek(word_list), 'noun')
	assert_equal(parser.peek(None), None)
	
def test_match():
	word_list = lexicon.scan('bear')
	assert_equal(parser.match(word_list, 'noun'), ('noun', 'bear'))
	assert_equal(parser.match(word_list, 'stop'), None)
	assert_equal(parser.match(None, 'noun'), None)
	
def test_skip():
	word_list = lexicon.scan('bear go door')
	assert_equal(word_list, [('noun', 'bear'), ('verb', 'go'), ('noun', 'door')])
	parser.skip(word_list, 'noun')
	assert_equal(word_list, [('verb', 'go'), ('noun', 'door')])
	
def test_parse_verb():
	word_list = lexicon.scan('it go door')
	assert_equal(parser.parse_verb(word_list
	), ('verb', 'go'))
	word_list = lexicon.scan('bear goes door')
	assert_raises(parser.ParserError, parser.parse_verb, word_list)

def test_parse_object():
	word_list = lexicon.scan('the bear')
	assert_equal(parser.parse_object(word_list), ('noun', 'bear'))
	word_list = lexicon.scan('the east')
	assert_equal(parser.parse_object(word_list), ('direction', 'east'))
	word_list = lexicon.scan('it stop')
	assert_raises(parser.ParserError, parser.parse_object, word_list)

def test_parse_subject():
	word_list = lexicon.scan('the princess')
	assert_equal(parser.parse_subject(word_list), ('noun', 'princess'))
	word_list = lexicon.scan('the stop')
	assert_equal(parser.parse_subject(word_list), ('noun', 'player'))
	word_list = lexicon.scan('the')
	assert_raises(parser.ParserError, parser.parse_subject, word_list)

def test_parse_sentence():
	word_list = lexicon.scan('the princess go east')
	s = parser.parse_sentence(word_list)
	assert_equal(s.to_tuple(), ('princess', 'go', 'east'))
	word_list = lexicon.scan('in go door')
	s = parser.parse_sentence(word_list)
	assert_equal(s.to_tuple(), ('player', 'go', 'door'))
	word_list = lexicon.scan('north eat door')
	assert_raises(parser.ParserError, parser.parse_sentence, word_list)

