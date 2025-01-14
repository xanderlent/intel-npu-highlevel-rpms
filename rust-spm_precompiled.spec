# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate spm_precompiled

Name:           rust-spm_precompiled
Version:        0.1.4
Release:        1%{?dist}
Summary:        Aims to emulate https://github.com/google/sentencepiece Dart::DoubleArray struct and it's Normalizer

License:        Apache-2.0
URL:            https://crates.io/crates/spm_precompiled
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
This crate aims to emulate https://github.com/google/sentencepiece
Dart::DoubleArray struct and it's Normalizer.  This crate is highly
specialized and not intended for general use.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 02 2025 Alexander F. Lent <lx@xanderlent.com> - 0.1.4-1
- Initial package
