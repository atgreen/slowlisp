Name:           cl-bordeaux-threads
Version:        0.8.0
Release:        1%{?dist}
Summary:        Portable shared-state concurrency for Common Lisp

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/bordeaux-threads/2010-10-06/cl-%{name}-%{version}.tgz
Source0:        bordeaux-threads-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires:        cl-alexandria
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
BORDEAUX-THREADS is a proposed standard for a minimal MP/Threading
interface. It is similar to the CLIM-SYS threading and lock support.

%prep
%setup -q -n bordeaux-threads-%{version}

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/bordeaux-threads/src
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in src/*.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/bordeaux-threads/src;
done;
install -m 644 version.lisp-expr %{buildroot}%{_datadir}/common-lisp/source/bordeaux-threads;
install -m 644 bordeaux-threads.asd %{buildroot}%{_datadir}/common-lisp/source/bordeaux-threads;
cd %{buildroot}%{_datadir}/common-lisp/source/bordeaux-threads
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/bordeaux-threads/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source bordeaux-threads

%preun
/usr/sbin/unregister-common-lisp-source bordeaux-threads

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%{_datadir}/common-lisp/source/bordeaux-threads
%{_datadir}/common-lisp/systems/bordeaux-threads.asd

%changelog
* Wed Nov  4 2010 Anthony Green <green@moxielogic.com> - 0.8.0-1
- Created.
