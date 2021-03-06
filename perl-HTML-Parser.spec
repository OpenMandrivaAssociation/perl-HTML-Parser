%define Werror_cflags %{nil}
%define	modname	HTML-Parser
%define modver 3.76

Summary:	Perl module to parse HTML documents
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/HTML::Parser
Source0:	http://www.cpan.org/modules/by-module/HTML/HTML-Parser-%{modver}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-HTML-Tagset
# For make test
BuildRequires:	perl(Test::More)
Requires:	perl-HTML-Tagset >= 3.30.0

%description
HTML::Parser module for Perl to parse and extract information from
HTML documents.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
# compile with default options (prompt() checks for STDIN being a terminal).
# yes to not ask for automate rebuild
yes | perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%make test || :

%install
%makeinstall_std

%files
%doc README TODO Changes
%{perl_vendorarch}/auto/HTML
%{perl_vendorarch}/HTML
%{_mandir}/man3/*


