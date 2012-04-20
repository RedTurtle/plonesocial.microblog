.. contents::

Introduction
============

Plonesocial.microblog is part of the `plonesocial suite`_.

This package provides a building block for Plone integrators who want to create
a custom social business solution in Plone.

If you're an end-user looking for a pre-integrated solution,
you should install `plonesocial.suite`_ instead.


plonesocial.microblog
=====================

Plonesocial.microblog uses plone.app.discussion to store microblog status updates
in an annotation on the Site Root.

It currently re-exposes a slightly modified p.a.discussion viewlet as a portlet.

bugs
----

- setting a real discussion comment somewhere else than on the SiteRoot
  somehow also creates a second reply on the SiteRoot

todo
----

- re-use the `plonesocial.activitystream`_ portlet for stream rendering
- narrow the current portlet to only the status update input form


Plonesocial
===========

Plonesocial consists of:

`plonesocial.suite`_
 An out-of-the-box social business experience integrating all of the above.
 If you're an end user, this is what you're looking for.

`plonesocial.microblog`_
 Status updates

`plonesocial.activitystream`_
 Lists content changes, discussion replies, and status updates

plonesocial.network
 Follow/unfollow of users

plonesocial.like
 Favoriting of content

`plonesocial.buildout`_
 Developer buildout. Not a Python package. Intended for Plonesocial developers only.

This is a work in progress and not suitable for general release yet.

.. _plonesocial suite: https://github.com/cosent/plonesocial.suite
.. _plonesocial.microblog: https://github.com/cosent/plonesocial.microblog
.. _plonesocial.activitystream: https://github.com/cosent/plonesocial.activitystream
.. _plonesocial.suite: https://github.com/cosent/plonesocial.suite
.. _plonesocial.buildout: https://github.com/cosent/plonesocial.buildout
