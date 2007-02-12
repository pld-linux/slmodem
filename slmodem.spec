# NOTE: no SMP drivers for now - I don't know if these binaries would work?
# TODO: test it on SMP and add SMP modules or update above comment
#
# - for 2.6.20 - symbols usb_deregister and usb_register_driver used by slusb.ko
#   will be GPL-only in a future.
# 
# Conditional build:
%bcond_without	dist_kernel	# without kernel from distribution
%bcond_without	kernel		# don't build kernel modules
%bcond_without	smp		# don't build SMP module
%bcond_without	userspace	# don't build userspace module
%bcond_with	verbose		# verbose build (V=1)

%define _snap	20061021

#
%define	rel	0.%{_snap}.2
Summary:	Smart Link soft modem drivers
Summary(de.UTF-8):	Smart Link Software Modem Treiber
Summary(pl.UTF-8):	Sterowniki do modemów programowych Smart Link
Name:		slmodem
Version:	2.9.11
Release:	%{rel}
License:	BSD almost without source
Group:		Base/Kernel
Source0:	http://linmodems.technion.ac.il/packages/smartlink/%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	8e1858b0a6d16fce73966759732986ab
Source1:	%{name}.init
Source2:	%{name}.sysconfig
# In 2.6.19 there was an interrupt handling infrastructure change - per cpu global struct pt_regs *
# variable is used instead of passing it in irq handlers.
Patch1:		%{name}-2.9.11-irq-global-pt_regs-2.6.19.patch
URL:		http://www.smlink.com/
BuildRequires:	%{kgcc_package}
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build}
BuildRequires:	rpmbuild(macros) >= 1.330
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Smart Link soft modem drivers.

%description -l de.UTF-8
Smart Link Software Modem Treiber.

%description -l pl.UTF-8
Sterowniki do modemów programowych Smart Link.

%package -n kernel%{_alt_kernel}-char-slmodem-amr
Summary:	Linux kernel driver for Smart Link soft modem AMR/PCI component
Summary(de.UTF-8):	Linux Kernel Treiber für Smart Link AMR/PCI Software Modems
Summary(pl.UTF-8):	Sterownik jądra Linuksa dla elementu AMR/PCI modemów programowych Smart Link
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod

%description -n kernel%{_alt_kernel}-char-slmodem-amr
Linux kernel drivers for Smart Link soft modem. This package contains
driver for HAMR5600 based AMR/CNR/MDC/ACR modem cards and SmartPCI56,
SmartPCI561 based PCI modem cards.

%description -n kernel%{_alt_kernel}-char-slmodem-amr -l de.UTF-8
Linux Kernel Treiber für Smart Link Software Modems. Dieses Packet
enthält Treiber für HAMR5600 AMR/CNR/MDC/ACR basierende Modems und
für SmartPCI56, SmartPCI561 PCI basierende Modems.

%description -n kernel%{_alt_kernel}-char-slmodem-amr -l pl.UTF-8
Sterowniki jądra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik do opartych na HAMR5600 kart modemowych
AMR/CNR/MDC/ACR oraz kart PCI SmartPCI56 i SmartPCI561.

%package -n kernel%{_alt_kernel}-char-slmodem-usb
Summary:	Linux kernel driver for Smart Link soft modem USB component
Summary(de.UTF-8):	Linux Kernel Trebier für Smart Link USB Software Modems
Summary(pl.UTF-8):	Sterownik jądra Linuksa dla elementu USB modemów programowych Smart Link
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod

%description -n kernel%{_alt_kernel}-char-slmodem-usb
Linux kernel drivers for Smart Link soft modem. This package contains
driver for SmartUSB56 based USB modem.

%description -n kernel%{_alt_kernel}-char-slmodem-usb -l de.UTF-8
Linux Kernel Treiber für Smart Link Software Modems. Dieses Packet
enthält Treiber für SmartUSB56 basierende Modems.

%description -n kernel%{_alt_kernel}-char-slmodem-usb -l pl.UTF-8
Sterowniki jądra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik dla modemów USB opartych na SmartUSB56.

%package -n kernel%{_alt_kernel}-smp-char-slmodem-amr
Summary:	Linux kernel driver for Smart Link soft modem AMR/PCI component (SMP)
Summary(de.UTF-8):	Linux Kernel Treiber für Smart Link AMR/PCI Software Modems (SMP)
Summary(pl.UTF-8):	Sterownik jądra Linuksa dla elementu AMR/PCI modemów programowych Smart Link (SMP)
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod

