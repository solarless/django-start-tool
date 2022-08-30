###########################
django-start-tool |version|
###########################

.. |version| image:: https://img.shields.io/pypi/v/django-start-tool
    :target: https://pypi.org/project/django-start-tool
    :alt: PyPI

Usage
=====

Detailed usage information can be found by typing ``django-start --help``

Examples
========

Create default project:

.. code-block:: shell

    $ django-start

    # Is equivalent to

    $ django-admin startproject config .

Create project from template:

.. code-block:: shell

    $ django-start \
    > -t /path/to/template

    # Is equivalent to

    $ django-admin startproject \
    > --template /path/to/template

.. code-block:: shell

    $ django-start \
    > -t https://github.com/<user>/<repository>/archive/main.zip

    # Is equivalent to

    $ django-admin startproject \
    > --template https://github.com/<user>/<repository>/archive/main.zip

Add files to rendering (in addition to ``*-tpl``):

.. code-block:: shell

    $ django-start \
    > -t /path/to/template \
    > -r '*.env Procfile'

    # Is equivalent to

    $ django-admin startproject \
    > --template /path/to/template \
    > --extension env \
    > --name Procfile

Exclude directories from rendering (in addition to ``.git`` and ``__pycache__``):

.. code-block:: shell

    $ django-start \
    > -t /path/to/template \
    > -x 'data logs'

    # Is equivalent to

    $ django-admin startproject \
    > --template /path/to/template \
    > --exclude data,logs
