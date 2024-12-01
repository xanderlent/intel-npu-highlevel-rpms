Name:           python-sphinx-thebe
Version:        0.3.1
Release:        2
# Fill in the actual package summary to submit package to Fedora
Summary:        Integrate interactive code blocks into your documentation with Thebe and Binder.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/executablebooks/sphinx-thebe
Source:         %{pypi_source sphinx_thebe}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinx-thebe' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-sphinx-thebe
Summary:        %{summary}

%description -n python3-sphinx-thebe %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-sphinx-thebe dev,testing


%prep
%autosetup -p1 -n sphinx_thebe-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,testing -t


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l sphinx_thebe


%check
%pyproject_check_import
# Tox runs but doesn't seem to test anything in the current environment
%tox



%files -n python3-sphinx-thebe -f %{pyproject_files}


%changelog
%autochangelog
