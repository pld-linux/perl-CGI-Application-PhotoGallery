#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define pnam	Application-PhotoGallery
Summary:	CGI::Application::PhotoGallery - module to provide a simple photo gallery
Summary(pl):	CGI::Application::PhotoGallery - modu³ do tworzenia prostych galerii zdjêæ
Name:		perl-CGI-Application-PhotoGallery
Version:	0.02
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	72309a8e1721a0f8f45f6e96b1fc167a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-CGI-Application
BuildRequires:	perl-HTML-Template
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Application::PhotoGallery is a CGI::Application module allowing
people to create their own simple photo gallery. There is no need to
generate your own thumbnails since they are created on the fly (using
either the GD or Image::Magick modules).

%description -l pl
CGI::Application::PhotoGallery to modu³ CGI::Application umo¿liwiaj±cy
tworzenie w³asnej prostej galerii zdjêæ. Nie ma potrzeby generowania
miniaturek, poniewa¿ s± one tworzone w locie (przy u¿yciu modu³ów GD
lub Image::Magick).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/Application/PhotoGallery.pm
%dir %{perl_vendorlib}/CGI/Application/PhotoGallery
%{perl_vendorlib}/CGI/Application/PhotoGallery/*.pm
%{perl_vendorlib}/CGI/Application/PhotoGallery/*.tmpl
%{_mandir}/man3/*
