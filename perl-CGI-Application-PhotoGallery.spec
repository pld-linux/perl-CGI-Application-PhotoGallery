
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define pnam	Application-PhotoGallery
Summary:	GGI::Application::PhotoGallery
Name:		perl-CGI-Application-PhotoGallery
Version:	0.02
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	72309a8e1721a0f8f45f6e96b1fc167a
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl(CGI::Application)
BuildRequires:	perl(HTML::Template)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:make test}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/CGI/Application/PhotoGallery.pm
%dir %{perl_vendorlib}/CGI/Application/PhotoGallery
%{perl_vendorlib}/CGI/Application/PhotoGallery/*.pm
%{perl_vendorlib}/CGI/Application/PhotoGallery/*.tmpl
%{_mandir}/man3/*
