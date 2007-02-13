#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Application-PhotoGallery
Summary:	CGI::Application::PhotoGallery - module to provide a simple photo gallery
Summary(pl.UTF-8):	CGI::Application::PhotoGallery - moduł do tworzenia prostych galerii zdjęć
Name:		perl-CGI-Application-PhotoGallery
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	034a51a2ad0f6dc5177376151841e8ad
URL:		http://search.cpan.org/dist/CGI-Application-PhotoGallery/
BuildRequires:	perl-CGI-Application
BuildRequires:	perl-HTML-Template
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Cache-Cache
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-MIME-Types
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Application::PhotoGallery is a CGI::Application module allowing
people to create their own simple photo gallery. There is no need to
generate your own thumbnails since they are created on the fly (using
either the GD or Image::Magick modules).

%description -l pl.UTF-8
CGI::Application::PhotoGallery to moduł CGI::Application umożliwiający
tworzenie własnej prostej galerii zdjęć. Nie ma potrzeby generowania
miniaturek, ponieważ są one tworzone w locie (przy użyciu modułów GD
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
%{_mandir}/man3/*
