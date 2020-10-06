.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

==============
Website Search
==============

Module implements a website snippet that allows a global search on website pages.
Structure allows for extendibility for searches in other resources like 
blogs, attachments, or product descriptions.

Usage
=====

To use this module:
-------------------

* Drag the widget in any website container
* Save page
* search for any term

Or just create a link to /search , you will find the search interface available there.


To extend this module:
----------------------
The module structure is easily extendible by extending the website.search model
with a method named _do_search_{OBJECTNAME}  The general method _do_search will 
call it and include in search results.
Search results also have a type, that can be used in result rendering or for a 
future javascript search type selection.


Credits
=======

Contributors
------------

* Giovanni Francesco Capalbo <giovanni@therp.nl>
* Holger Brunn <hbrunn@therp.nl>


Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.


Known issues / Roadmap
======================
   * higlight searched text in list.
   * don't show key , but page title in search.
   * an website option to inject search in menubar.
   * more objects searched: blogs, attachments, product descriptions...
   * selection in widget of the specific type of search (page is the only one for now)
   * prerendering via cron job to speed up search on big high traffic deployments.


Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/website/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smash it by providing detailed and welcomed feedback.
