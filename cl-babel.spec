Name:           cl-babel
Version:        20101006darcs
Release:        1%{?dist}
Summary:        A charset encoding/decoding library for Common Lisp

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/babel/2010-10-06/babel-20101006-darcs.tgz
Source0:        babel-20101006-darcs.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires:        cl-trivial-features
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
Babel is a charset encoding/decoding library, not unlike GNU libiconv,
but completely written in Common Lisp.

It strives to achieve decent performance. To that effect, we use
Clozure CL's approach of calculating the destination buffer size in
advance. Most of the encoding/decoding algorithms have been adapted
from Clozure CL's source. Another important goal is
reusability. Similarly to SBCL, we define an interface wherein the
algorithms can be reused between a variety of data types so long we're
dealing with conversions between octets and unicode code points.

Babel comes with converters between strings and octet vectors but can
be easily extended to deal with, e.g., strings and foreign memory,
vectors and Closure's runes, etc...

%prep
%setup -q -n babel-20101006-darcs

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/babel/src
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in src/*.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/babel/src;
done;
install -m 644 babel.asd %{buildroot}%{_datadir}/common-lisp/source/babel;
install -m 644 babel-streams.asd %{buildroot}%{_datadir}/common-lisp/source/babel;
cd %{buildroot}%{_datadir}/common-lisp/source/babel
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/babel/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source babel

%preun
/usr/sbin/unregister-common-lisp-source babel

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYRIGHT NOTES README HEADER
%{_datadir}/common-lisp/source/babel
%{_datadir}/common-lisp/systems/babel.asd
%{_datadir}/common-lisp/systems/babel-streams.asd

%changelog
* Wed Nov  4 2010 Anthony Green <green@moxielogic.com> - 20101006darcs-1
- Created.