%description -n kernel%{_alt_kernel}-smp-char-slmodem-amr
Linux kernel drivers for Smart Link soft modem. This package contains
driver for HAMR5600 based AMR/CNR/MDC/ACR modem cards and SmartPCI56,
SmartPCI561 based PCI modem cards. SMP kernels.

%description -n kernel%{_alt_kernel}-smp-char-slmodem-amr -l de.UTF-8
Linux Kernel Treiber für Smart Link Software Modems. Dieses Packet
enthält Treiber für HAMR5600 AMR/CNR/MDC/ACR basierende Modems und
für SmartPCI56, SmartPCI561 PCI basierende Modems. SMP Kernel Treiber.

%description -n kernel%{_alt_kernel}-smp-char-slmodem-amr -l pl.UTF-8
Sterowniki jądra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik do opartych na HAMR5600 kart modemowych
AMR/CNR/MDC/ACR oraz kart PCI SmartPCI56 i SmartPCI561. Jądra SMP.

%package -n kernel%{_alt_kernel}-smp-char-slmodem-usb
Summary:	Linux kernel driver for Smart Link soft modem USB component (SMP)
Summary(de.UTF-8):	Linux Kernel Trebier für Smart Link USB Software Modems (SMP)
Summary(pl.UTF-8):	Sterownik jądra Linuksa dla elementu USB modemów programowych Smart Link (SMP)
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod

%description -n kernel%{_alt_kernel}-smp-char-slmodem-usb
Linux kernel drivers for Smart Link soft modem. This package contains
driver for SmartUSB56 based USB modem. SMP kernels.

%description -n kernel%{_alt_kernel}-smp-char-slmodem-usb -l de.UTF-8
Linux Kernel Treiber für Smart Link Software Modems. Dieses Packet
enthält Treiber für SmartUSB56 basierende Modems. SMP Kernel Treiber.

%description -n kernel%{_alt_kernel}-smp-char-slmodem-usb -l pl.UTF-8
Sterowniki jądra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik dla modemów USB opartych na SmartUSB56. Jądra
SMP.

%prep
%setup -q -n %{name}-%{version}-%{_snap}

%patch1 -p1

%build
cd drivers
mv amrlibs.o ..
ln -s ../amrlibs.o amrlibs.o

%if %{with kernel}
%build_kernel_modules -m slamr,slusb
%endif

%if %{with userspace}
%{__make} -C ../modem \
	CC="%{__cc}"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_var}/lib/%{name}}

%if %{with userspace}
install modem/slmodemd	 $RPM_BUILD_ROOT%{_sbindir}
install modem/modem_test $RPM_BUILD_ROOT%{_sbindir}/slmodem-test
install %{SOURCE1}	 $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2}	 $RPM_BUILD_ROOT/etc/sysconfig/%{name}
%endif

%if %{with kernel}
%install_kernel_modules -m drivers/slamr,drivers/slusb -d misc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post -n kernel%{_alt_kernel}-char-slmodem-amr
%depmod %{_kernel_ver}

%postun -n kernel%{_alt_kernel}-char-slmodem-amr
%depmod %{_kernel_ver}

%post -n kernel%{_alt_kernel}-char-slmodem-usb
%depmod %{_kernel_ver}

%postun -n kernel%{_alt_kernel}-char-slmodem-usb
%depmod %{_kernel_ver}

%post -n kernel%{_alt_kernel}-smp-char-slmodem-amr
%depmod %{_kernel_ver}smp

%postun -n kernel%{_alt_kernel}-smp-char-slmodem-amr
%depmod %{_kernel_ver}smp

%post -n kernel%{_alt_kernel}-smp-char-slmodem-usb
%depmod %{_kernel_ver}smp

%postun -n kernel%{_alt_kernel}-smp-char-slmodem-usb
%depmod %{_kernel_ver}smp

%post
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun
if [ "$1" = "0" ]; then
	%service %{name} stop
	/sbin/chkconfig --del %{name}
fi

%if %{with userspace}
%files
%defattr(644,root,root,755)
%doc COPYING README* Changes
%attr(755,root,root) %{_sbindir}/*
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%dir %{_var}/lib/%{name}
%endif

%if %{with kernel}
%files -n kernel%{_alt_kernel}-char-slmodem-amr
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/slamr.ko*

%files -n kernel%{_alt_kernel}-char-slmodem-usb
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/slusb.ko*

%if %{with smp}
%files -n kernel%{_alt_kernel}-smp-char-slmodem-amr
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/slamr.ko*

%files -n kernel%{_alt_kernel}-smp-char-slmodem-usb
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/slusb.ko*
%endif
%endif
