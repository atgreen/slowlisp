Name:           cl-md5
Version:        20101006git
Release:        1%{?dist}
Summary:        An implementation of md5 in Common Lisp

Group:          System/Libraries
License:        BSD
URL:            git://beta.quicklisp.org/archive/md5/2010-10-06/md5-20101006-git.tgz
Source0:        md5-20101006-git.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
An implementation of RFC 2388, which is used to process form data
posted with GIT POST method using enctype "multipart/form-data".

%prep
%setup -q -n md5-20101006-git

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/md5
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/md5;
done;
install -m 644 md5.asd %{buildroot}%{_datadir}/common-lisp/source/md5;
cd %{buildroot}%{_datadir}/common-lisp/source/md5
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/md5/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source md5

%preun
/usr/sbin/unregister-common-lisp-source md5

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%{_datadir}/common-lisp/source/md5
%{_datadir}/common-lisp/systems/md5.asd

%changelog
* Wed Nov  3 2010 Anthony Green <green@moxielogic.com> - 20101006git-1
- Created.
