%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	CipherSaber
Summary:	Crypt::CipherSaber Perl module - interface to CipherSaber 1 and 2 encryptions
Summary(pl):	Modu³ Perla Crypt::CipherSaber - interfejs do szyfrów CipherSaber 1 i 2
Name:		perl-Crypt-CipherSaber
Version:	0.61
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::CipherSaber is a Perl module providing an object oriented
interface to CipherSaber-1 and CipherSaber-2 encryption.

%description -l pl
Crypt::CipherSaber to modu³ Perla daj±cy obiektowo zorientowany
interfejs do szyfrów CipherSaber-1 i CipherSaber-2.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Crypt/CipherSaber.pm
%{_mandir}/man3/*
