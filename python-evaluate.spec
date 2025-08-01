Name:           python-evaluate
Version:        0.4.5
Release:        1%{?dist}
Summary:        HuggingFace community-driven open-source library of evaluation

License:        Apache-2.0
URL:            https://github.com/huggingface/evaluate
Source:         %{pypi_source evaluate}

BuildArch:      noarch
BuildRequires:  python3-devel
# To import the CLI module we need cookiecutter.
BuildRequires:	python3dist(cookiecutter)
# To import some other files in the test phase
BuildRequires:	python3dist(matplotlib)
# We also need cookiecutter at runtime to use the CLI
# Probably should submit dep bug upstream.
Requires:	python3dist(cookiecutter)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'evaluate' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-evaluate
Summary:        %{summary}

%description -n python3-evaluate %_description

%pyproject_extras_subpkg -n python3-evaluate evaluator,torch


%prep
%autosetup -p1 -n evaluate-%{version}


%generate_buildrequires
%pyproject_buildrequires -x evaluator,torch


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l evaluate


%check
%pyproject_check_import


%files -n python3-evaluate -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/evaluate-cli


%changelog
%autochangelog
