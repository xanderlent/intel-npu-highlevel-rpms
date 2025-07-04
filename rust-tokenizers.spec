# Generated by rust2rpm 27
%bcond check 0
%global debug_package %{nil}

%global crate tokenizers

Name:           rust-tokenizers
Version:        0.21.1
Release:        3%{?dist}
Summary:        Implementation of today's most used tokenizers, with a focus on performances and versatility

License:        Apache-2.0
URL:            https://crates.io/crates/tokenizers
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
Patch:          tokenizers-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Provides an implementation of today's most used tokenizers, with a focus
on performances and versatility.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
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

%package     -n %{name}+esaxx_fast-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+esaxx_fast-devel %{_description}

This package contains library source intended for building other packages which
use the "esaxx_fast" feature of the "%{crate}" crate.

%files       -n %{name}+esaxx_fast-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fancy-regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fancy-regex-devel %{_description}

This package contains library source intended for building other packages which
use the "fancy-regex" feature of the "%{crate}" crate.

%files       -n %{name}+fancy-regex-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hf-hub-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hf-hub-devel %{_description}

This package contains library source intended for building other packages which
use the "hf-hub" feature of the "%{crate}" crate.

%files       -n %{name}+hf-hub-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http-devel %{_description}

This package contains library source intended for building other packages which
use the "http" feature of the "%{crate}" crate.

%files       -n %{name}+http-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+indicatif-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+indicatif-devel %{_description}

This package contains library source intended for building other packages which
use the "indicatif" feature of the "%{crate}" crate.

%files       -n %{name}+indicatif-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+onig-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+onig-devel %{_description}

This package contains library source intended for building other packages which
use the "onig" feature of the "%{crate}" crate.

%files       -n %{name}+onig-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+progressbar-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+progressbar-devel %{_description}

This package contains library source intended for building other packages which
use the "progressbar" feature of the "%{crate}" crate.

%files       -n %{name}+progressbar-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustls-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustls-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "rustls-tls" feature of the "%{crate}" crate.

%files       -n %{name}+rustls-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable_wasm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable_wasm-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable_wasm" feature of the "%{crate}" crate.

%files       -n %{name}+unstable_wasm-devel
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
%autochangelog
