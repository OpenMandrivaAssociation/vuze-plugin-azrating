
%define plugin	azrating

Name:		vuze-plugin-%plugin
Version:	1.3.1
Release:	%mkrel 1
Summary:	Vuze plugin: Rating
Group:		Networking/File transfer
License:	GPLv2+
URL:		http://azureus.sourceforge.net/
Source0:	http://azureus.sourceforge.net/plugins/%{plugin}_%{version}_src.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	vuze
BuildRequires:	java-rpmbuild
BuildRequires:	ant
Requires:	vuze
BuildArch:      noarch

%description
Lets users rate and comment torrents.

This package is part of default vuze installation.

%prep
%setup -q -c
find -name '*.class' -delete
ln -s %{_datadir}/azureus/build.plugins.xml build.xml

%build
CLASSPATH=%{_datadir}/azureus/Azureus2.jar:$(build-classpath swt) %ant makejar -Dsource.dir=.

%install
rm -rf %{buildroot}

install -d -m755 %{buildroot}%{_datadir}/azureus/plugins/%plugin
install -m644 %{plugin}_%{version}.jar %{buildroot}%{_datadir}/azureus/plugins/%plugin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_datadir}/azureus/plugins/%plugin
%{_datadir}/azureus/plugins/%plugin/%{plugin}_%{version}.jar
