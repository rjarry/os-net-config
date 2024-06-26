%define branch copr

Name: os-net-config
Version: 17.1.0
Release: 1
Summary: Host network configuration tool for OpenStack.
Source0: https://github.com/rjarry/os-net-config/archive/%{branch}.tar.gz#/%{name}-%{version}-%{release}.tar.gz

License: Apache-2.0
URL: https://github.com/os-net-config/os-net-config
BuildArch: noarch

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools

Requires: initscripts
Requires: iproute
Requires: ethtool
Requires: dhclient
Requires: mstflint
Requires: NetworkManager-ovs
# these two are not published on pypi.org and fail the resolution via python3dist()
Requires: python3-libnmstate
Requires: python3-nispor

%description
Host network configuration tool for OpenStack.

%prep
%autosetup -n %{name}-%{branch}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files os_net_config

%files -f %{pyproject_files}
%doc README.rst
%doc LICENSE

%{_bindir}/os-net-config
%{_bindir}/os-net-config-dcb
%{_bindir}/os-net-config-sriov
%{_bindir}/os-net-config-sriov-bind

%changelog
* Wed Jun 26 2024 Robin Jarry <rjarry@redhat.com> - 17.1.0-1
- COPR packging.
