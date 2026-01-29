%define _build_id_links none

# global info
%global major 25.30
%global minor 422-1
# Distro info
%global fedora 43

Name:     amdamf-pro-runtime
Version:  %{major}
Release:  1%{?dist}
License:       AMDGPU PRO  EULA NON-REDISTRIBUTABLE
Group:         System Environment/Libraries
Summary:       System runtime for AMD Advanced Media Framework
URL:      http://repo.radeon.com/amdgpu


%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amf/%{major}/ubuntu/pool/proprietary/a/amf-amdgpu-pro/amf-amdgpu-pro_%{major}-%{minor}_amd64.deb
Source1:  http://repo.radeon.com/amf/%{major}/ubuntu/pool/proprietary/liba/libamdenc-amdgpu-pro/libamdenc-amdgpu-pro_%{major}-%{minor}_amd64.deb

Provides:      amf-runtime = %{major}-%{release}
Provides:      amf-runtime(x86_64) = %{major}-%{release}
Provides:      amf-amdgpu-pro = %{major}-%{minor}
Provides:      amf-amdgpu-pro(x86_64) = %{major}-%{minor}
Provides:      libamfrt64.so.1()(64bit) 
Provides:      libamdenc-amdgpu-pro = %{major}-%{minor}
Provides:      libamdenc-amdgpu-pro(x86_64) = %{major}-%{minor}
Provides:      libamdenc64.so.1.0()(64bit)  
Provides:      libamdenc64.so.1.0()(64bit)  

Recommends:	rocm-opencl

BuildRequires: wget 
BuildRequires: cpio

Requires(post): /sbin/ldconfig  
Requires(postun): /sbin/ldconfig 

Requires:      opencl-filesystem

Recommends:	 rocm-opencl-runtime  

%description
System runtime for AMD Advanced Media Framework

%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

ar x --output . %{SOURCE1}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install
mkdir -p %{buildroot}/usr/%{_lib}
mkdir -p %{buildroot}/usr/share/licenses/amf-amdgpu-pro
mkdir -p %{buildroot}/usr/share/licenses/libamdenc-amdgpu-pro
#
cp -r files/opt/amf/lib/x86_64-linux-gnu/* %{buildroot}/usr/%{_lib}/
cp -r files/usr/share/doc/amf-amdgpu-pro/copyright %{buildroot}/usr/share/licenses/amf-amdgpu-pro/LICENSE
cp -r files/usr/share/doc/libamdenc-amdgpu-pro/copyright %{buildroot}/usr/share/licenses/libamdenc-amdgpu-pro/LICENSE

%files
/usr/lib64/libamf*
/usr/lib64/libamdenc*
/usr/share/*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
