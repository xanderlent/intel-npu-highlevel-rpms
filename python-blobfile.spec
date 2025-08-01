Name:           python-blobfile
Version:        3.0.0
Release:        2%{?dist}
Summary:        Read GCS, ABS and local paths with the same interface

License:        Unlicense
URL:            https://github.com/christopher-hesse/blobfile
Source:         %{pypi_source blobfile}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
This is a library that provides a Python-like interface for reading local and
remote files (only from blob storage), with an API similar to open() as well as
some of the os.path and shutil functions. blobfile supports local paths, Google
Cloud Storage paths (gs://<bucket>), and Azure Blob Storage paths
(az://<account>/<container>
or https://<account>.blob.core.windows.net/<container>/).

The main function is BlobFile, which lets you open local and remote files that
act more or less like local ones. There are also a few additional functions
such as basename, dirname, and join, which mostly do the same thing as their
os.path namesakes, only they also support GCS paths and ABS paths.

This library is inspired by TensorFlow's gfile but does not have exactly the
same interface.
}

%description %_description

%package -n     python3-blobfile
Summary:        %{summary}

%description -n python3-blobfile %_description


%prep
%autosetup -p1 -n blobfile-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l blobfile


%check
%pyproject_check_import
# We could run tests with python testing/run.py but
# "The tests are rather slow, ~7 minutes to run (even though large file tests
# are disabled) and require accounts with every cloud provider."


%files -n python3-blobfile -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
