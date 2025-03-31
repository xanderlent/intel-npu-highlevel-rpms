Name:           python-blobfile
Version:        3.0.0
Release:        1%{?dist}
# Fill in the actual package summary to submit package to Fedora
Summary:        Read GCS, ABS and local paths with the same interface, clone of tensorflow.io.gfile

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Unlicense
URL:            https://github.com/christopher-hesse/blobfile
Source:         %{pypi_source blobfile}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'blobfile' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-blobfile
Summary:        %{summary}

%description -n python3-blobfile %_description


%prep
%autosetup -p1 -n blobfile-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l blobfile


%check
%pyproject_check_import
# We could run tests with python testing/run.py but
# "The tests are rather slow, ~7 minutes to run (even though large file tests are disabled) and require accounts with every cloud provider."


%files -n python3-blobfile -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
