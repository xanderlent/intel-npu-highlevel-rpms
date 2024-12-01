Name:           python-sphinxcontrib-youtube
Version:        1.4.1
Release:        2
# Fill in the actual package summary to submit package to Fedora
Summary:        Sphinx "youtube" extension.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/sphinx-contrib/youtube
Source:         %{pypi_source sphinxcontrib_youtube}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinxcontrib-youtube' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-sphinxcontrib-youtube
Summary:        %{summary}

%description -n python3-sphinxcontrib-youtube %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-sphinxcontrib-youtube dev,doc,test


%prep
%autosetup -p1 -n sphinxcontrib_youtube-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,doc,test


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files sphinxcontrib


%check
%pyproject_check_import
# We would run the tests here but the official source distribution doesn't actually include them.
#{py3_test_envvars} #{python3} -m nox -s test

%files -n python3-sphinxcontrib-youtube -f %{pyproject_files}


%changelog
%autochangelog
