%define QLYEAR   2010
%define QLMONTH  11 
%define QLDAY    07

Name:           cl-alexandria
Version:        %{QLYEAR}%{QLMONTH}%{QLDAY}git
Release:        1%{?dist}
Summary:        A library of useful utilities for Common Lisp

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/alexandria/%{QLYEAR}-%{QLMONTH}-%{QLDAY}/alexandria-%{QLYEAR}%{QLMONTH}%{QLDAY}-git.tgz
Source0:        alexandria-%{QLYEAR}%{QLMONTH}%{QLDAY}-git.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller cl-trivial-gray-streams
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
Alexandria's goal is to reduce duplication of effort and improve
portability of Common Lisp code according to its own idiosyncratic and
rather conservative aesthetic.

%prep
%setup -q -n alexandria-%{QLYEAR}%{QLMONTH}%{QLDAY}-git

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/alexandria
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/alexandria;
done;
install -m 644 alexandria.asd %{buildroot}%{_datadir}/common-lisp/source/alexandria;
cd %{buildroot}%{_datadir}/common-lisp/source/alexandria
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/alexandria/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source alexandria

%preun
/usr/sbin/unregister-common-lisp-source alexandria

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%{_datadir}/common-lisp/source/alexandria
%{_datadir}/common-lisp/systems/alexandria.asd

%changelog
* Mon Nov  8 2010 Anthony Green <green@moxielogic.com> - 20101107git-1
- Upgraded.

* Wed Nov  4 2010 Anthony Green <green@moxielogic.com> - 20101006git-1
- Created.
