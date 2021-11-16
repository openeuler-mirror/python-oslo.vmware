%global _empty_manifest_terminate_build 0
Name:           python-oslo-vmware
Version:        2.34.1
Release:        1
Summary:        Oslo VMware library
License:        Apache-2.0
URL:            https://docs.openstack.org/oslo.vmware/latest/
Source0:        https://files.pythonhosted.org/packages/b2/db/de7f26b6d466d3bec50a68e824e5d8f5fe1dafd3211aba2797ce3ead8521/oslo.vmware-2.34.1.tar.gz
BuildArch:      noarch
%description
Oslo VMware library for OpenStack projects

%package -n python3-oslo-vmware
Summary:        Oslo VMware library
Provides:       python-oslo-vmware
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
# General requires
BuildRequires:  python3-stevedore
BuildRequires:  python3-netaddr
BuildRequires:  python3-six
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-pyyaml
BuildRequires:  python3-lxml
BuildRequires:  python3-suds-jurko
BuildRequires:  python3-eventlet
BuildRequires:  python3-requests
BuildRequires:  python3-urllib3
BuildRequires:  python3-oslo-concurrency
BuildRequires:  python3-oslo-context
# General requires
Requires:       python3-pbr
Requires:       python3-stevedore
Requires:       python3-netaddr
Requires:       python3-six
Requires:       python3-oslo-i18n
Requires:       python3-oslo-utils
Requires:       python3-pyyaml
Requires:       python3-lxml
Requires:       python3-suds-jurko
Requires:       python3-eventlet
Requires:       python3-requests
Requires:       python3-urllib3
Requires:       python3-oslo-concurrency
Requires:       python3-oslo-context
%description -n python3-oslo-vmware
Oslo VMware library for OpenStack projects

%package help
Summary:        Oslo VMware library
Provides:       python3-oslo-vmware-doc
%description help
Oslo VMware library for OpenStack projects

%prep
%autosetup -n oslo.vmware-%{version}

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
* Mon Nov 15 2021 OpenStack_SIG <openstack@openeuler.org> - 2.34.1-1
- Init package python3-oslo-vmware of version 2.34.1

