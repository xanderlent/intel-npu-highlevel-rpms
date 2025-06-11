Name:           python-datasets
Version:        3.6.0
Release:        1%{?dist}
Summary:        HuggingFace community-driven open-source library of datasets

License:        Apache-2.0
URL:            https://github.com/huggingface/datasets
Source:         %{pypi_source datasets}

BuildArch:      noarch
BuildRequires:  python3-devel
# for tests
BuildRequires:	pytest


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'datasets' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-datasets
Summary:        %{summary}

%description -n python3-datasets %_description

%pyproject_extras_subpkg -n python3-datasets torch,vision


%prep
%autosetup -p1 -n datasets-%{version}
# The project pins dill and multiprocess due to concerns about determinism.
# Our package may, then, exhibit different behavior from upstream.
# Relax dill version bound to allow latest upstream
sed -i "s/dill>=0.3.0,<0.3.9/dill>=0.3.0,<0.5/" setup.py
# Relax multiprocess version bound a little (to allow the latest version)
sed -i "s/multiprocess<0.70.17/multiprocess<0.70.18/" setup.py
# Remove modules that use unpackaged dependencies
# This file relies on pyspark
rm src/datasets/io/spark.py


%generate_buildrequires
%pyproject_buildrequires -x torch,vision


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l datasets


%check
%pyproject_check_import
# Would run pytest macro but I can't figure out how to get it to work...
#pytest


%files -n python3-datasets -f %{pyproject_files}
%license LICENSE AUTHORS
%doc README.md
%{_bindir}/datasets-cli


%changelog
%autochangelog
