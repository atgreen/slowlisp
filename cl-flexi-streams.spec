Name:           cl-flexi-streams
Version:        1.0.7
Release:        1%{?dist}
Summary:        Flexible bivalent streams for Common Lisp

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/flexi-streams/2010-10-06/flexi-streams-%{version}.tgz
Source0:        flexi-streams-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller cl-trivial-gray-streams
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
FLEXI-STREAMS implements "virtual" bivalent streams that can be
layered atop real binary or bivalent streams and that can be used to
read and write character data in various single- or multi-octet
encodings which can be changed on the fly. It also supplies in-memory
binary streams which are similar to string streams.

%prep
%setup -q -n flexi-streams-%{version}

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/flexi-streams
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/flexi-streams;
done;
for s in *.asd; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/flexi-streams;
done;
cd %{buildroot}%{_datadir}/common-lisp/source/flexi-streams
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/flexi-streams/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source flexi-streams

%preun
/usr/sbin/unregister-common-lisp-source flexi-streams

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%{_datadir}/common-lisp/source/flexi-streams
%{_datadir}/common-lisp/systems/flexi-streams.asd

%changelog
