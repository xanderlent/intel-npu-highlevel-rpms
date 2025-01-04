Name:           python-ablog
Version:        0.11.8
Release:        3%{?dist}
# Fill in the actual package summary to submit package to Fedora
Summary:        A Sphinx extension that converts any documentation or personal website project into a full-fledged blog.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://ablog.readthedocs.io/
Source:         %{pypi_source ablog}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ablog' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-ablog
Summary:        %{summary}

%description -n python3-ablog %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-ablog all,dev,docs,markdown,notebook,tests


%prep
%autosetup -p1 -n ablog-%{version}
# Skip the tests that use the Makefile that use git to remove specific files
sed -i -e "s/make tests//g" tox.ini


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,dev,docs,markdown,notebook,tests -t


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l ablog


%check
%pyproject_check_import
%tox


%files -n python3-ablog -f %{pyproject_files}
%{_bindir}/ablog


%changelog
%autochangelog
