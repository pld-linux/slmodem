# NOTE: no SMP drivers for now - I don't know if these binaries would work?
# TODO: test it on SMP and add SMP modules or update above comment
# 
# Conditional build:
%bcond_without	dist_kernel	# without kernel from distribution
%bcond_without	kernel		# don't build kernel modules
%bcond_without	smp		# don't build SMP module
%bcond_without	userspace	# don't build userspace module
%bcond_with	verbose		# verbose build (V=1)
#
Summary:	Smart Link soft modem drivers
Summary(pl):	Sterowniki do modemów programowych Smart Link
Name:		slmodem
Version:	2.9.10
%define	rel	1
Release:	%{rel}
License:	BSD almost without source
Vendor:		Smart Link Ltd.
Group:		Base/Kernel
# ftp://ftp.smlink.com/linux/unsupported/
Source0:	http://www.smlink.com/main/down/%{name}-%{version}.tar.gz
# Source0-md5:	cbc4918f2ee9ed4952d3f4309d364b35
# Source0-size:	806884
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Patch0:		%{name}-new-kernel-workaround.patch
URL:		http://www.smlink.com/
%{?with_dist_kernel:BuildRequires:	kernel-headers}
BuildRequires:	%{kgcc_package}
BuildRequires:	rpmbuild(macros) >= 1.118
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Smart Link soft modem drivers.

%description -l pl
Sterowniki do modemów programowych Smart Link.

%package -n kernel-char-slmodem-amr
Summary:	Linux kernel driver for Smart Link soft modem AMR/PCI component
Summary(pl):	Sterownik j±dra Linuksa dla elementu AMR/PCI modemów programowych Smart Link
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod

%description -n kernel-char-slmodem-amr
Linux kernel drivers for Smart Link soft modem. This package contains
driver for HAMR5600 based AMR/CNR/MDC/ACR modem cards and SmartPCI56,
SmartPCI561 based PCI modem cards.

%description -n kernel-char-slmodem-amr -l pl
Sterowniki j±dra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik do opartych na HAMR5600 kart modemowych
AMR/CNR/MDC/ACR oraz kart PCI SmartPCI56 i SmartPCI561.

%package -n kernel-char-slmodem-usb
Summary:	Linux kernel driver for Smart Link soft modem USB component
Summary(pl):	Sterownik j±dra Linuksa dla elementu USB modemów programowych Smart Link
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod

%description -n kernel-char-slmodem-usb
Linux kernel drivers for Smart Link soft modem. This package contains
driver for SmartUSB56 based USB modem.

%description -n kernel-char-slmodem-usb -l pl
Sterowniki j±dra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik dla modemów USB opartych na SmartUSB56.

%package -n kernel-smp-char-slmodem-amr
Summary:	Linux kernel driver for Smart Link soft modem AMR/PCI component (SMP)
Summary(pl):	Sterownik j±dra Linuksa dla elementu AMR/PCI modemów programowych Smart Link (SMP)
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod

%description -n kernel-smp-char-slmodem-amr
Linux kernel drivers for Smart Link soft modem. This package contains
driver for HAMR5600 based AMR/CNR/MDC/ACR modem cards and SmartPCI56,
SmartPCI561 based PCI modem cards. SMP kernels.

%description -n kernel-smp-char-slmodem-amr -l pl
Sterowniki j±dra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik do opartych na HAMR5600 kart modemowych
AMR/CNR/MDC/ACR oraz kart PCI SmartPCI56 i SmartPCI561. J±dra SMP.

%package -n kernel-smp-char-slmodem-usb
Summary:	Linux kernel driver for Smart Link soft modem USB component (SMP)
Summary(pl):	Sterownik j±dra Linuksa dla elementu USB modemów programowych Smart Link (SMP)
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod

%description -n kernel-smp-char-slmodem-usb
Linux kernel drivers for Smart Link soft modem. This package contains
driver for SmartUSB56 based USB modem. SMP kernels.

%description -n kernel-smp-char-slmodem-usb -l pl
Sterowniki j±dra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik dla modemów USB opartych na SmartUSB56. J±dra SMP.

%prep
%setup -q
%patch0 -p1

%build
cd drivers
cp amrlibs.o ..

