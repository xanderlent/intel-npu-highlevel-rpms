Name:           python-tokenizers
Version:        0.21.4
Release:        4%{?dist}
Summary:        Implementation of today's most used tokenizers

SourceLicense:  Apache-2.0
# Generated license info from Rust dependencies
# 
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# Apache-2.0 AND MIT
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 OR MIT OR Zlib
# BSD-2-Clause
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
%define license_expression %{shrink:
Unicode-DFS-2016 AND
Apache-2.0 AND
(Apache-2.0 OR BSL-1.0) AND
(Apache-2.0 OR MIT OR Zlib) AND
BSD-2-Clause AND
MIT AND
(Unlicense OR MIT)
}
License:	%{license_expression}
URL:            https://github.com/huggingface/tokenizers
Source:         %{pypi_source tokenizers}

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:	tomcli
BuildRequires:  python3dist(pytest)
# TODO: For some reason the generated buildrequires don't catch this?
BuildRequires:	crate(tempfile/default)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
Provides an implementation of today's most used tokenizers,
with a focus on performance and versatility.
Bindings over the rust-tokenizers implementation.}

%description %_description

%package -n     python3-tokenizers
Summary:        %{summary}

%description -n python3-tokenizers %_description


%prep
%autosetup -p1 -n tokenizers-%{version}
%cargo_prep
# Copy out LICENSE
cp -a tokenizers/LICENSE LICENSE
# Remove vendored tokenizers
rm -r tokenizers/
# Remove locked versions
rm bindings/python/Cargo.lock
# Replace the path-based dependency on the bundled crate with an exact-version
# dependency.
tomcli set bindings/python/Cargo.toml del dependencies.tokenizers.path
tomcli set bindings/python/Cargo.toml str dependencies.tokenizers.version '=%{version}'
# Drop tests that depend on python3dist(datasets)
rm bindings/python/tests/documentation/test_tutorial_train_from_iterators.py

%generate_buildrequires
# Get the cargo buildrequires first, so that maturin will succeed
cd bindings/python/
%cargo_generate_buildrequires
cd ../../
%pyproject_buildrequires

%build
# Generate the dependency license file first, so maturin will find it
cd bindings/python/
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
cd ../../
%pyproject_wheel

%install
%pyproject_install
# When saving the files, assert that a license file was found
%pyproject_save_files -l tokenizers

%check
%pyproject_check_import
cd bindings/python
# TODO: The cargo tests for the bindings fail to link to Python
#cargo_test
# only run the tests, not the benches
%pytest -s -v ./tests/
cd ../../


%files -n python3-tokenizers -f %{pyproject_files}
%doc bindings/python/README.md bindings/python/CHANGELOG.md

%changelog
%autochangelog
