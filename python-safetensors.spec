Name:           python-safetensors
Version:        0.4.1
Release:        1
# Fill in the actual package summary to submit package to Fedora
Summary:        ...

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/huggingface/safetensors
Source:         %{pypi_source safetensors}

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  cargo-rpm-macros >= 24
# TODO: Shouldn't this use the existing rust-safetensors library in Fedora?


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'safetensors' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-safetensors
Summary:        %{summary}

%description -n python3-safetensors %_description


%prep
%autosetup -p1 -n safetensors-%{version}
%cargo_prep
# Remove locked versions
rm bindings/python/Cargo.lock

%generate_buildrequires
%pyproject_buildrequires
cd bindings/python
%cargo_generate_buildrequires
cd ../..


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files safetensors


%check
# TODO: Fails on trying to import jax
%pyproject_check_import


%files -n python3-safetensors -f %{pyproject_files}


%changelog
%autochangelog
