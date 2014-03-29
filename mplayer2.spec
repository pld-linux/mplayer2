#
%bcond_with	directfb	# with DirectFB video output
%bcond_with	dxr3		# enable use of DXR3/H+ hardware MPEG decoder
%bcond_with	ggi		# with ggi video output
%bcond_with	nas		# with NAS audio output
%bcond_with	svga		# with svgalib video output
%bcond_without	osd		# with osd menu support
%bcond_without	altivec		# without altivec support
%bcond_without	x264		# without x264 support
%bcond_with	xmms		# with XMMS inputplugin support
%bcond_without	aalib		# without aalib video output
%bcond_without	jack		# without JACKD support
%bcond_without	alsa		# without ALSA audio output
%bcond_with	arts		# with arts audio output
%bcond_without	caca		# without libcaca video output
%bcond_without	cdparanoia	# without cdparanoia support
%bcond_without	dvdnav		# without dvdnav support
%bcond_without	enca		# disable using ENCA charset oracle library
%bcond_with	esd		# enable EsounD sound support
%bcond_without	faad		# disable FAAD2 (AAC) support
%bcond_without	gif		# disable GIF support
%bcond_without	gui		# without GTK+ GUI
%bcond_without	joystick	# disable joystick support
%bcond_without	libdts		# disable libdts support
%bcond_without	libdv		# disable libdv en/decoding support
%bcond_without	lirc		# without lirc support
%bcond_with	live		# without LIVE555 libraries
%bcond_without	lzo		# with LZO support (requires lzo 2.x)
%bcond_without	mad		# without mad (audio MPEG) support
%bcond_without	pulseaudio	# without pulseaudio output
%bcond_without	quicktime	# without binary quicktime dll support
%bcond_without	real		# without Real* 8/9 codecs support
%bcond_without	runtime		# disable runtime cpu detection, just detect CPU
				#  in compile time (advertised by mplayer authors as working faster); in this case
				#  mplayer may not work on machine other then where it was compiled
%bcond_without	select		# disable audio select() support (for example required this option ALSA or Vortex2 driver)
%bcond_without	smb		# disable Samba (SMB) input support
%bcond_without	theora		# without theora support
%bcond_without	win32		# without win32 codecs support
%bcond_without	vdpau		# disable vdpau
%bcond_without	vidix		# disable vidix
%bcond_without	vorbis		# without Ogg-Vorbis audio support
%bcond_with	system_vorbis	# use system libvorbis instead of internal tremor
%bcond_without	xvid		# disable XviD codec
%bcond_without	mencoder	# disable mencoder (a/v encoder) compilation
%bcond_without	sdl		# disable SDL
%bcond_without	doc		# don't build docs (slow)
%bcond_without	amr		# enable Adaptive Multi Rate (AMR) speech codec support
%bcond_without	gnomess		# disable controling gnome screensaver
%bcond_without	ssse3		# sse3 optimizations (needs binutils >= 2.16.92)
%bcond_with	system_ffmpeg	# use ffmpeg-devel, rather bundled sources (likely needs ffmpeg from same svn revision than mplayer)
%bcond_with	on2		# with patches from On2 Flix Engine for Linux

%bcond_with	nonfree		# non free options of package
%bcond_without	va		# VAAPI (Video Acceleration API)
%bcond_without	vpx		# VP8, a high-quality video codec

