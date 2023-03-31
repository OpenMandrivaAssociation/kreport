%define major 4
%define libname %mklibname KReport3 %{major}
%define devname %mklibname KReport3 -d
%define olibname %mklibname KReport3 3

Name:		kreport
Version:	3.2.0
Release:	4
Source0:	http://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz
Patch1:		kreport-3.0.2-pkgconfig.patch
Summary:	Framework for the creation and generation of reports
URL:		http://community.kde.org/KReport
License:	LGPLv2+
Group:		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KPropertyCore)
BuildRequires:	cmake(KPropertyWidgets)
BuildRequires:	python2
BuildRequires:	doxygen graphviz qt5-assistant
Requires:	%{libname} = %{EVRD}

%description
KReport is a framework for the creation and generation of reports in
multiple formats.

It is used by Kexi and Calligra Plan.


%package -n %{libname}
Summary: Framework for the creation and generation of reports
Group: System/Libraries
Requires: %{name} = %{EVRD}
Obsoletes: %{olibname}

%description -n %{libname}
KReport is a framework for the creation and generation of reports in
multiple formats.

It is used by Kexi and Calligra Plan.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

KReport is a framework for the creation and generation of reports in
multiple formats.

It is used by Kexi and Calligra Plan.

%prep
%setup -q
%autopatch -p1
# Build script requires python 2.x
#ln -s %{_bindir}/python2 python
export PATH=`pwd`:%{_libdir}/qt5/bin:$PATH

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%{_libdir}/qt5/plugins/kreport3
%{_datadir}/kreport3
%{_datadir}/kservicetypes5/kreport_elementplugin.desktop

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/KReport3
%{_libdir}/qt5/mkspecs/modules/qt_KReport3.pri
%doc %{_docdir}/qt5/*
