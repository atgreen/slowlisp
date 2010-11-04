Name:           cl-fad
Version:        0.6.3
Release:        1%{?dist}
Summary:        Something TBD

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/cl-fad/2010-10-06/%{name}-%{version}.tgz
Source0:        %{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
Regexp for CL.

%prep
%setup -q -n %{name}-%{version}

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/cl-fad
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/cl-fad;
done;
install -m 644 cl-fad.asd %{buildroot}%{_datadir}/common-lisp/source/cl-fad;
cd %{buildroot}%{_datadir}/common-lisp/source/cl-fad
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/cl-fad/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source cl-fad

%preun
/usr/sbin/unregister-common-lisp-source cl-fad

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG doc
%{_datadir}/common-lisp/source/cl-fad
%{_datadir}/common-lisp/systems/cl-fad.asd

%changelog
* Wed Nov  4 2010 Anthony Green <green@moxielogic.com> - 0.6.3-1
- Created.

