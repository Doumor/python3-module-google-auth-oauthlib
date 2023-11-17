%define pypi_name google-auth-oauthlib

%def_without check

Name:    python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: Google oAuth Authentication Library
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/GoogleCloudPlatform/google-auth-library-python-oauthlib

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-click
BuildRequires: python3-module-mock

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
This library provides oauthlib integration with google-auth.

%prep
%setup


%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest


%files
%doc README.rst LICENSE
%{_bindir}/google-oauthlib-tool
%python3_sitelibdir/google_auth_oauthlib/
%python3_sitelibdir/google_auth_oauthlib-%version.dist-info

%changelog
* Thu Oct 12 2023 Danilkin Danila <danild@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