%if %{with kernel}
# kernel module(s)
for cfg in %{?with_dist_kernel:%{?with_smp:smp} up}%{!?with_dist_kernel:nondist}; do
	if [ ! -r "%{_kernelsrcdir}/config-$cfg" ]; then
		exit 1
	fi
	rm -rf include
	install -d include/{linux,config}
	ln -sf %{_kernelsrcdir}/config-$cfg .config
	ln -sf %{_kernelsrcdir}/include/linux/autoconf-$cfg.h include/linux/autoconf.h
	ln -sf %{_kernelsrcdir}/include/asm-%{_target_base_arch} include/asm
	touch include/config/MARKER
	
	# patching/creating makefile(s) (optional)
	%{__make} -C %{_kernelsrcdir} clean \
		RCS_FIND_IGNORE="-name '*.ko' -o" \
		M=$PWD O=$PWD \
		%{?with_verbose:V=1}
	ln -sf ../amrlibs.o amrlibs.o
	%{__make} -C %{_kernelsrcdir} modules \
		CC="%{__cc}" CPP="%{__cpp}" \
		M=$PWD O=$PWD \
		%{?with_verbose:V=1}
	for mod in *.ko; do
		mod=$(echo "$mod" | sed -e 's#\.ko##g')
		mv $mod.ko ../$mod-$cfg.ko
	done
done
%endif

%if %{with userspace}
%{__make} -C ../modem \
	CC="%{__cc}"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}
install -d $RPM_BUILD_ROOT{%{_sbindir},/lib/modules/%{_kernel_ver}{,smp}/misc,%{_var}/lib/%{name}}

%if %{with userspace}
install modem/slmodemd	 $RPM_BUILD_ROOT%{_sbindir}
install modem/modem_test $RPM_BUILD_ROOT%{_sbindir}/slmodem-test
install %{SOURCE1}	 $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2}	 $RPM_BUILD_ROOT/etc/sysconfig/%{name}
%endif

%if %{with kernel}
%if %{with_dist_kernel}
for mod in *-nondist.ko; do
	nmod=$(echo "$mod" | sed -e 's#-nondist##g')
	install $mod $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/$nmod
done
%else
for mod in *-up.ko; do
	nmod=$(echo "$mod" | sed -e 's#-up##g')
	install $mod $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/$nmod
done
%if %{with smp}
for mod in *-smp.ko; do
	nmod=$(echo "$mod" | sed -e 's#-smp##g')
	install $mod $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/$nmod
done
%endif
%endif
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post -n kernel-char-slmodem-amr
%depmod %{_kernel_ver}

%postun -n kernel-char-slmodem-amr
%depmod %{_kernel_ver}

%post -n kernel-char-slmodem-usb
%depmod %{_kernel_ver}

%postun -n kernel-char-slmodem-usb
%depmod %{_kernel_ver}

%post -n kernel-smp-char-slmodem-amr
%depmod %{_kernel_ver}smp

%postun -n kernel-smp-char-slmodem-amr
%depmod %{_kernel_ver}smp

%post -n kernel-smp-char-slmodem-usb
%depmod %{_kernel_ver}smp

%postun -n kernel-smp-char-slmodem-usb
%depmod %{_kernel_ver}smp

%post
/sbin/chkconfig --add %{name}
if [ -f /var/lock/subsys/%{name} ]; then
	/etc/rc.d/init.d/%{name} restart >&2
else
	echo "Run \"/etc/rc.d/init.d/%{name} start\" to start %{name} daemon." >&2
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/%{name} ]; then
		/etc/rc.d/init.d/%{name} stop
	fi
	/sbin/chkconfig --del %{name}
fi

%if %{with userspace}
%files
%defattr(644,root,root,755)
%doc COPYING README* Changes
%attr(755,root,root) %{_sbindir}/*
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(640,root,root) %config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/%{name}
%dir %{_var}/lib/%{name}
%endif

%if %{with kernel}
%files -n kernel-char-slmodem-amr
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/slamr.*o*

%files -n kernel-char-slmodem-usb
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/slusb.*o*

%if %{with smp}
%files -n kernel-smp-char-slmodem-amr
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/slamr.*o*

%files -n kernel-smp-char-slmodem-usb
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/slusb.*o*
%endif
%endif
