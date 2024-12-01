Name:           python-sphinx-book-theme
Version:        1.1.3
Release:        2
# Fill in the actual package summary to submit package to Fedora
Summary:        A clean book theme for scientific explanations and documentation with Sphinx

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://pypi.org/project/sphinx-book-theme/
Source:         %{pypi_source sphinx_book_theme}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinx-book-theme' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-sphinx-book-theme
Summary:        %{summary}

%description -n python3-sphinx-book-theme %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-sphinx-book-theme code-style,doc,test


%prep
%autosetup -p1 -n sphinx_book_theme-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x code-style,doc,test


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files sphinx_book_theme


%check
%pyproject_check_import
# Tox runs but doesn't seem to test anything in the current environment
%tox


%files -n python3-sphinx-book-theme -f %{pyproject_files}


%changelog
%autochangelog
