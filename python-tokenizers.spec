Name:           python-tokenizers
Version:        0.21.1
Release:        2%{?dist}
# Fill in the actual package summary to submit package to Fedora
Summary:        Implementation of today's most used tokenizers, with a focus on performances and versatility

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
# The Python code is Apache-2.0
SourceLicense:  Apache-2.0
# Generated license info from Rust dependencies
#
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:	((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (BSD-2-Clause) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT) AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
URL:            https://github.com/huggingface/tokenizers
Source:         %{pypi_source tokenizers}
Patch:		pytokenizers.patch

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  cargo-rpm-macros >= 24
# For some reason the generated buildrequires don't catch this?
BuildRequires:	crate(tempfile/default)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tokenizers' generated automatically by pyp2spec.}

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

%generate_buildrequires
# Get the cargo buildrequires first, so that maturin will succeed
cd bindings/python/
%cargo_generate_buildrequires
cd ../../
%pyproject_buildrequires

%build
%pyproject_wheel
cd bindings/python/
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
cd ../../

%install
%pyproject_install
%pyproject_save_files tokenizers

%check
%pyproject_check_import


%files -n python3-tokenizers -f %{pyproject_files}
%license LICENSE bindings/python/LICENSE.dependencies
%doc bindings/python/README.md bindings/python/CHANGELOG.md

%changelog
%autochangelog
