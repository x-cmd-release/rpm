Name:           x-cmd
Version:        v0.5.5
Release:        1%{?dist}
Summary:        Bootstrap 1000+ command line tools in seconds
BuildArch:      noarch

License:        AGPL-3.0
URL:            https://www.x-cmd.com

Source0:        %{name}-%{version}.tgz

Requires:       curl

%description
Ultimate Integration of POSIX SHELL AWK. A super weapon built for the super engineer


%define  _pkgsum        .369a6a4b
%define  _pkgdir        %{_prefix}/share/x-cmd/v/%{_pkgsum}

%prep

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/x-cmd/v
cp -rf %{SOURCE0} $RPM_BUILD_ROOT/%{_pkgdir}.tgz


%post
mkdir -p %{_pkgdir}
tar -zxf %{_pkgdir}.tgz -C %{_pkgdir} >/dev/null 2>&1 || exit 1
rm -rf %{_prefix}/share/x-cmd/v/latest || exit 1
ln -sf %{_pkgdir} %{_prefix}/share/x-cmd/v/latest || exit 1
mkdir -p %{_bindir}
cp -rf %{_pkgdir}/mod/x-cmd/lib/bin/x-cmd %{_bindir}/x-cmd || exit 1

%postun
[ ! -f %{_pkgdir}.tgz ]     || rm -rf %{_pkgdir}.tgz
[ ! -f %{_bindir}/x ]       || rm -rf %{_bindir}/x
[ ! -f %{_bindir}/x-cmd ]   || rm -rf %{_bindir}/x-cmd


%files
%{_prefix}/share/x-cmd/v/%{_pkgsum}.tgz

%changelog
* Mon Feb 24 2025 Li Junhao <l@x-cmd.com> - v0.5.5-1
- First time packaging x-cmd into an RPM package


