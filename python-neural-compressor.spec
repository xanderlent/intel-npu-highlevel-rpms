Name:           python-neural-compressor
Version:        3.4.1
Release:        3%{?dist}
Summary:        Intel® Neural Compressor

License:        Apache-2.0
URL:            https://github.com/intel/neural-compressor
Source:         %{pypi_source neural_compressor}
%define commit_hash 5b8acf3a0be1b938bfbfbbd1f188ad675eaad445
Source:		https://raw.githubusercontent.com/intel/neural-compressor/%{commit_hash}/requirements.txt
Source:		https://raw.githubusercontent.com/intel/neural-compressor/%{commit_hash}/requirements_pt.txt
Source:		https://raw.githubusercontent.com/intel/neural-compressor/%{commit_hash}/requirements_tf.txt

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  git-core
# Dependencies for successful import tests (though optional at runtime?)
BuildRequires:  python3dist(datasets)
BuildRequires:  python3dist(evaluate)
BuildRequires:  python3dist(nltk)
BuildRequires:  python3dist(onnx)
BuildRequires:  python3dist(onnxruntime)



# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'neural-compressor' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-neural-compressor
Summary:        %{summary}

%description -n python3-neural-compressor %_description

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
sed -i -e "s/numpy<2.0/numpy/" neural_compressor.egg-info/requires.txt
sed -i -e "s/numpy<2.0/numpy/" neural_compressor.egg-info/PKG-INFO
sed -i -e "s/numpy<2.0/numpy/" PKG-INFO
sed -i -e "s/numpy<2.0/numpy/" requirements_pt.txt
# We also need to substitute the PyPI name for a special reduced opencv with
# the full opencv that is packaged by Fedora
sed -i -e "s/opencv-python-headless/opencv/" neural_compressor.egg-info/requires.txt
sed -i -e "s/opencv-python-headless/opencv/" neural_compressor.egg-info/PKG-INFO
sed -i -e "s/opencv-python-headless/opencv/" PKG-INFO
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
# needs lm_eval
rm neural_compressor/evaluation/lm_eval/accuracy.py
rm neural_compressor/evaluation/lm_eval/models/huggingface.py
rm neural_compressor/evaluation/lm_eval/__init__.py
rm neural_compressor/evaluation/lm_eval/models/__init__.py
# needs habana_frameworks
rm neural_compressor/torch/algorithms/fp8_quant/_quant_common/quant_config.py
# fallout of the above
rm neural_compressor/torch/algorithms/fp8_quant/common.py
rm neural_compressor/torch/algorithms/fp8_quant/__init__.py
rm neural_compressor/torch/algorithms/fp8_quant/observer.py
rm neural_compressor/torch/algorithms/fp8_quant/patched_module_base.py
# needs habana_frameworks
rm neural_compressor/torch/algorithms/fp8_quant/_core/measure.py
# fallout of the above
rm neural_compressor/torch/algorithms/fp8_quant/prepare_quant/prepare_model.py
rm neural_compressor/torch/algorithms/fp8_quant/quantizer.py
rm neural_compressor/torch/algorithms/fp8_quant/save_load.py
# needs habana_frameworks
rm neural_compressor/torch/algorithms/mixed_low_precision/custom_methods/gptq.py
# breaks on PyTorch 2.8 as shipped in rawhide/F43
%if 0%{?fedora} >= 43
rm neural_compressor/adaptor/torch_utils/hawq_metric.py
rm neural_compressor/torch/algorithms/pt2e_quant/core.py
rm neural_compressor/torch/algorithms/pt2e_quant/__init__.py
rm neural_compressor/torch/algorithms/pt2e_quant/half_precision_rewriter.py
rm neural_compressor/torch/algorithms/pt2e_quant/utility.py
rm neural_compressor/torch/export/pt2e_export.py
rm neural_compressor/torch/export/__init__.py
%endif
# needs ipex (intel_extensions_for_pytorch)
rm neural_compressor/torch/algorithms/smooth_quant/__init__.py
rm neural_compressor/torch/algorithms/smooth_quant/save_load.py
rm neural_compressor/torch/algorithms/smooth_quant/smooth_quant.py
rm neural_compressor/torch/algorithms/smooth_quant/utility.py
rm neural_compressor/torch/algorithms/static_quant/static_quant.py
rm neural_compressor/torch/algorithms/static_quant/__init__.py
rm neural_compressor/torch/algorithms/static_quant/save_load.py
# needs auto_round
rm neural_compressor/torch/algorithms/weight_only/autoround.py
# needs numba
rm neural_compressor/torch/utils/bit_packer.py


%generate_buildrequires
%pyproject_buildrequires -x pt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l neural_compressor


%check
%pyproject_check_import


%files -n python3-neural-compressor -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/incbench


%changelog
%autochangelog
