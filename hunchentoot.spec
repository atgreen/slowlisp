%define contentdir /var/hunchentoot

Name:           hunchentoot
Version:        1.1.1
Release:        1%{?dist}
Summary:        A web server written in Common Lisp.

Group:          System Environment/Daemons
License:        BSD
URL:            http://beta.quicklisp.org/archive/hunchentoot/2010-10-06/%{name}-%{version}.tgz
Source0:        %{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires:        cl-bordeaux-threads
Requires:        cl-usocket
Requires:        cl-trivial-backtrace
Requires:        cl-rfc2388
Requires:        cl-md5
Requires:        cl+ssl
Requires:        cl-ppcre
Requires:        cl-fad
Requires:        cl-chunga
Requires(pre):   /usr/sbin/useradd
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
Hunchentoot is a web server written in Common Lisp and at the same
time a toolkit for building dynamic websites. As a stand-alone web
server, Hunchentoot is capable of HTTP/1.1 chunking (both directions),
persistent connections (keep-alive), and SSL.

Hunchentoot provides facilities like automatic session handling (with
and without cookies), logging, customizable error handling, and easy
access to GET and POST parameters sent by the client. It does not
include functionality to programmatically generate HTML output. For
this task you can use any library you like, e.g. (shameless self-plug)
CL-WHO or HTML-TEMPLATE.

Hunchentoot talks with its front-end or with the client over TCP/IP
sockets and optionally uses multiprocessing to handle several requests
at the same time. Therefore, it cannot be implemented completely in
portable Common Lisp. It currently works "natively" with LispWorks
(which is the main development and testing platform), and additionally
on all Lisps which are supported by the compatibility layers usocket
and Bordeaux Threads.

%prep
%setup -q -n %{name}-%{version}

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{contentdir}
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/hunchentoot/url-rewrite
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/hunchentoot/test
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/hunchentoot;
done;
for s in url-rewrite/*.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/hunchentoot/url-rewrite;
done;
for s in test/*.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/hunchentoot/test;
done;
for s in *.asd; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/hunchentoot;
done;
cd %{buildroot}%{_datadir}/common-lisp/source/hunchentoot
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/hunchentoot/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source hunchentoot

%preun
/usr/sbin/unregister-common-lisp-source hunchentoot

%pre
# Add the "apache" user
/usr/sbin/useradd -c "hunchentoot" -u 48 \
	-s /sbin/nologin -r -d %{contentdir} hunchentoot 2> /dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{contentdir}
%doc CHANGELOG* doc/*
%{_datadir}/common-lisp/source/hunchentoot
%{_datadir}/common-lisp/systems/hunchentoot.asd

%changelog
* Wed Nov  3 2010 Anthony Green <green@moxielogic.com> - 1.1.1-1
- Created.
