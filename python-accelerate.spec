Name:           python-accelerate
Version:        1.6.0
Release:        1%{?dist}
Summary:        Accelerate PyTorch with distributed training and inference

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/huggingface/accelerate
Source:         %{pypi_source accelerate}

BuildArch:      noarch
BuildRequires:  python3-devel
# For passing the test imports
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(rich)

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
Accelerate is a library that enables the same PyTorch code to be run across any
distributed configuration by adding just four lines of code! In short, training
and inference at scale made simple, efficient and adaptable.}


%description %_description

%package -n     python3-accelerate
Summary:        %{summary}

%description -n python3-accelerate %_description

%pyproject_extras_subpkg -n python3-accelerate rich


%prep
%autosetup -p1 -n accelerate-%{version}
# Delete all the test_utils with external deps (they fail the import test)
rm -r src/accelerate/test_utils/scripts/external_deps/*
# Delete a test that would create a circular dep on python3dist(transformers)
#rm tests/test_big_modeling.py
# On Fedora 40, this eventually imports torch._C which doesn't work
%if 0%{?fedora} < 41
rm src/accelerate/test_utils/scripts/test_merge_weights.py
%endif


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x rich


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l accelerate


%check
export ACCELERATE_ENABLE_RICH=True
%pyproject_check_import
unset ACCELERATE_ENABLE_RICH
# Upstream source uses make to run tests, but they don't ship the Makefile to PyPI so...
# TODO: Skip all the failing tests?
#pytest


%files -n python3-accelerate -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/accelerate
%{_bindir}/accelerate-config
%{_bindir}/accelerate-estimate-memory
%{_bindir}/accelerate-launch
%{_bindir}/accelerate-merge-weights


%changelog
%autochangelog
