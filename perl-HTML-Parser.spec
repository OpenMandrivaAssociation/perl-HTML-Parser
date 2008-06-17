%define	module	HTML-Parser

Summary: 	Perl module to parse HTML documents
Name: 		perl-%{module}
Version: 	3.56
Release: 	%mkrel 3
License: 	GPL or Artistic
Group: 		Development/Perl
URL: 		http://search.cpan.org/dist/%{module}/
Source: 	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/HTML/%{module}-%{version}.tar.bz2
Requires: 	perl-HTML-Tagset >= 3.03
BuildRequires:	perl-devel
BuildRequires:	perl-HTML-Tagset
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
HTML::Parser module for Perl to parse and extract information from
HTML documents.

%prep

%setup -q -n %{module}-%{version}

%build
# compile with default options (prompt() checks for STDIN being a terminal).
# yes to not ask for automate rebuild
yes | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO Changes
%{perl_vendorarch}/auto/HTML
%{perl_vendorarch}/HTML
%{_mandir}/*/*


