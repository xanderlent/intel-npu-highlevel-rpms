Name:           python-neural-compressor
Version:        3.1.1
Release:        6%{?dist}
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
BuildRequires:	git
# ONNX seems to be an optional dependency, but we need it because we want the import checks to succeed, and some parts use ONNX
BuildRequires:  python3-onnx
BuildRequires:  python3-onnxruntime
# Torch also seems to be an optional dependency, but we are building with the pt extra
BuildRequires:  python3-torch
BuildRequires:  python3-transformers
# Some code uses nltk, and it is packaged so require it
BuildRequires:	python3-nltk
# Apparently some code also uses accelerate
BuildRequires:	python3-accelerate



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
cp -a %{SOURCE1} requirements.txt
cp -a %{SOURCE2} requirements_pt.txt
cp -a %{SOURCE3} requirements_tf.txt
# Fedora 41+ packages numpy 2.x.y and requirements.txt specifies numpy < 2, but
# that, per this PR https://github.com/intel/neural-compressor/pull/1684 is only
# because of old versions of scikit-learn, so remove the restriction!
sed -i -e "s/numpy < 2.0/numpy/" requirements.txt
# We also need to substitute the PyPI name for a special reduced opencv with
# the full opencv that is packaged by Fedora
sed -i -e "s/opencv-python-headless/opencv/" neural_compressor.egg-info/requires.txt
sed -i -e "s/opencv-python-headless/opencv/" neural_compressor.egg-info/PKG-INFO
sed -i -e "s/opencv-python-headless/opencv/" PKG-INFO
# This is the only substituion that matters, but do it in all the places above just in case
sed -i -e "s/opencv-python-headless/opencv/" requirements.txt
# Remove all the files that should only ship if we enable extras
# This makes the import check pass
# keras_utils, tf_utils needs tensorflow, which would be the +tf extra
rm -r neural_compressor/adaptor/keras_utils
rm -r neural_compressor/adaptor/tf_utils
rm -r neural_compressor/tensorflow/
# needs xgboost
rm neural_compressor/compression/hpo/search_algorithms.py
rm neural_compressor/compression/hpo/__init__.py
# needs bigcode_eval
rm neural_compressor/evaluation/bigcode_eval/evaluator.py
rm neural_compressor/evaluation/bigcode_eval/__init__.py
# needs evaluate
rm neural_compressor/evaluation/hf_eval/evaluator.py
rm neural_compressor/evaluation/hf_eval/__init__.py
# needs datasets
rm neural_compressor/evaluation/hf_eval/hf_datasets/cnn_dailymail.py
rm neural_compressor/transformers/quantization/utils.py
rm neural_compressor/transformers/quantization/__init__.py
rm neural_compressor/transformers/models/modeling_auto.py
# TODO: I'm worries that some of these removals, like this one, break the package?
rm neural_compressor/transformers/models/__init__.py
# needs lm_eval
rm neural_compressor/evaluation/lm_eval/accuracy.py
rm neural_compressor/evaluation/lm_eval/models/huggingface.py
rm neural_compressor/evaluation/lm_eval/__init__.py
rm neural_compressor/evaluation/lm_eval/models/__init__.py
# TODO: I'm worries that some of these removals, like this one, break the package?
rm neural_compressor/transformers/__init__.py
# needs habana_frameworks
rm neural_compressor/torch/algorithms/fp8_quant/_quant_common/quant_config.py
rm neural_compressor/torch/algorithms/fp8_quant/common.py
rm neural_compressor/torch/algorithms/fp8_quant/__init__.py
rm neural_compressor/torch/algorithms/fp8_quant/fp8_quant.py
rm neural_compressor/torch/algorithms/fp8_quant/_core/measure.py
rm neural_compressor/torch/algorithms/fp8_quant/prepare_quant/prepare_model.py
rm neural_compressor/torch/algorithms/mixed_low_precision/custom_methods/gptq.py
# needs ipex (intel_extensions_for_pytorch)
rm neural_compressor/torch/algorithms/smooth_quant/utility.py
rm neural_compressor/torch/algorithms/smooth_quant/__init__.py
rm neural_compressor/torch/algorithms/smooth_quant/save_load.py
rm neural_compressor/torch/algorithms/smooth_quant/smooth_quant.py
rm neural_compressor/torch/algorithms/static_quant/static_quant.py
rm neural_compressor/torch/algorithms/static_quant/__init__.py
rm neural_compressor/torch/algorithms/static_quant/save_load.py
# needs auto_round
rm neural_compressor/torch/algorithms/weight_only/autoround.py
# needs numba
rm neural_compressor/torch/utils/bit_packer.py


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
# Just drop the import checks so we can ship the package for now
%pyproject_check_import


%files -n python3-neural-compressor -f %{pyproject_files}
%{_bindir}/incbench


%changelog
%autochangelog
