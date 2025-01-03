Name:           python-tokenizers
Version:        0.20.3
Release:        1%{?dist}
# Fill in the actual package summary to submit package to Fedora
Summary:        ...

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/huggingface/tokenizers
Source:         %{pypi_source tokenizers}

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  cargo-rpm-macros >= 24


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tokenizers' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-tokenizers
Summary:        %{summary}

%description -n python3-tokenizers %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-tokenizers docs


%prep
%autosetup -p1 -n tokenizers-%{version}
%cargo_prep
# Remove locked versions
rm bindings/python/Cargo.lock
# Try using newer ndarray
sed -i -e "s/ndarray = \"0.15\"/ndarray = \"0.16\"/" bindings/python/Cargo.toml


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs
cd bindings/python
%cargo_generate_buildrequires
cd ../..

%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files tokenizers


%check
%pyproject_check_import


%files -n python3-tokenizers -f %{pyproject_files}


%changelog
%autochangelog
