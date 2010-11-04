Name:           cl+ssl
Version:        20101006cvs
Release:        1%{?dist}
Summary:        Portable backtrace generation in Common Lisp

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/cl+ssl/2010-10-06/cl+ssl-20101006-cvs.tgz
Source0:        cl+ssl-20101006-cvs.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires:        cl-cffi
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
On of the many things that didn't quite get into the Common Lisp standard was how to get a Lisp to output its call stack when something has gone wrong. As such, each Lisp has developed its own notion of what to display, how to display it, and what sort of arguments can be used to customize it. cl+ssl is a simple solution to generating a backtrace portably. As of 16 May 2009, it supports Allegro Common Lisp, LispWorks, ECL, MCL, SCL, SBCL and CMUCL. Its interface consists of three functions and one variable:

    * print-backtrace
    * print-backtrace-to-stream
    * print-condition
    * *date-time-format*

%prep
%setup -q -n cl+ssl-20101006-cvs

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/cl+ssl
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/cl+ssl;
done;
install -m 644 cl+ssl.asd %{buildroot}%{_datadir}/common-lisp/source/cl+ssl;
cd %{buildroot}%{_datadir}/common-lisp/source/cl+ssl
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/cl+ssl/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source cl+ssl

%preun
/usr/sbin/unregister-common-lisp-source cl+ssl

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_datadir}/common-lisp/source/cl+ssl
%{_datadir}/common-lisp/systems/cl+ssl.asd

%changelog
* Wed Nov  4 2010 Anthony Green <green@moxielogic.com> - 20101006cvs-1
- Created.
