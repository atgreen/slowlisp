Name:           cl-trivial-features
Version:        20101006darcs
Release:        1%{?dist}
Summary:        Provides a consistent *FEATURES* across multiple Common Lisp implementations

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/trivial-features/2010-10-06/trivial-features-20101006-darcs.tgz
Source0:        trivial-features-20101006-darcs.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
trivial-features ensures consistent *FEATURES* across multiple Common
Lisp implementations.

%prep
%setup -q -n trivial-features-20101006-darcs

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/trivial-features/src
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in src/*.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/trivial-features/src;
done;
install -m 644 trivial-features.asd %{buildroot}%{_datadir}/common-lisp/source/trivial-features;
cd %{buildroot}%{_datadir}/common-lisp/source/trivial-features
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/trivial-features/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source trivial-features

%preun
/usr/sbin/unregister-common-lisp-source trivial-features

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc SPEC COPYRIGHT README
%{_datadir}/common-lisp/source/trivial-features
%{_datadir}/common-lisp/systems/trivial-features.asd

%changelog
