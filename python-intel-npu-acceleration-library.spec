Name:           python-intel-npu-acceleration-library
Version:        1.4.0
Release:        5%{?dist}
# Fill in the actual package summary to submit package to Fedora
Summary:        Intel® NPU Acceleration Library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/CK-Force-loading-of-system-OpenVINO-rather-than-bu.patch
License:        Apache-2.0
URL:            https://github.com/intel/intel-npu-acceleration-library
Source:         %{pypi_source intel_npu_acceleration_library}
Patch:		0001-Disable-download-copy-of-OpenVINO-distribution.patch
Patch:		0002-Always-use-system-OpenVINO-rather-than-bundled-one.patch
Patch:		0003-Disable-insecure-rpath-when-using-system-OpenVINO.patch


BuildRequires:	python3-devel
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	lsb_release
BuildRequires:	dos2unix
BuildRequires:	g++
BuildRequires:  openvino-devel
# For import tests
BuildRequires:	openvino
BuildRequires:	python3-openvino
# TODO: Is the following correct?
Requires:	openvino
# TODO: Why isn't this being automatically installed as a depenedency?
Requires:	python3-openvino


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'intel-npu-acceleration-library' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-intel-npu-acceleration-library
Summary:        %{summary}

%description -n python3-intel-npu-acceleration-library %_description


%prep
%autosetup -N -n intel_npu_acceleration_library-%{version}
# Convert the line endings in CMakeLists.txt so the patch applies correctly.
# This seems to be a problem because Intel made the python package tarball on Windows? Sigh.
dos2unix CMakeLists.txt
dos2unix intel_npu_acceleration_library/backend/bindings.py
%autopatch -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l intel_npu_acceleration_library


%check
# Whoops, it thinks libintel_npu_acceleration_library.so is an importable dynamic module since
# it lives in the Python source tree. It is not that, becuase this package is weird.
# Maybe we should move it to the system wide libdir or libexec?
# For now disable the import check and hope nobody tries to import it!
#pyproject_check_import


%files -n python3-intel-npu-acceleration-library -f %{pyproject_files}


%changelog
%autochangelog
