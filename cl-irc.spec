Name:           cl-irc
Version:        20101006svn
Release:        1%{?dist}
Summary:        An IRC client library for Common Lisp

Group:          System/Libraries
License:        BSD
URL:            http://beta.quicklisp.org/archive/cl-irc/2010-10-06/%{name}-20101006-svn.tgz
Source0:        %{name}-20101006-svn.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:   common-lisp-controller
Requires:        common-lisp-controller
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

%description
cl-irc is an implementation of the client-side protocol.  It is not
impossible to add the server-side but it has simple not been done yet
(and the current authors have no plans of doing so, although patches
are certainly welcome).

Here's the basic idea: You tell the library to connect to an IRC
server; it gives you a connection object in return.  You call
`read-message-loop' which reads messages from the server.  For each
message that is received, it is parsed and the library tries to find a
hook to apply to the message (see ``Hooks'') and if successful the
hook will be called with the message as its single argument.  You
customize the library via the hooks.

%prep
%setup -q -n %{name}-20101006-svn

%build

%install
%{__rm} -rf %{buildroot}

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/cl-irc/src
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems
for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/cl-irc/src;
done;
install -m 644 cl-irc.asd %{buildroot}%{_datadir}/common-lisp/source/cl-irc;
cd %{buildroot}%{_datadir}/common-lisp/source/cl-irc
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/cl-irc/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source cl-irc

%preun
/usr/sbin/unregister-common-lisp-source cl-irc

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README ChangeLog CREDITS doc
%{_datadir}/common-lisp/source/cl-irc
%{_datadir}/common-lisp/systems/cl-irc.asd

%changelog
* Thu Nov  4 2010 Anthony Green <green@moxielogic.com> - 20101006svn-1
- Created.
