Name:           python-pycocotools
Version:        2.0.10
Release:        1%{?dist}
Summary:        Official APIs for the MS-COCO dataset

# BSD-2-Clause-Views covers most of the code as the main license.txt file
# common/gason.{cpp,h} are a vendored dependency, and is licensed MIT
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

%pyproject_extras_subpkg -n python3-pycocotools all


%prep
%autosetup -p1 -n pycocotools-%{version}


%generate_buildrequires
%pyproject_buildrequires -x all


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L pycocotools


%check
%pyproject_check_import


%files -n python3-pycocotools -f %{pyproject_files}
# TODO import both licenses


%changelog
%autochangelog
