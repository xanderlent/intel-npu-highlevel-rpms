Name:           python-accelerate
Version:        1.2.1
Release:        1%{?dist}
# Fill in the actual package summary to submit package to Fedora
Summary:        Accelerate

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/huggingface/accelerate
Source:         %{pypi_source accelerate}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'accelerate' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-accelerate
Summary:        %{summary}

%description -n python3-accelerate %_description


%prep
%autosetup -p1 -n accelerate-%{version}


%generate_buildrequires
%pyproject_buildrequires
# Delete all the test_utils with external deps
rm -r src/accelerate/test_utils/scripts/external_deps
# This particular utility tries to access something internal to pytorch?
rm src/accelerate/test_utils/scripts/test_merge_weights.py
# This particular utility uses pytest, but we don't package the test extras...
rm src/accelerate/test_utils/scripts/test_notebook.py
# The rich extra doesn't like system packages, insisting you use pip, so don't bother with it...
rm src/accelerate/utils/rich.py


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l accelerate


%check
%pyproject_check_import


%files -n python3-accelerate -f %{pyproject_files}
%{_bindir}/accelerate
%{_bindir}/accelerate-config
%{_bindir}/accelerate-estimate-memory
%{_bindir}/accelerate-launch
%{_bindir}/accelerate-merge-weights



%changelog
%autochangelog
