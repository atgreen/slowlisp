Name:           cl-usocket
Version:        20101006svn
Release:        1%{?dist}
Summary:        A library of useful utilities for Common Lisp

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/usocket/2010-10-06/usocket-20101006-svn.tgz
Source0:        usocket-20101006-svn.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
Usocket's goal is to reduce duplication of effort and improve
portability of Common Lisp code according to its own idiosyncratic and
rather conservative aesthetic.

%prep
%setup -q -n usocket-20101006-svn

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/usocket/backend
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/usocket/vendor
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in backend/*.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/usocket/backend;
done;
for s in vendor/*.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/usocket/vendor;
done;
for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/usocket;
done;
install -m 644 usocket.asd %{buildroot}%{_datadir}/common-lisp/source/usocket;
cd %{buildroot}%{_datadir}/common-lisp/source/usocket
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/usocket/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source usocket

%preun
/usr/sbin/unregister-common-lisp-source usocket

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE TODO CHANGES README doc
%{_datadir}/common-lisp/source/usocket
%{_datadir}/common-lisp/systems/usocket.asd

%changelog