Summary:	MPlayer - THE Movie Player for UN*X
Summary(de.UTF-8):	MPlayer ist ein unter der freien GPL-Lizenz stehender Media-Player
Summary(es.UTF-8):	Otro reproductor de películas
Summary(ko.UTF-8):	리눅스용 미디어플레이어
Summary(pl.UTF-8):	Odtwarzacz filmów dla systemów uniksowych
Summary(pt_BR.UTF-8):	Reprodutor de filmes
Name:		mplayer2
Version:	2.0
Release:	16
License:	GPL
Group:		Applications/Multimedia
Source0:	http://ftp.mplayer2.org/pub/release/%{name}-build-%{version}.tar.xz
# Source0-md5:	05b93784de995235e2758f182de15f73
Patch0:		format-security.patch
URL:		http://www.mplayer2.org/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
%{?with_sdl:BuildRequires:	SDL-devel >= 1.1.7}
%{?with_aalib:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	artsc-devel}
%{?with_ssse3:BuildRequires:	binutils >= 3:2.16.92}
%{?with_cdparanoia:BuildRequires:	cdparanoia-III-devel}
BuildRequires:	dirac-devel
%{?with_doc:BuildRequires:	docbook-dtd412-xml}
%{?with_doc:BuildRequires:	docbook-style-xsl}
%{?with_dxr3:BuildRequires:	em8300-devel}
%{?with_enca:BuildRequires:	enca-devel}
%{?with_esd:BuildRequires:	esound-devel}
BuildRequires:	faac-devel
%{?with_faad:BuildRequires:	faad2-devel >= 2.0}
%{?with_system_ffmpeg:BuildRequires:	ffmpeg-devel >= 0.4.9-4.20081024.3}
BuildRequires:	freetype-devel >= 2.0.9
BuildRequires:	fribidi-devel
BuildRequires:	tar >= 1:1.22
%{?with_vidix:BuildRequires:	vidix-devel}
%{?with_altivec:BuildRequires:	gcc >= 5:4.1}
%{?with_gnomess:BuildRequires:	dbus-glib-devel}
%{?with_gif:BuildRequires:	giflib-devel}
%{?with_gui:BuildRequires:	gtk+2-devel}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
BuildRequires:	lame-libs-devel
%{?with_caca:BuildRequires:	libcaca-devel}
BuildRequires:	libdc1394-devel
%{?with_libdts:BuildRequires:	libdts-devel}
%{?with_libdv:BuildRequires:	libdv-devel > 0.9.5}
%{?with_dvdnav:BuildRequires:	libdvdnav-devel >= 4.1.3}
%{?with_ggi:BuildRequires:	libggi-devel}
BuildRequires:	libjpeg-devel
%{?with_mad:BuildRequires:	libmad-devel}
BuildRequires:	libmng-devel
BuildRequires:	libmpcdec-devel >= 1.2.1
BuildRequires:	libpng-devel
%{?with_smb:BuildRequires:	libsmbclient-devel}
%{?with_theora:BuildRequires:	libtheora-devel}
%{?with_vdpau:BuildRequires:	libvdpau-devel}
BuildRequires:	libvorbis-devel
%{?with_vpx:BuildRequires:	libvpx-devel >= 0.9.1}
%{?with_system_vorbis:BuildRequires:	libvorbis-devel}
%{?with_x264:BuildRequires:	libx264-devel >= 0.1.3-1.20110327}
BuildRequires:	libxslt-progs
%{?with_lirc:BuildRequires:	lirc-devel}
%{?with_live:BuildRequires:	live-devel}
%{?with_lzo:BuildRequires:	lzo-devel >= 2.0}
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	ncurses-devel
%{?with_amr:BuildRequires:	opencore-amr-devel}
BuildRequires:	openjpeg-devel
BuildRequires:	pkgconfig
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel >= 0.9}
BuildRequires:	python-modules
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRequires:	schroedinger-devel
BuildRequires:	speex-devel >= 1.1
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	twolame-devel
%{?with_xmms:BuildRequires:	xmms-devel}
%{?with_xvid:BuildRequires:	xvid-devel >= 1:0.9.0}
%ifarch %{ix86} %{x8664}
BuildRequires:	yasm
%endif
BuildRequires:	zlib-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXvMC-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		specflags_ia32	-fomit-frame-pointer
%if %{with altivec}
%define		specflags_ppc	-maltivec
%endif

%description
Movie player. Supported input formats: VCD (VideoCD), MPEG1/2, RIFF
AVI, ASF 1.0, Quicktime. Supported audio codecs: PCM (uncompressed),
MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM. Supported video codecs:
MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX. Supported output
devices: Matrox G200/G400 hardware, Matrox G200/G400 overlay, X11
optionally with SHM extension, X11 using overlays with the Xvideo
extension, OpenGL renderer, Matrox G400 YUV support on framebuffer
Voodoo2/3 hardware, SDL v1.1.7 driver etc.

If you want to use win32 codecs install w32codec package.

%description -l de.UTF-8
MPlayer ist ein unter der freien GPL-Lizenz stehender Media-Player.
Kennzeichnend ist die herausragende Format- und
Plattform-Kompatibilität.

