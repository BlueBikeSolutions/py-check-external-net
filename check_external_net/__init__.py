""" Check domains, IPs, and networks for internal/external/reserved """

import ipaddress

import publicsuffix2


__version__ = '1.0.0'


def is_external_address(addr):
    """ Similar to the ``ipaddress`` ``is_global`` property, test if the
    address (given any way ``ipaddress.ip_address`` allows) is an "external"
    (publically routable) address, checking the IPv4 address if it's a mapped
    IPv6

    Examples:

    Local IPv4
    >>> is_external_address('127.0.1.1')
    False

    Public IPv4
    >>> is_external_address('8.8.8.8')
    True

    Local IPv6 -> IPv4 mapped address
    >>> is_external_address('::ffff:127.0.0.1')
    False
    >>> is_external_address('::ffff:7f00:1')
    False

    Public IPv6 -> IPv4 mapped address
    >>> is_external_address('::ffff:8.8.8.8')
    True
    >>> is_external_address('::ffff:808:808')
    True
    """
    if not isinstance(addr, (ipaddress.IPv4Address, ipaddress.IPv6Address)):
        addr = ipaddress.ip_address(addr)

    try:
        mapped = addr.ipv4_mapped
    except AttributeError:
        pass
    else:
        if mapped:
            addr = mapped

    return addr.is_global


_PSL = None

def is_external_domain(domain):
    """ Test if the domain is an "external" domain.

    An external domain is classified as any child of a public suffix

    Examples:

    >>> is_external_domain('google.com')
    True
    >>> is_external_domain('tehunoth.com')
    True
    >>> is_external_domain('localhost')
    False
    >>> is_external_domain('tneohu')
    False
    >>> is_external_domain('test.cluster.local')
    False

    Controvertial, but thanks to Google this is a thing
    >>> is_external_domain('web.dev')
    True
    """
    parts = domain.strip('.').rsplit('.', 1)

    try:
        (_, suffix) = parts
    except ValueError:
        (suffix,) = parts

    global _PSL
    _PSL = _PSL or publicsuffix2.PublicSuffixList()

    try:
        _PSL.root[1][suffix]
    except KeyError:
        return False
    else:
        return True


def is_external_host(host):
    """ Takes a host, and checks that it's external either via IP reservation
    checking, or via domain public suffix checking

    Examples:

    >>> is_external_host('google.com')
    True
    >>> is_external_host('8.8.8.8')
    True
    >>> is_external_host('::ffff:8.8.8.8')
    True
    >>> is_external_host('::ffff:808:808')
    True

    >>> is_external_host('localhost')
    False
    >>> is_external_host('192.168.100.2')
    False
    >>> is_external_host('::ffff:192.168.100.2')
    False
    >>> is_external_host('::ffff:c0a8:6402')
    False
    """
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return is_external_domain(host)
    else:
        return is_external_address(host)
