Name:           python-neural-compressor
Version:        3.1.1
Release:        1
# Fill in the actual package summary to submit package to Fedora
Summary:        Repository of Intel® Neural Compressor

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/intel/neural-compressor
Source:         %{pypi_source neural_compressor}
Source:         https://raw.githubusercontent.com/intel/neural-compressor/a8cd9aa815ba7a94d9e0b4b028ce99eae22c2940/requirements.txt
Source:		https://raw.githubusercontent.com/intel/neural-compressor/a8cd9aa815ba7a94d9e0b4b028ce99eae22c2940/requirements_pt.txt
Source:		https://raw.githubusercontent.com/intel/neural-compressor/a8cd9aa815ba7a94d9e0b4b028ce99eae22c2940/requirements_tf.txt

BuildArch:      noarch
BuildRequires:  python3-devel
# ONNX seems to be an optional dependency, but we need it because we want the import checks to succeed, and some parts use ONNX
BuildRequires:  python3-onnx
BuildRequires:  python3-onnxruntime
BuildRequires:  python3-torch
BuildRequires:  python3-transformers


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'neural-compressor' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-neural-compressor
Summary:        %{summary}

%description -n python3-neural-compressor %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-neural-compressor pt


%prep
%autosetup -p1 -n neural_compressor-%{version}
cp ../requirements.txt requirements.txt
cp ../requirements_pt.txt requirements_pt.txt
cp ../requirements_tf.txt requirements_tf.txt
sed -i -e "s/opencv-python-headless/opencv/" neural_compressor.egg-info/requires.txt
sed -i -e "s/opencv-python-headless/opencv/" neural_compressor.egg-info/PKG-INFO
sed -i -e "s/opencv-python-headless/opencv/" PKG-INFO
# This is the only substituion that matters, but do it in all the places above just in case
sed -i -e "s/opencv-python-headless/opencv/" requirements.txt
# Remove all the files that should only ship if we enable extras
# This makes the import check pass
# keras_utils, tf_utils needs tensorflow, which would be the +tf extra
rm -rf neural_compressor/adaptor/keras_utils
rm -rf neural_compressor/adaptor/tf_utils


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x pt


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l neural_compressor


%check
%pyproject_check_import


%files -n python3-neural-compressor -f %{pyproject_files}
%{_bindir}/incbench


%changelog
%autochangelog