Es unterstützt eine Vielzahl von Video und Audio-Codecs, darunter auch
plattformexklusive, wodurch etwa Windows Media auch außerhalb von
Windows wiedergegeben werden kann. Darüber hinaus unterstützt er DVB.
Eine besondere Fehlertoleranz ermöglicht es dem mehrfach
ausgezeichneten Player, auch defekte Dateien abzuspielen. Eine weitere
Stärke ist dabei der Wegfall jeglicher Installation, so dass bereits
installierte Codecs nicht mit MPlayer kollidieren können.

%description -l es.UTF-8
Reproductor video. Formatos de entrada soportados: VCD (VideoCD),
MPEG1/2, RIFF AVI, ASF 1.0, Quicktime. Codecs de audio soportados: PCM
(uncompressed), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM. Codecs
de video soportados: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Dispositivos de salida soportados: Matrox G200/G400 hardware, Matrox
G200/G400 overlay, X11 optionalmente con la extensión SHM, X11 usando
overlays con la extensión Xvideo, plasmador OpenGL, soporte de Matrox
G400 YUV en hardware de framebuffer de Voodoo2/3, controlador SDL
v1.1.7 etc.

Si quiere usar codecs Win32, instale el paquete w32codec.

%description -l ko.UTF-8
MPlayer는 리눅스용 무비플레이어입니다. 대부분의 mpeg, avi 그리고 asf
파일을 재생합니다. VCD, DVD, 심 지어 DivX까지 볼 수 있습니다.
MPlayer의 또 다른 큰 특징은 출력 드라이버가 다양하다는 것입니다. X11,
Xv, DGA, OpenGL, SVGAlib, fbdev와 작동하며, SDL이나
(Matrox/3dfx/Sis등의) 특정 카드에 종속된 로우레 벨 드라이버들도 사용할
수 있습니다. 대부분의 출력 드라이버들은 소프트웨어 혹은 하드웨어적인
크기조절 (scaling)을 지원하므로, 전체화면으로 영상을 감상할 수
있습니다. 뿐만아니라, 한국어, 영어, 헝가리어, 체코어, 러시아어등의
부드러운(antialiased) 자막폰트도 사용할 수 있습니다.

%description -l pl.UTF-8
Odtwarzacz wideo. Wspierane formaty wejściowe: VCD (VideoCD), MPEG1/2,
RIFF AVI, ASF 1.0, Quicktime. Wspierane kodeki audio: PCM
(nieskompresowane), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM.
Wspierane kodeki wideo: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Wspierane urządzenia wyjściowe: Matrox G200/G400, X11 opcjonalnie z
rozszerzeniem SHM, X11 z rozszerzeniem Xvideo, renderer OpenGL, Matrox
G400 używając framebuffera, Voodoo2/3, SDL v1.1.7 itp.

Jeśli chcesz używać kodeków win32, zainstaluj pakiet w32codec.

%description -l pt_BR.UTF-8
MPlayer é um reprodutor de filmes que suporta vários codecs de vídeo e
áudio. Diferentes mecanismos de reprodução podem também ser
escolhidos, incluindo SDL, SVGALib, frame buffer, aalib, X11 e outros.

%prep
%setup -q -n %{name}-build-%{version}
%patch0 -p1

