#
# Conditional build:
%bcond_with	cvsup		# checkout from cvs instead of using source0
#
Summary:	GnuPG keys for PLD Linux developers
Name:		pld-keyring
Version:	2008.02.23
Release:	1
# The keys in the keyrings don't fall under any copyright
License:	?
Group:		Applications/Text
URL:		http://cvs.pld-linux.org/cgi-bin/cvsweb.cgi/PGP-keys/
BuildArch:	noarch
Source0:	%{name}.tar.bz2
# Source0-md5:	18069b419fe40075bda5b1b59d6c3efd
%{?with_cvsup:BuildRequires:	cvs}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define     _cvsroot    :pserver:cvs@cvs.pld-linux.org:/cvsroot
%define     _cvsmodule  PGP-keys

%description
GnuPG keys for PLD Linux developers.

%prep
%if %{with cvsup}
%setup -q -c -T
cd ..
cvs -d %{_cvsroot} co -d %{name} %{_cvsmodule}
tar cjf %{SOURCE0} %{name}
cd -
%else
%setup -q -n %{name}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a . $RPM_BUILD_ROOT%{_datadir}/%{name}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/CVS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/%{name}
