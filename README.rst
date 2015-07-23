check-srx
=========

.. image:: https://pypip.in/v/check-srx/badge.png
    :target: https://pypi.python.org/pypi/check-srx
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/scibi/check_srx.png
   :target: https://travis-ci.org/scibi/check_srx
   :alt: Latest Travis CI build status

Icinga/Nagios plugin for Juniper SRX firewalls

Usage
-----

.. code-block:: shell

   $ check_srx --help
   usage: check_srx [-h] [-H HOSTNAME] [-u USER] [-v]
   
   Check SRX Cluster status
   
   optional arguments:
     -h, --help            show this help message and exit
     -H HOSTNAME, --hostname HOSTNAME
                           SRX hostname or IP address
     -u USER, --username USER
                           User name
     -v, --verbose         increase output verbosity (use up to 3 times)

Sample Output
^^^^^^^^^^^^^

.. code-block:: shell

   $ check_srx -H 10.0.0.10 -u username
   CLUSTERSTATUS CRITICAL - rg_0_device1_status: lost (Wrong node status: lost)



Installation
------------

Right now you can install check_srx direclty from the repository:

.. code-block:: shell

   $ pip install git+https://github.com/scibi/check_srx


Requirements
^^^^^^^^^^^^

Compatibility
-------------

Licence
-------

Authors
-------

`check-srx` was written by `Patryk Ściborek <patryk@sciborek.com>`_.
