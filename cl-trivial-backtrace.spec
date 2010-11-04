Name:           cl-trivial-backtrace
Version:        20101006git
Release:        1%{?dist}
Summary:        Portable backtrace generation in Common Lisp

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/trivial-backtrace/2010-10-06/trivial-backtrace-20101006-git.tgz
Source0:        trivial-backtrace-20101006-git.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
On of the many things that didn't quite get into the Common Lisp
standard was how to get a Lisp to output its call stack when something
has gone wrong. As such, each Lisp has developed its own notion of
what to display, how to display it, and what sort of arguments can be
used to customize it. trivial-backtrace is a simple solution to
generating a backtrace portably. As of 16 May 2009, it supports
Allegro Common Lisp, LispWorks, ECL, MCL, SCL, SBCL and CMUCL. Its
interface consists of three functions and one variable:

    * print-backtrace
    * print-backtrace-to-stream
    * print-condition
    * *date-time-format*

%prep
%setup -q -n trivial-backtrace-20101006-git

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/trivial-backtrace/dev
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in dev/*.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/trivial-backtrace/dev;
done;
install -m 644 trivial-backtrace.asd %{buildroot}%{_datadir}/common-lisp/source/trivial-backtrace;
cd %{buildroot}%{_datadir}/common-lisp/source/trivial-backtrace
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/trivial-backtrace/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source trivial-backtrace

%preun
/usr/sbin/unregister-common-lisp-source trivial-backtrace

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%{_datadir}/common-lisp/source/trivial-backtrace
%{_datadir}/common-lisp/systems/trivial-backtrace.asd

%changelog
