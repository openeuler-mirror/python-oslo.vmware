%global _empty_manifest_terminate_build 0
Name:		python-oslo-vmware
Version:	3.7.0
Release:	2
Summary:	Oslo VMware library
License:	Apache-2.0
URL:		https://opendev.org/openstack/oslo.vmware
Source0:	https://files.pythonhosted.org/packages/3b/be/c0a53bf599b8dc5469d8dfac16a64d816e33918b97fb25e46e2d8a2fdfb2/oslo.vmware-3.7.0.tar.gz
BuildArch:	noarch

Requires:	python3-PyYAML
Requires:	python3-eventlet
Requires:	python3-lxml
Requires:	python3-netaddr
Requires:	python3-pbr
Requires:	python3-requests
Requires:	python3-stevedore
Requires:	python3-suds-jurko
Requires:	python3-urllib3

%description
Oslo VMware library for OpenStack projects


%package -n python3-oslo-vmware
Summary:	Oslo VMware library
Provides:	python-oslo-vmware
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-pbr
%description -n python3-oslo-vmware
Oslo VMware library for OpenStack projects


%package help
Summary:	Development documents and examples for oslo.vmware
Provides:	python3-oslo-vmware-doc
%description help
Oslo VMware library for OpenStack projects


%prep
%autosetup -n oslo.vmware-3.7.0

%build
%py3_build

%install
%py3_install
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

%files -n python3-oslo-vmware -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri Jan 22 2021 zhangy1317 <zhangy1317@foxmail.com>
- Add BuildRequires python3-pbr and python3-pbr
* Fri Jan 08 2021 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
