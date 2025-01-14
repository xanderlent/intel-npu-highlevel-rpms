# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate ndarray

Name:           rust-ndarray0.15
Version:        0.15.6
Release:        1%{?dist}
Summary:        N-dimensional array for general elements and for numerics

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ndarray
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
An n-dimensional array for general elements and for numerics.
Lightweight array views and slicing; views support chunking and
splitting.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README-crates.io.md
%doc %{crate_instdir}/README-quick-start.md
%doc %{crate_instdir}/README.rst
%doc %{crate_instdir}/RELEASES.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+approx-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+approx-devel %{_description}

This package contains library source intended for building other packages which
use the "approx" feature of the "%{crate}" crate.

%files       -n %{name}+approx-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+approx-0_5-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+approx-0_5-devel %{_description}

This package contains library source intended for building other packages which
use the "approx-0_5" feature of the "%{crate}" crate.

%files       -n %{name}+approx-0_5-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+blas-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blas-devel %{_description}

This package contains library source intended for building other packages which
use the "blas" feature of the "%{crate}" crate.

%files       -n %{name}+blas-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cblas-sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cblas-sys-devel %{_description}

This package contains library source intended for building other packages which
use the "cblas-sys" feature of the "%{crate}" crate.

%files       -n %{name}+cblas-sys-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+docs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+docs-devel %{_description}

This package contains library source intended for building other packages which
use the "docs" feature of the "%{crate}" crate.

%files       -n %{name}+docs-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+libc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libc-devel %{_description}

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%files       -n %{name}+libc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+matrixmultiply-threading-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+matrixmultiply-threading-devel %{_description}

This package contains library source intended for building other packages which
use the "matrixmultiply-threading" feature of the "%{crate}" crate.

%files       -n %{name}+matrixmultiply-threading-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rayon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rayon-devel %{_description}

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%files       -n %{name}+rayon-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rayon_-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rayon_-devel %{_description}

This package contains library source intended for building other packages which
use the "rayon_" feature of the "%{crate}" crate.

%files       -n %{name}+rayon_-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-1-devel %{_description}

This package contains library source intended for building other packages which
use the "serde-1" feature of the "%{crate}" crate.

%files       -n %{name}+serde-1-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+test-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+test-devel %{_description}

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

%files       -n %{name}+test-devel
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
* Fri Jan 03 2025 Alexander F. Lent <lx@xanderlent.com> - 0.15.6-1
- Initial package
