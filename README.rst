kbsoftware.co.uk
****************

WIP
===

Move CRM from ``pkimber_net`` to ``kbsoftware_couk``::

  pg_dump test_pkimber_net_patrick -f test_pkimber_net_patrick.sql
  # psql -U postgres test_pkimber_net_patrick
  drop database test_kbsoftware_couk_patrick;
  psql -X -U postgres -c "CREATE DATABASE test_kbsoftware_couk_patrick TEMPLATE=template0 ENCODING='utf-8';"

  psql -d test_kbsoftware_couk_patrick -f test_pkimber_net_patrick.sql 2> out.log
  cat out.log

.. important:: Don't forget to copy files (private and public).

Development
===========

Virtual Environment
-------------------

::

  pyvenv-3.4 --without-pip venv-kbsoftware_couk
  source venv-kbsoftware_couk/bin/activate
  wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
  python get-pip.py

  pip install -r requirements/local.txt

Testing
-------

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
-----

::

  ./init_dev.sh

Browse to http://localhost:8000/::

  user          staff
  password      letmein

Release and Deploy
==================

https://pkimber.net/open/
