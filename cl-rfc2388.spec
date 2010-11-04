Name:           cl-rfc2388
Version:        20101006http
Release:        1%{?dist}
Summary:        An implementation of RFC 2388 in Common Lisp

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/rfc2388/2010-10-06/rfc2388-20101006-http.tgz
Source0:        rfc2388-20101006-http.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
An implementation of RFC 2388, which is used to process form data
posted with HTTP POST method using enctype "multipart/form-data".

%prep
%setup -q -n rfc2388-20101006-http

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/rfc2388
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/rfc2388;
done;
install -m 644 rfc2388.asd %{buildroot}%{_datadir}/common-lisp/source/rfc2388;
cd %{buildroot}%{_datadir}/common-lisp/source/rfc2388
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/rfc2388/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source rfc2388

%preun
/usr/sbin/unregister-common-lisp-source rfc2388

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%{_datadir}/common-lisp/source/rfc2388
%{_datadir}/common-lisp/systems/rfc2388.asd

%changelog
* Wed Nov  4 2010 Anthony Green <green@moxielogic.com> - 20101006http-1
- Created.
