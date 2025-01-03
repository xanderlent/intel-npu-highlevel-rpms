Name:           python-safetensors
Version:        0.4.3
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
# Actually, this package seems to recomplile that one...
# Because the python package is really bindings to the rust package?
# TODO: Maybe these bindings belong with the rust package upstream?
Provides:	bundled(crate(safetensors)) = %version


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'safetensors' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-safetensors
Summary:        %{summary}

%description -n python3-safetensors %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-safetensors numpy,torch


%prep
%autosetup -p1 -n safetensors-%{version}
%cargo_prep
# Remove locked versions
rm bindings/python/Cargo.lock
# flax needs jax, not built, so remove it (avoid failing the import test for unpackaged stuff)
rm py_src/safetensors/flax.py
# paddle needs paddlepaddle, so remove it to pass the import test
rm py_src/safetensors/paddle.py
# tensorflow needs tensorflow, so remove it to pass the import test
rm py_src/safetensors/tensorflow.py
# mlx needs mlx, so remove it to pass the import test
rm py_src/safetensors/mlx.py

%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x numpy,torch
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
%pyproject_check_import


%files -n python3-safetensors -f %{pyproject_files}


%changelog
%autochangelog
