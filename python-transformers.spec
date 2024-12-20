Name:           python-transformers
Version:        4.46.3
Release:        1
# Fill in the actual package summary to submit package to Fedora
Summary:        State-of-the-art Machine Learning for JAX, PyTorch and TensorFlow

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/huggingface/transformers
Source:         %{pypi_source transformers}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'transformers' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-transformers
Summary:        %{summary}

%description -n python3-transformers %_description


%prep
%autosetup -p1 -n transformers-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l ...


%check
%pyproject_check_import


%files -n python3-transformers -f %{pyproject_files}


%changelog
%autochangelog
