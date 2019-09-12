%global debug_package %{nil}
%global gh_user starship

Name:           starship
Version:        0.17.0
Release:        1%{?dist}
Summary:        The cross-shell prompt for astronauts
Group:          Applications/System
License:        GPLv2
URL:            https://github.com/%{gh_user}/%{name}
BuildRequires:  cmake, libgit2, openssl-devel
%{?el7:BuildRequires: cargo, rust}

%description
Starship is the minimal, blazing fast, and extremely customizable prompt for any shell!
The prompt shows information you need while you're working, while staying sleek and out of the way.


%prep
wget https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
tar xzf v%{version}.tar.gz


%build
cd %{name}-%{version}
cargo build --release


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp %{name}-%{version}/target/release/%{name} %{buildroot}/usr/bin/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc %{name}-%{version}/LICENSE* %{name}-%{version}/*.md
/usr/bin/%{name}


%changelog
* Fri Sep 13 2019 Jamie Curnow <jc@jc21.com> - 0.17.0-1
- v0.17.0

* Mon Sep 9 2019 Jamie Curnow <jc@jc21.com> - 0.16.0-1
- Initial spec
