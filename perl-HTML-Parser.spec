%define	modname	HTML-Parser
%define	modver	3.68

%define Werror_cflags %{nil}

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	9

Summary:	Perl module to parse HTML documents
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/HTML/%{modname}-%{modver}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-HTML-Tagset
Requires:	perl-HTML-Tagset >= 3.30.0

%description
HTML::Parser module for Perl to parse and extract information from
HTML documents.

%prep
%setup -q -n %{modname}-%{modver}

%build
# compile with default options (prompt() checks for STDIN being a terminal).
# yes to not ask for automate rebuild
yes | perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc README TODO Changes
%{perl_vendorarch}/auto/HTML
%{perl_vendorarch}/HTML
%{_mandir}/*/*

%changelog
* Fri Dec 21 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.680.0-7
- rebuild for new perl-5.16.2
- cleanups

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 3.680.0-5mdv2012.0
+ Revision: 765304
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 3.680.0-4
+ Revision: 763845
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 3.680.0-3
+ Revision: 763247
- force it
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.680.0-2
+ Revision: 667194
- mass rebuild

* Sat Sep 04 2010 Jérôme Quelin <jquelin@mandriva.org> 3.680.0-1mdv2011.0
+ Revision: 575741
- update to 3.68

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 3.670.0-1mdv2011.0
+ Revision: 572219
- update to 3.67

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 3.660.0-4mdv2011.0
+ Revision: 564519
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.660.0-3mdv2011.0
+ Revision: 555301
- rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for 5.12

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 3.660.0-1mdv2011.0
+ Revision: 552316
- update to 3.66

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 3.650.0-1mdv2010.1
+ Revision: 532148
- update to 3.65

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 3.640.0-3mdv2010.1
+ Revision: 461285
- update to 3.64

* Sun Aug 16 2009 Jérôme Quelin <jquelin@mandriva.org> 3.620.0-3mdv2010.0
+ Revision: 416994
- force rebuild
- update to 3.62

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 3.610.0-2mdv2010.0
+ Revision: 408231
- forgot to bump mkrel
- fix requires:

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 3.610.0-1mdv2010.0
+ Revision: 407755
- rebuild using %%perl_convert_version

* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.61-3mdv2010.0
+ Revision: 396939
- rebuild for properly versioned dependencies

* Fri Jul 17 2009 Olivier Thauvin <nanardon@mandriva.org> 3.61-2mdv2010.0
+ Revision: 396936
- rebuild to fix dependencies

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.61-1mdv2010.0
+ Revision: 387756
- update to new version 3.61

* Mon Feb 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.60-1mdv2009.1
+ Revision: 341080
- new release
- temporarily disable format errors

* Tue Nov 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.59-1mdv2009.1
+ Revision: 306761
- update to new version 3.59

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.58-1mdv2009.1
+ Revision: 305714
- update to new version 3.58

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 3.56-3mdv2009.0
+ Revision: 223787
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 3.56-2mdv2008.1
+ Revision: 151255
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Mar 05 2007 Olivier Thauvin <nanardon@mandriva.org> 3.56-1mdv2007.0
+ Revision: 132943
- 3.56

* Tue Dec 12 2006 Olivier Thauvin <nanardon@mandriva.org> 3.55-1mdv2007.1
+ Revision: 95139
- 3.55

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild
    - Import perl-HTML-Parser

* Tue May 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.54-1mdv2007.0
- New release 3.54
- spec cleanup

* Wed Mar 22 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.51-1mdk
- 3.51

* Fri Feb 17 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.50-1mdk
- 3.50

* Fri Feb 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.49-1mdk
- 3.49

* Tue Dec 06 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.48-1mdk
- 3.48

* Wed Nov 30 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.47-1mdk
- 3.47

* Thu Oct 27 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.46-1mdk
- 3.46

* Fri Jan 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 3.45-1mdk
- 3.45

* Tue Jan 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 3.44-1mdk
- 3.44

* Tue Dec 07 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 3.43-1mdk
- 3.43

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 3.38-1mdk
- 3.38

* Tue Apr 20 2004 Stefan van der Eijk <stefan@eijk.nu> 3.36-1mdk
- 3.36

