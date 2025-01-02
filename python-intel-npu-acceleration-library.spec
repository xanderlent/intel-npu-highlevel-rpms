Name:           python-intel-npu-acceleration-library
Version:        1.4.0
Release:        1
# Fill in the actual package summary to submit package to Fedora
Summary:        Intel® NPU Acceleration Library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/intel/intel-npu-acceleration-library
Source:         %{pypi_source intel_npu_acceleration_library}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'intel-npu-acceleration-library' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-intel-npu-acceleration-library
Summary:        %{summary}

%description -n python3-intel-npu-acceleration-library %_description


%prep
%autosetup -p1 -n intel_npu_acceleration_library-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l ...


%check
%pyproject_check_import


%files -n python3-intel-npu-acceleration-library -f %{pyproject_files}


%changelog
%autochangelog