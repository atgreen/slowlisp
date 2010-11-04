Name:           cl-base64
Version:        20101006git
Release:        1%{?dist}
Summary:        Something TBD

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/cl-base64/2010-10-06/%{name}-%{version}.tgz
Source0:        %{name}-20101006-git.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
Regexp for CL.

%prep
%setup -q -n %{name}-20101006-git

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/cl-base64
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/cl-base64;
done;
install -m 644 cl-base64.asd %{buildroot}%{_datadir}/common-lisp/source/cl-base64;
cd %{buildroot}%{_datadir}/common-lisp/source/cl-base64
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/cl-base64/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source cl-base64

%preun
/usr/sbin/unregister-common-lisp-source cl-base64

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%{_datadir}/common-lisp/source/cl-base64
%{_datadir}/common-lisp/systems/cl-base64.asd

%changelog
