Name:           python-datasets
Version:        4.0.0
Release:        1%{?dist}
Summary:        HuggingFace community-driven open-source library of datasets

License:        Apache-2.0
URL:            https://github.com/huggingface/datasets
Source:         %{pypi_source datasets}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
Datasets is a lightweight library providing two main features:
- one-line dataloaders for many public datasets
- efficient data pre-processing}

%description %_description

%package -n     python3-datasets
Summary:        %{summary}

%description -n python3-datasets %_description

# Extras not packaged
# - audio: Missing torchcodec package.
# - jax: Missing jax and jaxlib packages.
# - pdf: Missing pdfplumber package.
# - streaming: Legacy extra, no deps, can package if needed.
# - tensorflow: Missing tensorflow package.
# - tensorflow_gpu: Missing tensorflow package.
# - benchmarks, dev, docs, quality, tests, tests-numpy2:
#     Development tools, no need to package.
%pyproject_extras_subpkg -n python3-datasets torch,vision


%prep
%autosetup -p1 -n datasets-%{version}
# The project pins dill and multiprocess due to concerns about determinism.
# Relax dill version bound to allow latest upstream
sed -i "s/dill>=0.3.0,<0.3.9/dill>=0.3.0/" setup.py
# Relax multiprocess version bound to allow the latest version
sed -i "s/multiprocess<0.70.17/multiprocess/" setup.py
# Relax fsspec version because Fedora ships a newer version
sed -i "s/fsspec\[http\]>=2023.1.0,<=2025.3.0/fsspec\[http\]>=2023.1.0/" setup.py
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
# TODO: run the tests

%files -n python3-datasets -f %{pyproject_files}
%license LICENSE AUTHORS
%doc README.md
%{_bindir}/datasets-cli


%changelog
%autochangelog
