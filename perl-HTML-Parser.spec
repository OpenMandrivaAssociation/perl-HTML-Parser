%define	upstream_name	 HTML-Parser
%define upstream_version 3.66

%define Werror_cflags %nil

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary: 	Perl module to parse HTML documents
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url: 		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-HTML-Tagset
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}
Requires: 	perl-HTML-Tagset >= 3.30.0

%description
HTML::Parser module for Perl to parse and extract information from
HTML documents.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
