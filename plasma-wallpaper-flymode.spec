%define name	plasma-wallpaper-flymode
%define version	 0.8
%define srcname	plasma-wallpaper-FlyMode
%define release	%mkrel 0
%define Summary	 An animated wallpaper


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://www.kde-look.org/CONTENT/content-files/119187-%{srcname}_%{version}.tar.gz
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		http://www.kde-look.org/content/show.php/Wallpaper+Plugin+%22Fly+Mode%22?content=119187
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase4-workspace-devel
Requires:	kdebase4-runtime => 4.3
Provides:	plasma-applet

%description
The wallpaper plugin moves a seamless wallpaper picture endlessly over the 
desktop, making you feel like flying.

%files  
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_wallpaper_FlyMode.so
%_kde_services/%{srcname}.desktop

#------------------------------------------------------------------------------

%prep
%setup -q -n %{srcname}

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%{makeinstall_std} -C build


%clean
%__rm -rf %{buildroot}
