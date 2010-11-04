Name:           cl-trivial-gray-streams
Version:        20101006cvs
Release:        1%{?dist}
Summary:        Gray stream compatibility library for common lisp.

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/trivial-gray-streams/2010-10-06/trivial-gray-streams-%{version}.tgz
Source0:        trivial-gray-streams-20101006-cvs.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
trivial-gray-streams is a trivial library which provides an extremely
thin compatibility layer for Gray streams.

%prep
%setup -q -n trivial-gray-streams-20101006-cvs

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/trivial-gray-streams
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/trivial-gray-streams;
done;
for s in *.asd; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/trivial-gray-streams;
done;
cd %{buildroot}%{_datadir}/common-lisp/source/trivial-gray-streams
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/trivial-gray-streams/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source trivial-gray-streams

%preun
/usr/sbin/unregister-common-lisp-source trivial-gray-streams

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%{_datadir}/common-lisp/source/trivial-gray-streams
%{_datadir}/common-lisp/systems/trivial-gray-streams.asd

%changelog
