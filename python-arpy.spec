%global srcname arpy

Name:          python-%{srcname}
Summary:       Library for accessing "ar" files
License:       BSD
URL:           https://github.com/viraptor/arpy

Version:       2.2.0
Release:       1
Source0:       https://github.com/viraptor/arpy/archive/refs/tags/2.2.0.tar.gz

BuildArch:     noarch

%description
arpy is a library for accessing the archive files and reading the contents.
It supports extended long filenames in both GNU and BSD format. Right now it
does not support the symbol tables, but can ignore them gracefully.

%package -n python3-%{srcname}
Summary:       %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-nose

%description -n python3-%{srcname}
arpy is a library for accessing the archive files and reading the contents.
It supports extended long filenames in both GNU and BSD format. Right now it
does not support the symbol tables, but can ignore them gracefully.
This package allows using arpy in Python 3 applications.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
nosetests-3

%files -n python3-%{srcname}
%{python3_sitelib}/arpy*
%{python3_sitelib}/__pycache__/*

%changelog
* Fri Jul 16 2021 yinyongkang <yinyongkang@kylinos.cn> - 2.2.0-1
- Init Package
