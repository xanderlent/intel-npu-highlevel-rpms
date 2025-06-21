Name:           python-accelerate
Version:        1.8.1
Release:        1%{?dist}
Summary:        Accelerate PyTorch with distributed training and inference

License:        Apache-2.0
URL:            https://github.com/huggingface/accelerate
Source:         %{pypi_source accelerate}

BuildArch:      noarch
BuildRequires:  python3-devel
# For passing the test imports
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(parameterized)

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
# This test would cause a circular dependency on python3dist(transformers)
rm tests/test_big_modeling.py


%generate_buildrequires
%pyproject_buildrequires -x rich


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l accelerate


%check
export ACCELERATE_ENABLE_RICH=True
%pyproject_check_import
unset ACCELERATE_ENABLE_RICH
# Upstream source uses make to run tests, but they don't ship the Makefile to PyPI so...
# Lots of test fails. TODO: Skip all the failing tests?
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