# set ffmpeg options:
echo "	--arch=%{_target_base_arch}" >>ffmpeg_options
echo "	--cc="%{__cc}"" >>ffmpeg_options
echo "	--extra-cflags="-D_GNU_SOURCE=1 %{rpmcppflags} %{rpmcflags} -I/usr/include/openjpeg-1.5"" >>ffmpeg_options
echo "	--extra-ldflags="%{rpmcflags} %{rpmldflags}"" >>ffmpeg_options
echo "	--disable-debug" >>ffmpeg_options
echo "	--disable-optimizations" >>ffmpeg_options
echo "	--disable-stripping" >>ffmpeg_options
echo "	--enable-avfilter" >>ffmpeg_options
echo "	--enable-gpl" >>ffmpeg_options
echo "	--enable-version3" >>ffmpeg_options
echo "	--enable-libdc1394" >>ffmpeg_options
echo "	--enable-libdirac" >>ffmpeg_options
#echo "	--enable-libfaad" >>ffmpeg_options
#echo "	--enable-libfaadbin" >>ffmpeg_options
# no libgsm-devel
#echo "	--enable-libgsm" >>ffmpeg_options 
echo "	--enable-libmp3lame" >>ffmpeg_options
echo "	--enable-libschroedinger" >>ffmpeg_options
echo "	--enable-libspeex" >>ffmpeg_options
echo "	--enable-libtheora" >>ffmpeg_options
echo "	--enable-libvorbis" >>ffmpeg_options
echo "	%{?with_vpx:--enable-libvpx}" >>ffmpeg_options
# x264 API >= 0.99
echo "	--enable-libx264" >>ffmpeg_options
echo "	--enable-libxvid" >>ffmpeg_options
echo "	--enable-libopencore-amrnb" >>ffmpeg_options
echo "	--enable-libopencore-amrwb" >>ffmpeg_options
echo "	--enable-libopenjpeg" >>ffmpeg_options
echo "	--enable-postproc" >>ffmpeg_options
echo "	--enable-pthreads" >>ffmpeg_options
echo "	--enable-swscale" >>ffmpeg_options
echo "	--enable-vdpau" >>ffmpeg_options
echo "	--enable-x11grab" >>ffmpeg_options
%ifnarch %{ix86} %{x8664}
echo "	--disable-mmx" >>ffmpeg_options
%endif
#% ifarch i386 i486
#echo "	--disable-mmx" >>ffmpeg_options
#% endif
%if %{with nonfree}
echo "	--enable-nonfree" >>ffmpeg_options
echo "	--enable-libfaac" >>ffmpeg_options
%endif
echo "	%{__enable_disable runtime runtime-cpudetect}" >>ffmpeg_options

