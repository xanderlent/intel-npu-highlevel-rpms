Name:           python-accelerate
Version:        1.10.0
Release:        3%{?dist}
Summary:        Accelerate PyTorch with distributed training and inference

License:        Apache-2.0
URL:            https://github.com/huggingface/accelerate
Source:         %{pypi_source accelerate}

BuildArch:      noarch
BuildRequires:  python3-devel
# For passing the import test
# For passing the test suites
BuildRequires:	python3dist(parameterized)
BuildRequires:	python3dist(pytest)
#BuildRequires:	python3dist(pytest-order) # Not packaged
BuildRequires:	python3dist(pytest-subtests)
BuildRequires:	python3dist(pytest-xdist)

%global _description %{expand:
Accelerate is a library that enables the same PyTorch code to be run across any
distributed configuration by adding just four lines of code! In short, training
and inference at scale made simple, efficient and adaptable.}


%description %_description

%package -n     python3-accelerate
Summary:        %{summary}

%description -n python3-accelerate %_description

# Extras not packaged:
# - deepspeed: Missing deepspeed package in Fedora
# - sagemaker: Missing sagemaker package in Fedora
%pyproject_extras_subpkg -n python3-accelerate rich


%prep
%autosetup -p1 -n accelerate-%{version}
# Delete all the test_utils with external deps (they fail the import test)
rm -r src/accelerate/test_utils/scripts/external_deps/*
# This test would cause a circular dependency on python3dist(transformers)
rm tests/test_big_modeling.py


%generate_buildrequires
%pyproject_buildrequires -x rich


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l accelerate


%check
export ACCELERATE_ENABLE_RICH=True
%pyproject_check_import
unset ACCELERATE_ENABLE_RICH
# Upstream source uses make to run tests, but they don't ship the Makefile to PyPI so...
# we manually copy the test cases we can use from the upstream Makefile.
# Upstream's test_core suite
%pytest -s -v ./tests/ \
	--ignore=./tests/test_big_modeling.py \
	--ignore=./tests/test_modeling_utils.py \
	--ignore=./tests/test_examples.py \
	--ignore=./tests/test_cli.py \
	--ignore=./tests/deepspeed \
	--ignore=./tests/fsdp \
	--ignore=./tests/tp \
        --deselect="tests/test_accelerator.py::AcceleratorTester::test_can_unwrap_distributed_compiled_model_keep_torch_compile" \
        --deselect="tests/test_accelerator.py::AcceleratorTester::test_can_unwrap_distributed_compiled_model_remove_torch_compile" \
        --deselect="tests/test_utils.py::UtilsTester::test_convert_to_fp32" \
        --deselect="tests/test_utils.py::UtilsTester::test_dynamo_extract_model_keep_torch_compile" \
        --deselect="tests/test_utils.py::UtilsTester::test_dynamo_extract_model_remove_torch_compile" \
        --deselect="tests/test_utils.py::UtilsTester::test_send_to_device_compiles" \
        --deselect="tests/test_cpu.py::MultiCPUTester::test_cpu" \
        --deselect="tests/test_cpu.py::MultiCPUTester::test_ops" \
        --deselect="tests/test_grad_sync.py::SyncScheduler::test_gradient_sync_cpu_multi" \
        --deselect="tests/test_grad_sync.py::SyncScheduler::test_gradient_sync_cpu_noop" \
        --deselect="tests/test_scheduler.py::SchedulerTester::test_lambda_scheduler_not_step_with_optimizer_multiprocess" \
        --deselect="tests/test_scheduler.py::SchedulerTester::test_lambda_scheduler_not_step_with_optimizer_single_process" \
        --deselect="tests/test_scheduler.py::SchedulerTester::test_lambda_scheduler_steps_with_optimizer_multiprocess" \
        --deselect="tests/test_scheduler.py::SchedulerTester::test_lambda_scheduler_steps_with_optimizer_single_process" \
        --deselect="tests/test_scheduler.py::SchedulerTester::test_one_cycle_scheduler_not_step_with_optimizer_multiprocess" \
        --deselect="tests/test_scheduler.py::SchedulerTester::test_one_cycle_scheduler_not_step_with_optimizer_single_process" \
        --deselect="tests/test_scheduler.py::SchedulerTester::test_one_cycle_scheduler_steps_with_optimizer_multiprocess" \
        --deselect="tests/test_scheduler.py::SchedulerTester::test_one_cycle_scheduler_steps_with_optimizer_single_process" \
        --deselect="tests/test_utils.py::UtilsTester::test_patch_environment_key_exists"
# Note that we deselected tests where either
# - PyTorch dynamo was not available
# - multiprocess gives an error inside PyTorch
# - In the enivronment test, it fails if AA BB or CC is defined. Seriously?
# Upstream's test_cli
%pytest -s -v ./tests/test_cli.py \
        --deselect="tests/test_cli.py::AccelerateLauncherTester::test_invalid_keys" \
        --deselect="tests/test_cli.py::AccelerateLauncherTester::test_mpi_multicpu_config_cmd" \
        --deselect="tests/test_cli.py::AccelerateLauncherTester::test_validate_launch_command" \
        --deselect="tests/test_cli.py::ClusterConfigTester::test_sagemaker_config" \
        --deselect="tests/test_cli.py::TpuConfigTester::test_accelerate_install" \
        --deselect="tests/test_cli.py::TpuConfigTester::test_accelerate_install_version" \
        --deselect="tests/test_cli.py::TpuConfigTester::test_base_backward_compatibility" \
        --deselect="tests/test_cli.py::TpuConfigTester::test_with_config_file" \
        --deselect="tests/test_cli.py::TpuConfigTester::test_with_config_file_and_command" \
        --deselect="tests/test_cli.py::TpuConfigTester::test_with_config_file_and_command_file" \
        --deselect="tests/test_cli.py::TpuConfigTester::test_with_config_file_and_command_file_backward_compatibility" \
        --deselect="tests/test_cli.py::TpuConfigTester::test_with_config_file_and_multiple_command" \
        --deselect="tests/test_cli.py::ToFSDP2Tester::test_config_already_fsdp2" \
        --deselect="tests/test_cli.py::ToFSDP2Tester::test_fsdp2_config" \
        --deselect="tests/test_cli.py::ToFSDP2Tester::test_fsdp2_overwrite" \
        --deselect="tests/test_cli.py::ToFSDP2Tester::test_no_output_without_overwrite" \
        --deselect="tests/test_cli.py::ModelEstimatorTester::test_gated" \
        --deselect="tests/test_cli.py::ToFSDP2Tester::test_overwrite_when_output_file_exists" \
        --deselect="tests/test_cli.py::ToFSDP2Tester::test_nonexistent_config_file" \
        --deselect="tests/test_cli.py::ModelEstimatorTester::test_no_metadata"
# Note that we deselected tests where:
# - The test config files are missing from the PyPI dist.
# - transformers is a curcular depenededency  test_gates-
# - AttributeError: type object 'ToFSDP2Tester' has no attribute 'original_config`'
# - Internet access is required
# Upstream's test_big_modeling suite
# Not currently supported due to circular dep on python3dist(transformers)
#pytest -s -v ./tests/test_big_modeling.py ./tests/test_modeling_utils.py
# The deepspeed, fsdp, and tp folders under test are missing from the PyPI sources.
# And so are the examples, so we can't test the examples, either.


%files -n python3-accelerate -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/accelerate
%{_bindir}/accelerate-config
%{_bindir}/accelerate-estimate-memory
%{_bindir}/accelerate-launch
%{_bindir}/accelerate-merge-weights


%changelog
%autochangelog
