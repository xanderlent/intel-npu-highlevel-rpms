Name:           python-optimum
Version:        1.27.0
Release:        2%{?dist}
# Fill in the actual package summary to submit package to Fedora
Summary:        Optimum Library is an extension of the Hugging Face Transformers library, providing a framework to integrate third-party libraries from Hardware Partners and interface with their specific functionality.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/huggingface/optimum
Source:         %{pypi_source optimum}

BuildArch:      noarch
BuildRequires:  python3-devel
# Import test requirements
BuildRequires:  python3dist(accelerate)
BuildRequires:  python3dist(datasets)
BuildRequires:  python3dist(onnx)
BuildRequires:  python3dist(optuna)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(torchaudio)
BuildRequires:  python3dist(torchvision)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'optimum' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-optimum
Summary:        %{summary}

%description -n python3-optimum %_description


%prep
%autosetup -p1 -n optimum-%{version}
# BetterTransformer is deprecated and needs an older version of Transformers than we package
rm -r optimum/bettertransformer/
# modeling_diffusion fails the import test because it needs python3dist(diffusers)
rm optimum/onnxruntime/modeling_diffusion.py
# We don't support onnxruntime right now, and it fails the import test
rm -r optimum/onnxruntime/
rm -r optimum/pipelines/
# the runs stuff also fails the import test
rm optimum/runs_base.py
rm optimum/utils/runs.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l optimum


%check
%pyproject_check_import


%files -n python3-optimum -f %{pyproject_files}
%{_bindir}/optimum-cli


%changelog
%autochangelog
