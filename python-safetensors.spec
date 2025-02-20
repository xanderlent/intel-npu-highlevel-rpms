Name:           python-safetensors
Version:        0.5.2
Release:        2%{?dist}
# Fill in the actual package summary to submit package to Fedora
Summary:        ...

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
SourceLicense:        Apache-2.0
# Results of the Cargo License Check
# 
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:	Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
URL:            https://github.com/huggingface/safetensors
Source:         %{pypi_source safetensors}
Patch:		pysafetensors.patch

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  cargo-rpm-macros >= 24

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
# Copy over LICENSE file
cp -a safetensors/LICENSE LICENSE
# Delete the bundled crate
rm -r safetensors/
# Remove locked versions
rm bindings/python/Cargo.lock
# flax needs jax, not built, so remove it to pass the import test
rm py_src/safetensors/flax.py
# paddle needs paddlepaddle, so remove it to pass the import test
rm py_src/safetensors/paddle.py
# tensorflow needs tensorflow, so remove it to pass the import test
rm py_src/safetensors/tensorflow.py
# mlx needs mlx, so remove it to pass the import test
rm py_src/safetensors/mlx.py

%generate_buildrequires
# Get the cargo buildrequires first, so that maturin will succeed
cd bindings/python/
%cargo_generate_buildrequires
cd ../../
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x numpy,torch

%build
%pyproject_wheel
cd bindings/python/
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
cd ../../


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files safetensors


%check
%pyproject_check_import


%files -n python3-safetensors -f %{pyproject_files}
%license LICENSE bindings/python/LICENSE.dependencies
%doc bindings/python/README.md


%changelog
%autochangelog
