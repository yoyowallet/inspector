Systems, Environments, Instances
================================

A brief explanation of the basic concepts in the Systems module

System
------

An abstract application that has a database
and where you will run your checks.

Examples:

* CRM
* Some backend app
* Data warehouse

No connection details at this point yet

Environment
-----------

No need to explain. Examples:

* Dev
* QA
* Staging
* Production

If you need a separate instance of Inspector for every environment,
for example due to network separation, you can use some generic name

Instance
--------

System + Environment, including connection details and credentials.
