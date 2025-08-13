Name:           python-datasets
Version:        4.0.0
Release:        2%{?dist}
Summary:        HuggingFace community-driven open-source library of datasets

License:        Apache-2.0
URL:            https://github.com/huggingface/datasets
Source:         %{pypi_source datasets}

BuildArch:      noarch
BuildRequires:  python3-devel
# Test requires
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-datadir)
BuildRequires:  python3dist(pytest-xdist)


%global _description %{expand:
Datasets is a lightweight library providing two main features:
- one-line dataloaders for many public datasets
- efficient data pre-processing}

%description %_description

%package -n     python3-datasets
Summary:        %{summary}

%description -n python3-datasets %_description

# Extras not packaged
# - audio: Missing torchcodec package.
# - jax: Missing jax and jaxlib packages.
# - pdf: Missing pdfplumber package.
# - streaming: Legacy extra, no deps, can package if needed.
# - tensorflow: Missing tensorflow package.
# - tensorflow_gpu: Missing tensorflow package.
# - benchmarks, dev, docs, quality, tests, tests-numpy2:
#     Development tools, no need to package.
%pyproject_extras_subpkg -n python3-datasets torch,vision


%prep
%autosetup -p1 -n datasets-%{version}
# The project pins dill and multiprocess due to concerns about determinism.
# Relax dill version bound to allow latest upstream
sed -i "s/dill>=0.3.0,<0.3.9/dill>=0.3.0/" setup.py
# Relax multiprocess version bound to allow the latest version
sed -i "s/multiprocess<0.70.17/multiprocess/" setup.py
# Relax fsspec version because Fedora ships a newer version
sed -i "s/fsspec\[http\]>=2023.1.0,<=2025.3.0/fsspec\[http\]>=2023.1.0/" setup.py
# Remove modules that use unpackaged dependencies
# This file relies on pyspark
rm src/datasets/io/spark.py
# Remove tests with unmet deps
# TODO: enable more of these
rm tests/test_arrow_dataset.py
rm tests/test_arrow_reader.py
rm tests/test_arrow_writer.py
rm tests/test_builder.py
rm tests/test_dataset_dict.py
rm tests/test_distributed.py
rm tests/test_extract.py
rm tests/test_file_utils.py
rm tests/test_filesystem.py
rm tests/test_fingerprint.py
rm tests/test_formatting.py
rm tests/test_iterable_dataset.py
rm tests/test_load.py
rm tests/test_offline_util.py
rm tests/test_parallel.py
rm tests/test_patching.py
rm tests/test_py_utils.py
rm tests/test_search.py
rm tests/test_streaming_download_manager.py
rm tests/test_table.py
rm tests/test_upstream_hub.py


%generate_buildrequires
%pyproject_buildrequires -x torch,vision


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l datasets


