# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate numpy

Name:           rust-numpy
Version:        0.22.1
Release:        1%{?dist}
Summary:        PyO3-based Rust bindings of the NumPy C-API

License:        BSD-2-Clause
URL:            https://crates.io/crates/numpy
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
# TODO: The test phase requires this, technically not used when building or at runtime...
# ...but all your API calls will fail badly when numpy is missing, so let's just require it.
# Require it at build time so the test phase of the build passes... Sigh.
BuildRequires:  python3-numpy

%global _description %{expand:
PyO3-based Rust bindings of the NumPy C-API.}

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

%package     -n %{name}+gil-refs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gil-refs-devel %{_description}

This package contains library source intended for building other packages which
use the "gil-refs" feature of the "%{crate}" crate.

%files       -n %{name}+gil-refs-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+half-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+half-devel %{_description}

This package contains library source intended for building other packages which
use the "half" feature of the "%{crate}" crate.

%files       -n %{name}+half-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nalgebra-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nalgebra-devel %{_description}

This package contains library source intended for building other packages which
use the "nalgebra" feature of the "%{crate}" crate.

%files       -n %{name}+nalgebra-devel
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
* Thu Jan 02 2025 Alexander F. Lent <lx@xanderlent.com> - 0.22.1-1
- Initial package