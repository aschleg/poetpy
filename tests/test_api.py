import vcr
import pytest
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

    r3 = get_poetry('author', 'Ernest Dowson', 'author,title,linecount', output_format='text')

    assert isinstance(r3, str)


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


@vcr.use_cassette('tests/cassettes/test_get_poetry_lines.yml')
def test_get_poetry_lines():
    r = get_poetry('lines', 'Latitudeless Place', 'author,title,linecount')

    assert r[0]['author'] == 'Emily Dickinson'
    assert int(r[0]['linecount']) == 20
    assert r[0]['title'] == 'Now I knew I lost her --'


@vcr.use_cassette('tests/cassettes/test_get_poetry_linecount.yml')
def test_get_poetry_linecount():
    r = get_poetry('linecount', '51', 'author,linecount,title')

    assert isinstance(r, list)
    assert r[0]['author'] == 'Edward Thomas'
    assert r[1]['author'] == 'John Clare'
    assert r[2]['author'] == 'Percy Bysshe Shelley'

    assert r[0]['linecount'] == r[1]['linecount'] == r[2]['linecount']


@vcr.use_cassette('tests/cassettes/test_get_poetry_combined.yml')
def test_get_poetry_combination():
    r = get_poetry('author,title', 'William Shakespeare;Spring and Winter ii', 'author,title')

    assert r[0]['author'] == 'William Shakespeare'
    assert r[0]['title'] == 'Spring and Winter ii'


def test_poetry_exceptions():
    with pytest.raises(ValueError):
        r = get_poetry('author', output_format='lfhdsubg')
