Name:           python-pycocotools
Version:        2.0.7
Release:        2%{?dist}
# Fill in the actual package summary to submit package to Fedora
Summary:        Official APIs for the MS-COCO dataset

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause-Views AND MIT
URL:            https://github.com/ppwwyyxx/cocoapi
Source:         %{pypi_source pycocotools}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pycocotools' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pycocotools
Summary:        %{summary}

%description -n python3-pycocotools %_description


%prep
%autosetup -p1 -n pycocotools-%{version}
# Use sed to swap out the oldest-supported-numpy magic package for numpy
sed -i "s/oldest-supported-//" pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files pycocotools


%check
%pyproject_check_import


%files -n python3-pycocotools -f %{pyproject_files}


%changelog
%autochangelog