%check
%pyproject_check_import
# Run the tests like the upstream Makefile does
# The two deselected groups are (a) doesn't work in fedora, (b) doesn't work in mock without internet
%pytest -s -v ./tests/ \
        --deselect="tests/test_dataset_list.py::DatasetListTest::test_create" \
        --deselect="tests/test_dataset_list.py::DatasetListTest::test_create_empty" \
        --deselect="tests/test_dataset_list.py::DatasetListTest::test_list_dict_equivalent" \
        --deselect="tests/test_dataset_list.py::DatasetListTest::test_uneven_records" \
        --deselect="tests/test_dataset_list.py::DatasetListTest::test_variable_list_records" \
        --deselect="tests/test_download_manager.py::test_iter_archive_path[tar_jsonl_path]" \
        --deselect="tests/test_download_manager.py::test_iter_archive_path[zip_jsonl_path]" \
        --deselect="tests/test_download_manager.py::test_iter_archive_file[tar_nested_jsonl_path]" \
        --deselect="tests/test_download_manager.py::test_iter_archive_file[zip_nested_jsonl_path]" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_info[rajpurkar/squad-plain_text-expected_splits0]" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_info[dalle-mini/wit-default-expected_splits1]" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_info[paws-labeled_final-expected_splits2]" \
        --deselect="tests/test_inspect.py::test_get_dataset_info[rajpurkar/squad-expected_configs0-expected_splits_in_first_config0]" \
        --deselect="tests/test_inspect.py::test_get_dataset_info[dalle-mini/wit-expected_configs1-expected_splits_in_first_config1]" \
        --deselect="tests/test_inspect.py::test_get_dataset_info[paws-expected_configs2-expected_splits_in_first_config2]" \
        --deselect="tests/test_inspect.py::test_get_dataset_split_names[rajpurkar/squad-plain_text-expected_splits0]" \
        --deselect="tests/test_inspect.py::test_get_dataset_split_names[dalle-mini/wit-default-expected_splits1]" \
        --deselect="tests/test_inspect.py::test_get_dataset_split_names[paws-labeled_final-expected_splits2]" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository[*]" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository[**]" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository[**/*]" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository[*.txt]" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository[data/*]" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository[**/*.txt]" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository[**/train.txt]" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository_with_base_path[**-4-None]" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository_with_base_path[**-4-data]" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository_with_base_path[**-2-data/subdir]" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository_with_base_path[**-0-data/subdir2]" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository_with_extensions[**-4-extensions0]" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository_with_extensions[**-4-None]" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository_with_extensions[**-0-extensions2]" \
        --deselect="tests/test_data_files.py::test_fail_resolve_pattern_in_dataset_repository" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository_returns_hidden_file_only_if_requested" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository_hidden_base_path" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository_returns_hidden_dir_only_if_requested" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository_returns_special_dir_only_if_requested" \
        --deselect="tests/test_data_files.py::test_resolve_pattern_in_dataset_repository_special_base_path" \
        --deselect="tests/test_data_files.py::test_DataFilesList_from_patterns_in_dataset_repository_[*]" \
        --deselect="tests/test_data_files.py::test_DataFilesList_from_patterns_in_dataset_repository_[**]" \
        --deselect="tests/test_data_files.py::test_DataFilesList_from_patterns_in_dataset_repository_[**/*]" \
        --deselect="tests/test_data_files.py::test_DataFilesList_from_patterns_in_dataset_repository_[*.txt]" \
        --deselect="tests/test_data_files.py::test_DataFilesList_from_patterns_in_dataset_repository_[data/*]" \
        --deselect="tests/test_data_files.py::test_DataFilesList_from_patterns_in_dataset_repository_[**/*.txt]" \
        --deselect="tests/test_data_files.py::test_DataFilesList_from_patterns_in_dataset_repository_[**/train.txt]" \
        --deselect="tests/test_data_files.py::test_DataFilesList_from_patterns_locally_with_extra_files" \
        --deselect="tests/test_data_files.py::test_DataFilesDict_from_patterns_in_dataset_repository[*]" \
        --deselect="tests/test_data_files.py::test_DataFilesDict_from_patterns_in_dataset_repository[**]" \
        --deselect="tests/test_data_files.py::test_DataFilesDict_from_patterns_in_dataset_repository[**/*]" \
        --deselect="tests/test_data_files.py::test_DataFilesDict_from_patterns_in_dataset_repository[*.txt]" \
        --deselect="tests/test_data_files.py::test_DataFilesDict_from_patterns_in_dataset_repository[data/*]" \
        --deselect="tests/test_data_files.py::test_DataFilesDict_from_patterns_in_dataset_repository[**/*.txt]" \
        --deselect="tests/test_data_files.py::test_DataFilesDict_from_patterns_in_dataset_repository[**/train.txt]" \
        --deselect="tests/test_data_files.py::test_DataFilesDict_from_patterns_in_dataset_repository_with_base_path[**-4-None-train]" \
        --deselect="tests/test_data_files.py::test_DataFilesDict_from_patterns_in_dataset_repository_with_base_path[**-4-data-train]" \
        --deselect="tests/test_data_files.py::test_DataFilesDict_from_patterns_in_dataset_repository_with_base_path[**-2-data/subdir-train]" \
        --deselect="tests/test_data_files.py::test_DataFilesDict_from_patterns_in_dataset_repository_with_base_path[**-0-data/subdir2-train]" \
        --deselect="tests/test_data_files.py::test_DataFilesDict_from_patterns_in_dataset_repository_hashing" \
        --deselect="tests/test_data_files.py::test_DataFilesDict_from_patterns_locally_or_remote_hashing" \
        --deselect="tests/test_data_files.py::test_DataFilesPatternsList" \
        --deselect="tests/test_data_files.py::test_DataFilesPatternsDict" \
        --deselect="tests/test_download_manager.py::test_download_manager_download[str]" \
        --deselect="tests/test_download_manager.py::test_download_manager_download[list]" \
        --deselect="tests/test_download_manager.py::test_download_manager_download[dict]" \
        --deselect="tests/test_download_manager.py::test_download_manager_download[dict_of_dict]" \
        --deselect="tests/test_download_manager.py::test_download_manager_extract[False-str]" \
        --deselect="tests/test_download_manager.py::test_download_manager_extract[False-list]" \
        --deselect="tests/test_download_manager.py::test_download_manager_extract[False-dict]" \
        --deselect="tests/test_download_manager.py::test_download_manager_extract[True-str]" \
        --deselect="tests/test_download_manager.py::test_download_manager_extract[True-list]" \
        --deselect="tests/test_download_manager.py::test_download_manager_extract[True-dict]" \
        --deselect="tests/test_download_manager.py::test_download_manager_delete_extracted_files" \
        --deselect="tests/test_download_manager.py::test_iter_files" \
        --deselect="tests/test_hub.py::test_delete_from_hub" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_info_private" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_info_raises[paws-None-ValueError]" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_info_raises[hf-internal-testing/non-existing-dataset-default-DatasetNotFoundError]" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_info_raises[hf-internal-testing/gated_dataset_with_data_files-default-DatasetNotFoundError0]" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_info_raises[hf-internal-testing/private_dataset_with_data_files-default-DatasetNotFoundError0]" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_info_raises[hf-internal-testing/gated_dataset_with_data_files-default-DatasetNotFoundError1]" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_info_raises[hf-internal-testing/private_dataset_with_data_files-default-DatasetNotFoundError1]" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_names[amirveyseh/acronym_identification-expected0]" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_names[rajpurkar/squad-expected1]" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_names[dalle-mini/wit-expected2]" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_names[hf-internal-testing/librispeech_asr_dummy-expected3]" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_names[hf-internal-testing/audiofolder_no_configs_in_metadata-expected4]" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_names[hf-internal-testing/audiofolder_single_config_in_metadata-expected5]" \
        --deselect="tests/test_inspect.py::test_get_dataset_config_names[hf-internal-testing/audiofolder_two_configs_in_metadata-expected6]" \
        --deselect="tests/test_inspect.py::test_get_dataset_default_config_name[amirveyseh/acronym_identification-default]" \
        --deselect="tests/test_inspect.py::test_get_dataset_default_config_name[rajpurkar/squad-plain_text]" \
        --deselect="tests/test_inspect.py::test_get_dataset_default_config_name[dalle-mini/wit-default]" \
        --deselect="tests/test_inspect.py::test_get_dataset_default_config_name[hf-internal-testing/librispeech_asr_dummy-clean]" \
        --deselect="tests/test_inspect.py::test_get_dataset_default_config_name[hf-internal-testing/audiofolder_no_configs_in_metadata-default]" \
        --deselect="tests/test_inspect.py::test_get_dataset_default_config_name[hf-internal-testing/audiofolder_single_config_in_metadata-custom]" \
        --deselect="tests/test_inspect.py::test_get_dataset_default_config_name[hf-internal-testing/audiofolder_two_configs_in_metadata-None]" \
        --deselect="tests/test_inspect.py::test_get_dataset_split_names_error[paws-None-ValueError]"


%files -n python3-datasets -f %{pyproject_files}
%license LICENSE AUTHORS
%doc README.md
%{_bindir}/datasets-cli


%changelog
%autochangelog
