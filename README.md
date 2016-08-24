# ex48
zed shaw's ex48

from nose.tools import *
from ex48.lexicon import Lexicon

lexicon = Lexicon()

def test_directions():
	assert_equal(lexicon.scan("north"), [('direction', 'north')])
	result = lexicon.scan("north south east")
	assert_equal(result, [('direction', 'north'),
						('direction', 'south'),
						('direction', 'east')])
