# Poetpy

[![Documentation Status](https://readthedocs.org/projects/poetpy/badge/?version=latest)](https://poetpy.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/aschleg/poetpy.svg?branch=master)](https://travis-ci.org/aschleg/poetpy)
[![Build status](https://ci.appveyor.com/api/projects/status/jprq31sokv9rlbuh?svg=true)](https://ci.appveyor.com/project/aschleg/poetpy)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7abf894070ba46418181f9d07af68838)](https://www.codacy.com/app/aschleg/poetpy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=aschleg/poetpy&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/aschleg/poetpy/badge.svg?branch=master)](https://coveralls.io/github/aschleg/poetpy?branch=master)
![https://pypi.org/project/poetpy/](https://img.shields.io/badge/pypi%20version-1.1.0-blue.svg)
![https://pypi.org/project/petpy/](https://img.shields.io/badge/python-3.4%2C%203.5%2C%203.6-blue.svg)

Python wrapper of the [PoetryDB API](http://poetrydb.org/).

## Installation

`poetpy` is must easily installed using `pip`.

~~~ python
pip install poetpy
~~~

Otherwise, the project repository can be download and installed through invoking the 
`python install` command.

~~~ python
python setup.py install
~~~

## Examples

Extracting poetry and poets from the PoetryDB API requires at least one `input_term` 
parameter. The `input_term` parameter results can be further refined with a corresponding 
search term. For example, let's say we are interested in finding all of William Shakespeare's 
poems and sonnets available in the PoetryDB API. 

~~~ python
w = poetpy.get_poetry('author', 'William Shakespeare')
~~~

In the above example, the `input_term` is 'author' and the author we are interested 
in finding is 'William Shakespeare'. 

If we wanted to only output the lines and line counts of all of Shakespeare's poetry and sonnets, 
we can use the `output` parameter to narrow the returned results.

~~~ python
w = poetpy.get_poetry('author', 'William Shakespeare', 'lines,linecounts')
~~~

The default output format from the PoetryDB API is JSON; however, we can change the 
output to text by specifying the `output_format` parameter. 

~~~ python
w = poetpy.get_poetry('author', 'William Shakespeare', 'lines,linecounts', 'text')
~~~

The output text format will be newline escaped.

Combination searches are also allowed to enable users to further refine the returned search results. 
Each `input_term` should be given a corresponding search term delimited by a semi-colon. For example, 
let's say we want to find all of []John Milton's](https://en.wikipedia.org/wiki/John_Milton) poetry 
with [*Paradise Lost*](https://en.wikipedia.org/wiki/Paradise_Lost) in the title. 

~~~ python
get_poetry('title,author', 'Paradise Lost;Milton')
~~~

Different `input_term` parameter combinations can also be performed. Taking the above example, 
let's say we are actually only interested in finding Wordworth's poem *I Wandered Lonely As A Cloud*.

~~~ python
w = poetpy.get_poetry('author,title', 'William Shakespeare;I Wandered Lonely As A Cloud')
~~~

## Further Examples and Notebooks

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/aschleg/poetpy/master?filepath=notebooks)

A set of [Jupyter Notebooks](http://jupyter.org/) that further explore the potential usage of `poetpy` 
and the PoetryDB API. The notebooks can also be opened interactively using [binder](https://mybinder.org/)

* [Introduction to `poetpy`](https://github.com/aschleg/poetpy/blob/master/notebooks/Introduction%20to%20Poetpy.ipynb)

## Requirements

* Python 3.4+
  - `poetpy` should also work fine on Python 2.7, however; given that 2.7 support 
    will be discontinued in the near future, 2.7 will not be tested or supported.
* `requests >= 2.18`

## See Also

* [PoetryDB](https://github.com/thundercomb/poetrydb) Github page with more information 
  regarding the implementation and design of PoetryDB and its API. The README of the 
  repository also contains other examples for working with the API (though not in Python).
  
## License

GPL-2.0