Name:           python-sphinx-examples
Version:        0.0.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A lightweight example directive to make it easy to demonstrate code / results.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://executablebooks.org/
Source:         %{pypi_source sphinx-examples}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinx-examples' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-sphinx-examples
Summary:        %{summary}

%description -n python3-sphinx-examples %_description


%prep
%autosetup -p1 -n sphinx-examples-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files sphinx_examples


%check
%pyproject_check_import


%files -n python3-sphinx-examples -f %{pyproject_files}


%changelog
%autochangelog
