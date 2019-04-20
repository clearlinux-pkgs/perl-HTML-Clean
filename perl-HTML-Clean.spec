#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTML-Clean
Version  : 0.8
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/L/LI/LINDNER/HTML-Clean-0.8.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LI/LINDNER/HTML-Clean-0.8.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhtml-clean-perl/libhtml-clean-perl_0.8-12.debian.tar.xz
Summary  : Cleans up HTML code for web browsers, not humans
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-HTML-Clean-bin = %{version}-%{release}
Requires: perl-HTML-Clean-license = %{version}-%{release}
Requires: perl-HTML-Clean-man = %{version}-%{release}
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


%prep
%setup -q -n HTML-Clean-0.8
cd ..
%setup -q -T -D -n HTML-Clean-0.8 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/HTML-Clean-0.8/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTML-Clean
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-HTML-Clean/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/HTML/Clean.pm
/usr/lib/perl5/vendor_perl/5.28.2/auto/HTML/Clean/autosplit.ix

%files bin
%defattr(-,root,root,-)
/usr/bin/htmlclean

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTML::Clean.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTML-Clean/deblicense_copyright

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/htmlclean.1
