%global debug_package %{nil}
%global gh_user starship

Name:           starship
Version:        0.48.0
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
* Mon Jan 4 2021 Jamie Curnow <jc@jc21.com> - 0.48.0-1
- v0.48.0

* Mon Nov 16 2020 Jamie Curnow <jc@jc21.com> - 0.47.0-1
- v0.47.0

* Thu Oct 15 2020 Jamie Curnow <jc@jc21.com> - 0.46.2-1
- v0.46.2

* Fri Oct 9 2020 Jamie Curnow <jc@jc21.com> - 0.46.0-1
- v0.46.0

* Thu Oct 1 2020 Jamie Curnow <jc@jc21.com> - 0.45.1-1
- v0.45.1

* Wed Sep 30 2020 Jamie Curnow <jc@jc21.com> - 0.45.0-1
- v0.45.0

* Tue Jul 7 2020 Jamie Curnow <jc@jc21.com> - 0.44.0-1
- v0.44.0

* Mon Jun 26 2020 Jamie Curnow <jc@jc21.com> - 0.43.0-1
- v0.43.0

* Tue Jun 10 2020 Jamie Curnow <jc@jc21.com> - 0.42.0-1
- v0.42.0

* Mon May 18 2020 Jamie Curnow <jc@jc21.com> - 0.41.3-1
- v0.41.3

* Fri May 15 2020 Jamie Curnow <jc@jc21.com> - 0.41.1-1
- v0.41.1

* Wed Apr 29 2020 Jamie Curnow <jc@jc21.com> - 0.41.0-1
- v0.41.0

* Tue Apr 14 2020 Jamie Curnow <jc@jc21.com> - 0.40.1-1
- v0.40.1

* Tue Apr 7 2020 Jamie Curnow <jc@jc21.com> - 0.39.0-1
- v0.39.0

* Tue Mar 24 2020 Jamie Curnow <jc@jc21.com> - 0.38.1-1
- v0.38.1

* Fri Mar 20 2020 Jamie Curnow <jc@jc21.com> - 0.38.0-1
- v0.38.0

* Mon Mar 2 2020 Jamie Curnow <jc@jc21.com> - 0.37.0-1
- v0.37.0

* Thu Feb 20 2020 Jamie Curnow <jc@jc21.com> - 0.36.1-1
- v0.36.1

* Thu Feb 13 2020 Jamie Curnow <jc@jc21.com> - 0.36.0-1
- v0.36.0

* Fri Feb 7 2020 Jamie Curnow <jc@jc21.com> - 0.35.1-1
- v0.35.1

* Tue Feb 4 2020 Jamie Curnow <jc@jc21.com> - 0.34.1-1
- v0.34.1

* Fri Jan 17 2020 Jamie Curnow <jc@jc21.com> - 0.33.1-1
- v0.33.1

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
