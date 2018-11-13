Check external net
==================

Check domains, IPs, and hosts to ensure they are "external"

This is intended to be used to check user-entered host names to ensure that
they only contain IP addresses, or domain names that are considered to be
external to your system. No IP addresses that are reserved (eg
``127.0.0.0/8``, ``192.168.0.0/16``, ``fc00::/7``) and no domains that aren't
children of a public suffix (eg *.com is okay, *.local is not).

Internal IP addresses (``is_external_address``)
-----------------------------------------------

If we are able to discern an `IPv4 mapped`_ address, that is passed through
as the address to check rather than the original.

From there, all `IPv4 reserved networks`_, and `IPv6 reserved networks`_ are
considered "internal" (see `is_global`_)

.. `IPv4 mapped`: https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.ipv4_mapped
.. `IPv4 reserved networks`: https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml
.. `IPv6 reserved networks`: https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml
.. `is_global`: https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_global

Internal domains (``is_external_domain``)
-----------------------------------------

A domain is considered internal if it is not external.

A domain is considered external if the last suffix (the final part of a domain
after the last ``.`` character) exists in the
`Mozilla public suffix registry`_.

.. `Mozilla public suffix registry`: https://publicsuffix.org

Internal hosts (``is_external_host``)
-------------------------------------

Hosts are parsed as IP addresses via the `ipaddress.ip_address`_ function. If
this succeeds, it's treated to the rules of an internal IP address. Otherwise,
it's treated as a domain.

*Usage*

::

>>> check_external_net.is_external_host('127.0.0.1')
False
>>> check_external_net.is_external_host('::0')
False
>>> check_external_net.is_external_host('8.8.8.8')
True
>>> check_external_net.is_external_host('::ffff:8.8.8.8')
True
>>> check_external_net.is_external_host('localhost')
False
>>> check_external_net.is_external_host('cluster.local')
False
>>> check_external_net.is_external_host('google.com')
True
>>> check_external_net.is_external_host('dutyof.care')
True

.. `ipaddress.ip_address`: https://docs.python.org/3/library/ipaddress.html#ipaddress.ip_address