# set mplayer options:
echo "	--prefix=%{_prefix}" >>mplayer_options
echo "	--confdir=%{_sysconfdir}/mplayer" >>mplayer_options
echo "	--cc="%{__cc}"" >>mplayer_options
echo "	--extra-cflags="$CFLAGS"" >>mplayer_options
#echo "	--real-ldflags="%{rpmldflags}"" >>mplayer_options
echo "	--extra-ldflags="%{?_x_libraries:-L%{_x_libraries}} -lX11 -lXext"" >>mplayer_options
%if %{with system_ffmpeg}
echo "	--disable-libavutil_a" >>mplayer_options
echo "	--disable-libavcodec_a" >>mplayer_options
echo "	--disable-libavformat_a" >>mplayer_options
echo "	--disable-libpostproc_a" >>mplayer_options
echo "	--enable-libavutil_so" >>mplayer_options
echo "	--enable-libavcodec_so" >>mplayer_options
echo "	--enable-libavformat_so" >>mplayer_options
echo "	--enable-libpostproc_so" >>mplayer_options
%endif
%ifnarch %{ix86} %{x8664}
echo "	--disable-mmx" >>mplayer_options
echo "	--disable-mmxext" >>mplayer_options
echo "	--disable-3dnow" >>mplayer_options
echo "	--disable-3dnowext" >>mplayer_options
echo "	--disable-sse" >>mplayer_options
echo "	--disable-sse2" >>mplayer_options
echo "	--disable-fastmemcpy" >>mplayer_options
%endif
echo "	%{__disable ssse3}" >>mplayer_options
#echo "	%{__enable_disable amr libopencore_amrnb} %{__enable_disable amr libopencore_amrwb}" >>mplayer_options
echo "	%{__enable_disable directfb}" >>mplayer_options
echo "	%{__disable dxr3}" >>mplayer_options
echo "	%{__disable ggi}" >>mplayer_options
echo "	%{__disable live}" >>mplayer_options
echo "	%{__disable lzo liblzo}" >>mplayer_options
echo "	%{__disable nas}" >>mplayer_options
echo "	%{__disable svga}" >>mplayer_options
echo "	%{__disable aalib aa}" >>mplayer_options
echo "	%{__disable jack}" >>mplayer_options
echo "	%{__enable_disable alsa}" >>mplayer_options
echo "	%{__disable arts}" >>mplayer_options
echo "	%{__disable caca}" >>mplayer_options
echo "	%{__disable cdparanoia}" >>mplayer_options
echo "	%{__disable enca}" >>mplayer_options
echo "	%{__disable esd}" >>mplayer_options
echo "	%{__disable faad}" >>mplayer_options
echo "	%{__disable gif}" >>mplayer_options
echo "	%{__enable joystick}" >>mplayer_options
echo "	%{__disable libdv}" >>mplayer_options
echo "	%{__disable libdts libdca}" >>mplayer_options
echo "	%{__enable_disable lirc}" >>mplayer_options
echo "	%{__disable mad}" >>mplayer_options
echo "	%{__disable pulseaudio pulse}" >>mplayer_options
echo "	%{__disable quicktime qtx}" >>mplayer_options
echo "	%{__disable real}" >>mplayer_options
echo "	%{__enable_disable runtime runtime-cpudetection}" >>mplayer_options
echo "	%{__disable select}" >>mplayer_options
echo "	%{__disable smb}" >>mplayer_options
echo "	%{__disable win32 win32dll}" >>mplayer_options
echo "	%{__disable vorbis tremor-internal} --disable-tremor %{__disable vorbis libvorbis}" >>mplayer_options
echo "	%{__disable_if system_vorbis tremor-internal}" >>mplayer_options
echo "	%{__enable osd menu}" >>mplayer_options
echo "	%{__disable theora}" >>mplayer_options
echo "	%{__disable x264}" >>mplayer_options
echo "	%{?with_xmms:--enable-xmms --with-xmmsplugindir=%{_libdir}/xmms/Input --with-xmmslibdir=%{_libdir}}" >>mplayer_options
echo "	%{__disable xvid}" >>mplayer_options
echo "	%{__disable vidix}" >>mplayer_options
echo "	%{__disable vdpau}" >>mplayer_options
echo "	%{__disable mencoder}" >>mplayer_options
echo "	--enable-dga1" >>mplayer_options
echo "	--enable-dga2" >>mplayer_options
echo "	%{__enable_disable dvdnav}" >>mplayer_options
echo "	--enable-fbdev" >>mplayer_options
echo "	--enable-gl" >>mplayer_options
echo "	--enable-mga" >>mplayer_options
echo "	--enable-radio" >>mplayer_options
echo "	--enable-radio-capture" >>mplayer_options
echo "	%{__enable_disable sdl}" >>mplayer_options
echo "	--enable-tdfxfb" >>mplayer_options
echo "	--enable-vm" >>mplayer_options
echo "	--enable-x11" >>mplayer_options
echo "	--enable-xmga" >>mplayer_options
echo "	--enable-xv" >>mplayer_options
echo "	--enable-xvmc" >>mplayer_options
echo "	--with-xvmclib=XvMCW" >>mplayer_options
#echo "	--enable-zr" >>mplayer_options
echo "	--enable-unrarexec" >>mplayer_options
echo "	--enable-dynamic-plugins" >>mplayer_options
echo "	--enable-largefiles" >>mplayer_options
echo "	--language=all" >>mplayer_options
echo "	--codecsdir=%{_libdir}/codecs" >>mplayer_options

cat mplayer/etc/example.conf > mplayer/etc/mplayer.conf
cat <<'CONFIGADD' >> mplayer/etc/mplayer.conf

######################
# PLD Linux Defaults #
######################
[default]

# alternate solution for CP1250-encoded subtitles
fontconfig = yes
subcp = cp1250

# ...or if you prefer native bitmap fonts shipped with mplayer
#fontconfig = no
#subcp = iso-8859-1

# Standard location
unrarexec = "%{_bindir}/unrar"

CONFIGADD

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_sysconfdir}/mplayer} 

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/{mplayer,%{name}}
# default config files
#install mplayer/etc/{codecs,mplayer%{?with_osd:,menu},input}.conf $RPM_BUILD_ROOT%{_sysconfdir}/mplayer

# fonts
#cp -r font-* $RPM_BUILD_ROOT%{_datadir}/mplayer
#ln -sf font-arial-iso-8859-2/font-arial-24-iso-8859-2 $RPM_BUILD_ROOT%{_datadir}/mplayer/font

#install %{SOURCE8} $RPM_BUILD_ROOT%{_desktopdir}
#install %{SOURCE7} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
