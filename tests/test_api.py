import vcr
import pytest
import poetpy
from poetpy import get_poetry


tape = vcr.VCR(
    cassette_library_dir='tests/cassettes',
    serializer='json',
    record_mode='once'
)

@vcr.use_cassette('tests/cassettes/test_get_poetry_author.yml')
def test_get_poetry_author():
    r1 = get_poetry('author', 'Ernest Dowson', 'author,title,linecount')

    r2 = get_poetry('author', 'Ernest Dowson', 'author,title,linecount', search_type='abs')

    assert isinstance(r1, list)
    assert isinstance(r1[0], dict)

    assert r1 == r2


@vcr.use_cassette('tests/cassettes/test_get_poetry_title.yml')
def test_get_poetry_title():

    r3 = get_poetry('title', "A Lover's Complaint", 'author,title,linecount')

    assert r3[0]['author'] == 'William Shakespeare'
    assert r3[0]['linecount'] == 331
    assert r3[0]['title'] == "A Lover's Complaint"

    r4 = get_poetry('title', "Orpheus with his Lute Made Trees", 'author,title,linecount')

    assert r4[0]['author'] == 'William Shakespeare'
    assert r4[0]['linecount'] == 12
    assert r4[0]['title'] == 'Orpheus with his Lute Made Trees'


@vcr.use_cassette('tests/cassettes/test_get_poetry_title.yml')
def test_get_poetry_title():
    pass
