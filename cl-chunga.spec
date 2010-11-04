Name:           cl-chunga
Version:        1.1.1
Release:        1%{?dist}
Summary:        Something TBD

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/cl-chunga/2010-10-06/chunga-%{version}.tgz
Source0:        chunga-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
Something TBD.

%prep
%setup -q -n chunga-%{version}

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/chunga
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/chunga;
done;
install -m 644 chunga.asd %{buildroot}%{_datadir}/common-lisp/source/chunga;
cd %{buildroot}%{_datadir}/common-lisp/source/chunga
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/chunga/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source chunga

%preun
/usr/sbin/unregister-common-lisp-source chunga

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG.txt doc
%{_datadir}/common-lisp/source/chunga
%{_datadir}/common-lisp/systems/chunga.asd

%changelog
* Wed Nov  4 2010 Anthony Green <green@moxielogic.com> - 1.1.1-1
- Created.
