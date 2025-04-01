Name:           python-datasets
Version:        3.5.0
Release:        2%{?dist}
# Fill in the actual package summary to submit package to Fedora
Summary:        HuggingFace community-driven open-source library of datasets

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/huggingface/datasets
Source:         %{pypi_source datasets}

BuildArch:      noarch
BuildRequires:  python3-devel


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
# Relax dill version bound a little (to allow the latest version)
sed -i "s/dill>=0.3.0,<0.3.9/dill>=0.3.0,<0.3.10/" setup.py
# Relax multiprocess version bound a little (to allow the latest version)
sed -i "s/multiprocess<0.70.17/multiprocess<0.70.18/" setup.py
%if 0%{?fedora} == 40
# Relax requests version bound a little (to allow an older version on F40)
# This bound is because upstream is worried about CVEs in requests.
sed -i "s/requests>=2.32.2/requests>=2.31.0/" setup.py
%endif
# Remove modules that use unpackaged dependencies
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


%files -n python3-datasets -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/datasets-cli


%changelog
%autochangelog
