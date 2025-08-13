Name:           python-tokenizers
Version:        0.21.4
Release:        5%{?dist}
Summary:        Implementation of today's most used tokenizers

SourceLicense:  Apache-2.0
# Generated license info from Rust dependencies
# 
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# Apache-2.0 AND MIT
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 OR MIT OR Zlib
# BSD-2-Clause
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
%define license_expression %{shrink:
Unicode-DFS-2016 AND
Apache-2.0 AND
(Apache-2.0 OR BSL-1.0) AND
(Apache-2.0 OR MIT OR Zlib) AND
BSD-2-Clause AND
MIT AND
(Unlicense OR MIT)
}
License:	%{license_expression}
URL:            https://github.com/huggingface/tokenizers
Source:         %{pypi_source tokenizers}

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:	tomcli
# TODO: For some reason the generated buildrequires don't catch this?
BuildRequires:	crate(tempfile/default)
# For tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
Provides an implementation of today's most used tokenizers,
with a focus on performance and versatility.
Bindings over the rust-tokenizers implementation.}

%description %_description

%package -n     python3-tokenizers
Summary:        %{summary}

%description -n python3-tokenizers %_description


%prep
%autosetup -p1 -n tokenizers-%{version}
%cargo_prep
# Copy out LICENSE
cp -a tokenizers/LICENSE LICENSE
# Remove vendored tokenizers
rm -r tokenizers/
# Remove locked versions
rm bindings/python/Cargo.lock
# Replace the path-based dependency on the bundled crate with an exact-version
# dependency.
tomcli set bindings/python/Cargo.toml del dependencies.tokenizers.path
tomcli set bindings/python/Cargo.toml str dependencies.tokenizers.version '=%{version}'
# Drop tests that depend on python3dist(datasets)
rm bindings/python/tests/documentation/test_tutorial_train_from_iterators.py

%generate_buildrequires
# Get the cargo buildrequires first, so that maturin will succeed
cd bindings/python/
%cargo_generate_buildrequires
cd ../../
%pyproject_buildrequires

%build
# Generate the dependency license file first, so maturin will find it
cd bindings/python/
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
cd ../../
%pyproject_wheel

%install
%pyproject_install
# When saving the files, assert that a license file was found
%pyproject_save_files -l tokenizers

%check
%pyproject_check_import
cd bindings/python
# TODO: The cargo tests for the bindings fail to link to Python
#cargo_test
# only run the tests, not the benches
%pytest -s -v ./tests/ \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_char_to_token" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_char_to_word" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_invalid_truncate_direction" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_n_sequences" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_sequence_ids" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_token_to_chars" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_token_to_sequence" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_token_to_word" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_truncation" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_word_to_chars" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_word_to_tokens" \
        --deselect="tests/bindings/test_models.py::TestBPE::test_instantiate" \
        --deselect="tests/bindings/test_models.py::TestWordLevel::test_instantiate" \
        --deselect="tests/bindings/test_processors.py::TestByteLevelProcessing::test_processing" \
        --deselect="tests/bindings/test_tokenizer.py::TestTokenizer::test_encode_add_special_tokens" \
        --deselect="tests/bindings/test_tokenizer.py::TestTokenizer::test_encode_formats" \
        --deselect="tests/bindings/test_tokenizer.py::TestTokenizer::test_encode_special_tokens" \
        --deselect="tests/bindings/test_tokenizer.py::TestTokenizer::test_from_pretrained" \
        --deselect="tests/bindings/test_tokenizer.py::TestTokenizer::test_from_pretrained_revision" \
        --deselect="tests/bindings/test_tokenizer.py::TestTokenizer::test_splitting" \
        --deselect="tests/bindings/test_trainers.py::TestUnigram::test_continuing_prefix_trainer_mismatch" \
        --deselect="tests/bindings/test_trainers.py::TestUnigram::test_train" \
        --deselect="tests/bindings/test_trainers.py::TestUnigram::test_train_parallelism_with_custom_pretokenizer" \
        --deselect="tests/documentation/test_pipeline.py::TestPipeline::test_bert_example" \
        --deselect="tests/documentation/test_pipeline.py::TestPipeline::test_pipeline" \
        --deselect="tests/documentation/test_quicktour.py::TestQuicktour::test_quicktour" \
        --deselect="tests/implementations/test_bert_wordpiece.py::TestBertWordPieceTokenizer::test_basic_encode" \
        --deselect="tests/implementations/test_bert_wordpiece.py::TestBertWordPieceTokenizer::test_multiprocessing_with_parallelism" \
        --deselect="tests/implementations/test_byte_level_bpe.py::TestByteLevelBPE::test_add_prefix_space" \
        --deselect="tests/implementations/test_byte_level_bpe.py::TestByteLevelBPE::test_basic_encode" \
        --deselect="tests/implementations/test_byte_level_bpe.py::TestByteLevelBPE::test_lowerspace" \
        --deselect="tests/implementations/test_byte_level_bpe.py::TestByteLevelBPE::test_multiprocessing_with_parallelism" \
        --deselect="tests/implementations/test_char_bpe.py::TestCharBPETokenizer::test_basic_encode" \
        --deselect="tests/implementations/test_char_bpe.py::TestCharBPETokenizer::test_decoding" \
        --deselect="tests/implementations/test_char_bpe.py::TestCharBPETokenizer::test_lowercase" \
        --deselect="tests/implementations/test_char_bpe.py::TestCharBPETokenizer::test_multiprocessing_with_parallelism" \
        --deselect="tests/test_serialization.py::TestSerialization::test_full_serialization_albert" \
        --deselect="tests/test_serialization.py::TestSerialization::test_str_big"
cd ../../


%files -n python3-tokenizers -f %{pyproject_files}
%doc bindings/python/README.md bindings/python/CHANGELOG.md

%changelog
%autochangelog
