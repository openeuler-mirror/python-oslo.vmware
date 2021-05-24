%global _empty_manifest_terminate_build 0
Name:		python-oslo-vmware
Version:	2.31.0
Release:	1
Summary:	Oslo VMware library
License:	Apache-2.0
URL:		https://docs.openstack.org/oslo.vmware/latest/
Source0:	https://files.pythonhosted.org/packages/10/42/1c0a4e01321af46c6b34145a3bd7a7ec5d26f56a979831450d453853ae08/oslo.vmware-2.31.0.tar.gz
BuildArch:	noarch
%description
========================
Team and repository tags
========================

.. image:: https://governance.openstack.org/tc/badges/oslo.vmware.svg
    :target: https://governance.openstack.org/tc/reference/tags/index.html

.. Change things from this point on

===================================================
 oslo.vmware --- VMware support code for OpenStack
===================================================

.. image:: https://img.shields.io/pypi/v/oslo.vmware.svg
    :target: https://pypi.org/project/oslo.vmware/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/oslo.vmware.svg
    :target: https://pypi.org/project/oslo.vmware/
    :alt: Downloads

The Oslo VMware library provides support for common VMware operations
and APIs.

* License: Apache License, Version 2.0
* Documentation: https://docs.openstack.org/oslo.vmware/latest/
* Source: https://git.openstack.org/cgit/openstack/oslo.vmware
* Bugs: https://bugs.launchpad.net/oslo.vmware
* Release notes: https://docs.openstack.org/releasenotes/oslo.vmware/




%package -n python2-oslo-vmware
Summary:	Oslo VMware library
Provides:	python2-oslo-vmware
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
Requires:	python2-pbr
Requires:	python2-stevedore
Requires:	python2-netaddr
Requires:	python2-six
Requires:	python2-oslo-i18n
Requires:	python2-oslo-utils
Requires:	python2-pyyaml
Requires:	python2-lxml
Requires:	python2-suds-jurko
Requires:	python2-eventlet
Requires:	python2-requests
Requires:	python2-urllib3
Requires:	python2-oslo-concurrency
%description -n python2-oslo-vmware
========================
Team and repository tags
========================

.. image:: https://governance.openstack.org/tc/badges/oslo.vmware.svg
    :target: https://governance.openstack.org/tc/reference/tags/index.html

.. Change things from this point on

===================================================
 oslo.vmware --- VMware support code for OpenStack
===================================================

.. image:: https://img.shields.io/pypi/v/oslo.vmware.svg
    :target: https://pypi.org/project/oslo.vmware/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/oslo.vmware.svg
    :target: https://pypi.org/project/oslo.vmware/
    :alt: Downloads

The Oslo VMware library provides support for common VMware operations
and APIs.

* License: Apache License, Version 2.0
* Documentation: https://docs.openstack.org/oslo.vmware/latest/
* Source: https://git.openstack.org/cgit/openstack/oslo.vmware
* Bugs: https://bugs.launchpad.net/oslo.vmware
* Release notes: https://docs.openstack.org/releasenotes/oslo.vmware/




%package help
Summary:	Development documents and examples for oslo.vmware
Provides:	python2-oslo-vmware-doc
%description help
========================
Team and repository tags
========================

.. image:: https://governance.openstack.org/tc/badges/oslo.vmware.svg
    :target: https://governance.openstack.org/tc/reference/tags/index.html

.. Change things from this point on

===================================================
 oslo.vmware --- VMware support code for OpenStack
===================================================

.. image:: https://img.shields.io/pypi/v/oslo.vmware.svg
    :target: https://pypi.org/project/oslo.vmware/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/oslo.vmware.svg
    :target: https://pypi.org/project/oslo.vmware/
    :alt: Downloads

The Oslo VMware library provides support for common VMware operations
and APIs.

* License: Apache License, Version 2.0
* Documentation: https://docs.openstack.org/oslo.vmware/latest/
* Source: https://git.openstack.org/cgit/openstack/oslo.vmware
* Bugs: https://bugs.launchpad.net/oslo.vmware
* Release notes: https://docs.openstack.org/releasenotes/oslo.vmware/




%prep
%autosetup -n oslo.vmware-2.31.0

%build
%py2_build

%install
%py2_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python2-oslo-vmware -f filelist.lst
%dir %{python2_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri May 07 2021 OpenStack_SIG <openstack@openeuler.org>
- Package Spec generated
