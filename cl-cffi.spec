Name:           cl-cffi
Version:        0.10.6
Release:        1%{?dist}
Summary:        Portable Foreign Function Interface for Common Lisp

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/cffi/2010-10-06/cffi_%{version}.tgz
Source0:        cffi_%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires:        cl-babel
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
CFFI, the Common Foreign Function Interface, purports to be a portable
foreign function interface for Common Lisp. The CFFI library is
composed of a Lisp-implementation-specific backend in the CFFI-SYS
package, and a portable frontend in the CFFI package.

The CFFI-SYS backend package defines a low-level interface to the
native FFI support in the Lisp implementation. It offers operators for
allocating and dereferencing foreign memory, calling foreign
functions, and loading shared libraries. The CFFI frontend provides a
declarative interface for defining foreign functions, structures,
typedefs, enumerated types, etc. It is implemented in portable ANSI CL
making use of the low-level operators exported by CFFI-SYS.


%prep
%setup -q -n cffi_%{version}

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/cffi/src
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in src/*.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/cffi/src;
done;
install -m 644 cffi.asd %{buildroot}%{_datadir}/common-lisp/source/cffi;
cd %{buildroot}%{_datadir}/common-lisp/source/cffi
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/cffi/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source cffi

%preun
/usr/sbin/unregister-common-lisp-source cffi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYRIGHT README TODO
%{_datadir}/common-lisp/source/cffi
%{_datadir}/common-lisp/systems/cffi.asd

%changelog
