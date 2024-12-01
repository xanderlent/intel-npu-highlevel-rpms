Name:           python-sphinx-togglebutton
Version:        0.3.2
Release:        2
# Fill in the actual package summary to submit package to Fedora
Summary:        Toggle page content and collapse admonitions in Sphinx.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/executablebooks/sphinx-togglebutton
Source:         %{pypi_source sphinx-togglebutton}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinx-togglebutton' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-sphinx-togglebutton
Summary:        %{summary}

%description -n python3-sphinx-togglebutton %_description


%prep
%autosetup -p1 -n sphinx-togglebutton-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l sphinx_togglebutton


%check
%pyproject_check_import
# We would use tox to check the package, but the sources do not include the tests
# That doesn't prevent tox from succeeding, so I guess keep running it?
%tox


%files -n python3-sphinx-togglebutton -f %{pyproject_files}


%changelog
%autochangelog
