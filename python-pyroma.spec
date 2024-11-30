Name:           python-pyroma
Version:        4.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Test your project's packaging friendliness

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/regebro/pyroma
Source:         %{pypi_source pyroma}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyroma' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pyroma
Summary:        %{summary}

%description -n python3-pyroma %_description


%prep
%autosetup -p1 -n pyroma-%{version}
# TODO: Hack to prevent packaging the tests in a later step
rm -rf pyroma/testdata
rm pyroma/tests.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l pyroma


%check
%pyproject_check_import


%files -n python3-pyroma -f %{pyproject_files}
# TODO: Should the package be pyroma or provide pyroma the binary to make using dnf easier?
%{_bindir}/pyroma


%changelog
%autochangelog
