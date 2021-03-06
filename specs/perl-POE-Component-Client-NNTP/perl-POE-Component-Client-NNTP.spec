# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-NNTP

Summary: POE component that implements an RFC 977 NNTP client
Name: perl-POE-Component-Client-NNTP
Version: 2.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-NNTP/

Source: http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/POE-Component-Client-NNTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(POE) >= 0.9999
BuildRequires: perl(POE::Component::Pluggable) >= 0.03
BuildRequires: perl(POE::Component::Pluggable::Constants)
BuildRequires: perl(POE::Driver::SysRW)
BuildRequires: perl(POE::Filter::Line)
BuildRequires: perl(POE::Wheel::ReadWrite)
BuildRequires: perl(POE::Wheel::SocketFactory)
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Test::POE::Server::TCP)
BuildRequires: perl >= 5.6.0
Requires: perl(POE) >= 0.9999
Requires: perl(POE::Component::Pluggable) >= 0.03
Requires: perl(POE::Component::Pluggable::Constants)
Requires: perl(POE::Driver::SysRW)
Requires: perl(POE::Filter::Line)
Requires: perl(POE::Wheel::ReadWrite)
Requires: perl(POE::Wheel::SocketFactory)
Requires: perl >= 5.6.0

%filter_from_requires /^perl*/d
%filter_setup

%description
A component that provides access to NNTP.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/POE::Component::Client::NNTP.3pm*
%doc %{_mandir}/man3/POE::Component::Client::NNTP::*.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Client/
%{perl_vendorlib}/POE/Component/Client/NNTP/
%{perl_vendorlib}/POE/Component/Client/NNTP.pm

%changelog
* Wed Dec 23 2009 Christoph Maser <cmr@financial.com> - 2.14-1
- Updated to version 2.14.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 2.12-1
- Updated to version 2.12.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 2.06-1
- Updated to release 2.06.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 2.04-1
- Updated to release 2.04.

* Thu Jul 5 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.02-1
- Updated to latest upstream version { old source not available }

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 2.01-1
- Updated to release 2.01.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
