#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTML-Clean
Version  : 1.4
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/A/AZ/AZJADFTRE/HTML-Clean-1.4.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AZ/AZJADFTRE/HTML-Clean-1.4.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhtml-clean-perl/libhtml-clean-perl_0.8-12.debian.tar.xz
Summary  : HTML::Clean - Cleans up HTML code for web browsers, not humans
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTML-Clean-bin = %{version}-%{release}
Requires: perl-HTML-Clean-license = %{version}-%{release}
Requires: perl-HTML-Clean-man = %{version}-%{release}
Requires: perl-HTML-Clean-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
HTML::Clean - Cleans up HTML code for web browsers, not humans
-------------------------------------------------------------------

%package bin
Summary: bin components for the perl-HTML-Clean package.
Group: Binaries
Requires: perl-HTML-Clean-license = %{version}-%{release}

%description bin
bin components for the perl-HTML-Clean package.


%package dev
Summary: dev components for the perl-HTML-Clean package.
Group: Development
Requires: perl-HTML-Clean-bin = %{version}-%{release}
Provides: perl-HTML-Clean-devel = %{version}-%{release}
Requires: perl-HTML-Clean = %{version}-%{release}

%description dev
dev components for the perl-HTML-Clean package.


%package license
Summary: license components for the perl-HTML-Clean package.
Group: Default

%description license
license components for the perl-HTML-Clean package.


%package man
Summary: man components for the perl-HTML-Clean package.
Group: Default

%description man
man components for the perl-HTML-Clean package.


%package perl
Summary: perl components for the perl-HTML-Clean package.
Group: Default
Requires: perl-HTML-Clean = %{version}-%{release}

%description perl
perl components for the perl-HTML-Clean package.


%prep
%setup -q -n HTML-Clean-1.4
cd %{_builddir}
tar xf %{_sourcedir}/libhtml-clean-perl_0.8-12.debian.tar.xz
cd %{_builddir}/HTML-Clean-1.4
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/HTML-Clean-1.4/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTML-Clean
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-HTML-Clean/d6471ff660cd7bcc0346ce3ef130ec74d834008d
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/htmlclean

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTML::Clean.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTML-Clean/d6471ff660cd7bcc0346ce3ef130ec74d834008d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/htmlclean.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/HTML/Clean.pm
/usr/lib/perl5/vendor_perl/5.34.0/auto/HTML/Clean/autosplit.ix
