Name:           cl-who
Version:        0.11.1
Release:        1%{?dist}
Summary:        A charset encoding/decoding library for Common Lisp

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/cl-who/2010-10-06/%{name}-%{version}.tgz
Source0:        %{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description

%prep
%setup -q

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/cl-who/src
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/cl-who/src;
done;
install -m 644 cl-who.asd %{buildroot}%{_datadir}/common-lisp/source/cl-who;
cd %{buildroot}%{_datadir}/common-lisp/source/cl-who
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/cl-who/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source cl-who

%preun
/usr/sbin/unregister-common-lisp-source cl-who

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG doc
%{_datadir}/common-lisp/source/cl-who
%{_datadir}/common-lisp/systems/cl-who.asd

%changelog
* Thu Nov  4 2010 Anthony Green <green@moxielogic.com> - 0.11.1-1
- Created.
