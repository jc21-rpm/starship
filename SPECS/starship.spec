%global debug_package %{nil}
%global gh_user starship

Name:           starship
Version:        0.33.0
Release:        1%{?dist}
Summary:        The cross-shell prompt for astronauts
Group:          Applications/System
License:        GPLv2
URL:            https://github.com/%{gh_user}/%{name}
BuildRequires:  cmake, libgit2, openssl-devel
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
%{?el7:BuildRequires: cargo, rust}

%description
Starship is the minimal, blazing fast, and extremely customizable prompt for any shell!
The prompt shows information you need while you're working, while staying sleek and out of the way.


%prep
%setup -q -n %{name}-%{version}

%build
cargo build --release


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp target/release/%{name} %{buildroot}/usr/bin/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE* *.md
/usr/bin/%{name}


%changelog
* Tue Jan 7 2020 Jamie Curnow <jc@jc21.com> - 0.33.0-1
- v0.33.0

* Sun Dec 29 2019 Jamie Curnow <jc@jc21.com> - 0.32.2-1
- v0.32.2

* Thu Dec 26 2019 Jamie Curnow <jc@jc21.com> - 0.32.1-1
- v0.32.1

* Fri Dec 20 2019 Jamie Curnow <jc@jc21.com> - 0.31.0-1
- v0.31.0

* Sat Dec 14 2019 Jamie Curnow <jc@jc21.com> - 0.30.1-1
- v0.30.1

* Thu Dec 12 2019 Jamie Curnow <jc@jc21.com> - 0.29.0-1
- v0.29.0

* Mon Dec 9 2019 Jamie Curnow <jc@jc21.com> - 0.28.0-1
- v0.28.0

* Wed Dec 4 2019 Jamie Curnow <jc@jc21.com> - 0.27.0-1
- v0.27.0

* Mon Dec 2 2019 Jamie Curnow <jc@jc21.com> - 0.26.5-1
- v0.26.5

* Wed Nov 13 2019 Jamie Curnow <jc@jc21.com> - 0.26.4-1
- v0.26.4

* Wed Nov 13 2019 Jamie Curnow <jc@jc21.com> - 0.26.3-1
- v0.26.3

* Mon Nov 4 2019 Jamie Curnow <jc@jc21.com> - 0.26.2-1
- v0.26.2

* Mon Oct 21 2019 Jamie Curnow <jc@jc21.com> - 0.25.2-1
- v0.25.2

* Mon Oct 21 2019 Jamie Curnow <jc@jc21.com> - 0.25.1-1
- v0.25.1

* Wed Oct 16 2019 Jamie Curnow <jc@jc21.com> - 0.25.0-1
- v0.25.0

* Tue Oct 15 2019 Jamie Curnow <jc@jc21.com> - 0.24.0-1
- v0.24.0

* Mon Oct 14 2019 Jamie Curnow <jc@jc21.com> - 0.23.0-1
- v0.23.0

* Wed Oct 9 2019 Jamie Curnow <jc@jc21.com> - 0.22.0-1
- v0.22.0

* Mon Oct 7 2019 Jamie Curnow <jc@jc21.com> - 0.21.0-1
- v0.21.0

* Thu Sep 26 2019 Jamie Curnow <jc@jc21.com> - 0.19.0-1
- v0.19.0

* Sat Sep 21 2019 Jamie Curnow <jc@jc21.com> - 0.18.0-1
- v0.18.0

* Fri Sep 13 2019 Jamie Curnow <jc@jc21.com> - 0.17.0-1
- v0.17.0

* Mon Sep 9 2019 Jamie Curnow <jc@jc21.com> - 0.16.0-1
- Initial spec
