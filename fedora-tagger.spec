%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get _python_lib; print get_python_lib()")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

%define modname fedoratagger
%define eggname fedora_tagger

Name:           fedora-tagger
Version:        0.1.5
Release:        1%{?dist}
Summary:        A web application for adding and ranking tags for Fedora packages

License:        LGPLv2
URL:            https://github.com/ralphbean/fedora-tagger
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel
BuildRequires:  libcurl-devel
BuildRequires:  python-kitchen
BuildRequires:  python-nose
BuildRequires:  python-paste
BuildRequires:  python-paste-deploy
BuildRequires:  TurboGears2
BuildRequires:  python-pylons
BuildRequires:  python-mako
BuildRequires:  python-zope-sqlalchemy
BuildRequires:  python-sqlalchemy
BuildRequires:  python-repoze-what
BuildRequires:  python-repoze-who-friendlyform
BuildRequires:  python-repoze-what-pylons
BuildRequires:  python-repoze-who
BuildRequires:  python-repoze-what-plugins-sql
BuildRequires:  python-kitchen
BuildRequires:  pycurl
BuildRequires:  python-tw2-core
BuildRequires:  python-tw2-forms
BuildRequires:  python-tw2-jqplugins-ui
BuildRequires:  python-tw2-jqplugins-gritter
BuildRequires:  python-docutils
BuildRequires:  python-bunch
BuildRequires:  python-fedora
BuildRequires:  python-fedora-turbogears2
BuildRequires:  python-tgscheduler

Requires:       TurboGears2
Requires:       python-mako
Requires:       python-zope-sqlalchemy
Requires:       python-sqlalchemy
Requires:       python-repoze-what
Requires:       python-repoze-who-friendlyform
Requires:       python-repoze-what-pylons
Requires:       python-repoze-who
#Requires:       python-repoze-what-quickstart
Requires:       python-repoze-what-plugins-sql
Requires:       python-kitchen
Requires:       pycurl
Requires:       python-tw2-core
Requires:       python-tw2-jqplugins-gritter
Requires:       python-tw2-jqplugins-ui
Requires:       python-fedora-turbogears2
Requires:       python-psycopg2
Requires:       python-tgscheduler

%description
A web application for adding and ranking tags for Fedora packages.

%prep
%setup -q

%if %{?rhel}%{!?rhel:0} >= 6

# Make sure that epel/rhel picks up the correct version of webob
awk 'NR==1{print "import __main__; __main__.__requires__ = __requires__ = [\"WebOb>=1.0\"]; import pkg_resources"}1' setup.py > setup.py.tmp
mv setup.py.tmp setup.py

%endif


%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build \
    --install-data=%{_datadir} --root %{buildroot}
%{__python} setup.py archive_tw2_resources -f -o %{buildroot}%{_datadir}/%{name}/public/toscawidgets -d fedora_tagger

rm -fr %{buildroot}%{python_sitelib}/migration

%{__mkdir_p} %{buildroot}%{_datadir}/%{name}/apache
%{__install} apache/%{modname}.wsgi %{buildroot}%{_datadir}/%{name}/apache/%{modname}.wsgi


%files
%doc README.rst
%{_datadir}/%{name}/
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{eggname}-%{version}-py%{pyver}.egg-info/

%changelog
* Wed May 23 2012 Ralph Bean <rbean@redhat.com> - 0.1.5-1
- python-tgscheduler now handles updating package metadata.
- Removed a hardcoded link to the stg deployment of f-packages.
* Thu Apr 26 2012 Ralph Bean <rbean@redhat.com> - 0.1.4-1
- Added a controller method /_update to get new packages from pkgdb+yum
- Unicode safeguards in websetup/bootstrap.py
* Wed Apr 25 2012 Ralph Bean <rbean@redhat.com> - 0.1.3-1
- New version.  Fixes a typo-bug in the gritter notification
- Added LGPLv2 license.
* Wed Apr 25 2012 Ralph Bean <rbean@redhat.com> - 0.1.2-2
- Dependency fixes
- Removed the patch; using awk instead
* Thu Mar 29 2012 Ralph Bean <rbean@redhat.com> - 0.1.2-1
- Statistics window
- Toggle notifications
* Tue Feb 28 2012 Ralph Bean <rbean@redhat.com> - 0.1.1-1
- jQuery UI styling
- Statistics
- Toggle Notifications
- Misc fixups
* Mon Jan 09 2012 Luke Macken <lmacken@redhat.com> - 0.1-1
- Initial RPM package
