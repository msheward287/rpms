# $Id$
# Authority: dries
# Upstream: Francis J, Lacoste <frajulac$contre,com>

%define real_name Net-IPv4Addr
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Perl extension for manipulating IPv4 addresses
Name: perl-Net-IPv4Addr
Version: 0.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-IPv4Addr/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/F/FR/FRAJULAC/Net-IPv4Addr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This package contains a Perl extension for manipulating IPv4 addresses.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%{_mandir}/man?/*
%{_bindir}/ipv4calc
%{perl_vendorlib}/Net/IPv4Addr.pm
%{perl_vendorlib}/auto/Net

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
