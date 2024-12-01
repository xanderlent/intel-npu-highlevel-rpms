Name:           python-sphinx-automodapi
Version:        0.15.0
Release:        2
# Fill in the actual package summary to submit package to Fedora
Summary:        Sphinx extension for auto-generating API documentation for entire modules

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/astropy/sphinx-automodapi
Source:         %{pypi_source sphinx-automodapi}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinx-automodapi' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-sphinx-automodapi
Summary:        %{summary}

%description -n python3-sphinx-automodapi %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-sphinx-automodapi test


%prep
%autosetup -p1 -n sphinx-automodapi-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x test -t


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l sphinx_automodapi


%check
%pyproject_check_import
# Skip all tox tests, for now, since they fail in the build environment
#tox


%files -n python3-sphinx-automodapi -f %{pyproject_files}


%changelog
%autochangelog
