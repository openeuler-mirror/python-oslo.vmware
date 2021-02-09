%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1

Name:           python-oslo-vmware
Version:        3.7.0
Release:        4
Summary:        Oslo VMware library for OpenStack projects
License:        ASL 2.0
URL:            https://opendev.org/openstack/oslo.vmware
Source0:        https://tarballs.openstack.org/oslo.vmware/oslo.vmware-3.7.0.tar.gz
BuildArch:      noarch

%description
Oslo VMware library for OpenStack projects

%package -n python3-oslo-vmware
Summary:        Oslo VMware library for OpenStack projects
%{?python_provide:%python_provide python3-oslo-vmware}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  git
# test dependencies
BuildRequires: python3-ddt
BuildRequires: python3-fixtures
BuildRequires: python3-mock
BuildRequires: python3-stestr
BuildRequires: python3-subunit
BuildRequires: python3-testtools
BuildRequires: python3-suds
BuildRequires: python3-oslo-concurrency
BuildRequires: python3-oslo-context
BuildRequires: python3-oslo-utils
BuildRequires: python3-oslo-i18n
BuildRequires: python3-eventlet
BuildRequires: python3-oslo-i18n
BuildRequires: python3-oslo-utils
BuildRequires: python3-requests >= 2.14.2
BuildRequires: python3-suds
BuildRequires: python3-netaddr
# Required to compile translation files
BuildRequires: python3-testscenarios
BuildRequires: python3-babel

BuildRequires: python3-lxml

Requires:  python3-pbr
Requires:  python3-eventlet
Requires:  python3-oslo-concurrency >= 3.26.0
Requires:  python3-oslo-context >= 2.19.2
Requires:  python3-oslo-i18n >= 3.15.3
Requires:  python3-oslo-utils
Requires:  python3-requests
Requires:  python3-stevedore >= 1.20.0
Requires:  python3-suds >= 0.6
Requires:  python3-urllib3
Requires:  python3-netaddr
Requires:  python-oslo-vmware-lang = %{version}-%{release}

Requires:  python3-lxml
Requires:  python3-PyYAML

%description -n python3-oslo-vmware
Oslo VMware library for OpenStack projects

%if 0%{?with_doc}
%package -n python-oslo-vmware-doc
Summary:    Documentation for OpenStack common VMware library

BuildRequires: python3-sphinx
BuildRequires: python3-sphinxcontrib-apidoc
BuildRequires: python3-openstackdocstheme

%description -n python-oslo-vmware-doc
Documentation for OpenStack common VMware library.
%endif

%package -n python3-oslo-vmware-tests
Summary:    Test subpackage for OpenStack common VMware library

Requires: python3-oslo-vmware = %{version}-%{release}
Requires: python3-fixtures
Requires: python3-mock
Requires: python3-subunit
Requires: python3-testtools
Requires: python3-suds >= 0.6
Requires: python3-oslo-context
Requires: python3-oslo-utils
Requires: python3-oslo-i18n >= 3.15.3
Requires: python3-testscenarios

%description -n python3-oslo-vmware-tests
Tests for OpenStack common VMware library.

%package  -n python-oslo-vmware-lang
Summary:   Translation files for Oslo vmware library

%description -n python-oslo-vmware-lang
Translation files for Oslo vmware library

%prep

%autosetup -n oslo.vmware-3.7.0 -S git
# FIXME(hguemar): requirements blocks 0.20.1 due to lp#1696094
# but eventlet 0.20.1-2 package has backported the fix
sed -i '/eventlet/s/!=0.20.1,//' requirements.txt
# FIXME(hguemar): we use system lxml from EL7
sed -i '/lxml/s/,>=3.4.1//' requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -b html doc/source doc/build/html

# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

# Generate i18n files
python3 setup.py compile_catalog -d build/lib/oslo_vmware/locale --domain oslo_vmware

%install
%{py3_install}

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python3_sitelib}/oslo_vmware/locale/*/LC_*/oslo_vmware*po
rm -f %{buildroot}%{python3_sitelib}/oslo_vmware/locale/*pot
mv %{buildroot}%{python3_sitelib}/oslo_vmware/locale %{buildroot}%{_datadir}/locale

# Find language files
%find_lang oslo_vmware --all-name

%check
rm -f ./oslo_vmware/tests/test_hacking.py
export OS_TEST_PATH="./oslo_vmware/tests"
PYTHON=python3 stestr-3 --test-path $OS_TEST_PATH run

%files -n python3-oslo-vmware
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_vmware
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/oslo_vmware/tests

%if 0%{?with_doc}
%files -n python-oslo-vmware-doc
%doc doc/build/html
%license LICENSE
%endif

%files -n python3-oslo-vmware-tests
%{python3_sitelib}/oslo_vmware/tests

%files -n python-oslo-vmware-lang -f oslo_vmware.lang
%license LICENSE

%changelog
* Mon Jan 25 2021 zhangy1317 <zhangy1317@foxmail.com>
- Add BuildRequires python3-pip

* Wed Oct 21 2020 Joel Capitao <jcapitao@redhat.com> 3.7.0-2
- Enable sources tarball validation using GPG signature.

* Fri Sep 18 2020 RDO <dev@lists.rdoproject.org> 3.7.0-1
- Update to 3.7.0

