%define srcname	plasma-wallpaper-FlyMode

Summary:	An animated wallpaper
Name:		plasma-wallpaper-flymode
Version:	0.8
Release:	2
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		http://www.kde-look.org
Source0:	http://www.kde-look.org/CONTENT/content-files/119187-%{srcname}_%{version}.tar.gz
BuildRequires:	kdebase4-workspace-devel
Requires:	kdebase4-runtime
Provides:	plasma-applet

%description
The wallpaper plugin moves a seamless wallpaper picture endlessly over the 
desktop, making you feel like flying.

%files  
%{_kde_libdir}/kde4/plasma_wallpaper_FlyMode.so
%{_kde_services}/%{srcname}.desktop

#------------------------------------------------------------------------------

%prep
%setup -q -n %{srcname}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

