#

%if %{_lib} == "lib64"
%define		_suf	64
%else
%define		_suf	32
%endif

%define		subver	rc2
%define		rel	1
Summary:	MPlayer - THE Movie Player for UN*X
Summary(de.UTF-8):	MPlayer ist ein unter der freien GPL-Lizenz stehender Media-Player
Summary(es.UTF-8):	Otro reproductor de películas
Summary(ko.UTF-8):	리눅스용 미디어플레이어
Summary(pl.UTF-8):	Odtwarzacz filmów dla systemów uniksowych
Summary(pt_BR.UTF-8):	Reprodutor de filmes
Name:		mplayer2
Version:	2.0
Release:	0.%{subver}.%{rel}
License:	GPL
Group:		Applications/Multimedia
Source0:	http://ftp.mplayer2.org/pub/release/%{name}-build-%{version}-%{subver}.tar.xz
# Source0-md5:	92793d629181e059384c43972fa9a701
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
%{?with_jack:%requires_eq	jack-audio-connection-kit-libs}
BuildRequires:	lame-libs-devel
%{?with_caca:BuildRequires:	libcaca-devel}
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
%{?with_system_vorbis:BuildRequires:	libvorbis-devel}
%{?with_x264:BuildRequires:	libx264-devel >= 0.1.3}
BuildRequires:	libxslt-progs
%{?with_lirc:BuildRequires:	lirc-devel}
%{?with_live:BuildRequires:	live-devel}
%{?with_lzo:BuildRequires:	lzo-devel >= 2.0}
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	ncurses-devel
%{?with_amr:BuildRequires:	opencore-amr-devel}
BuildRequires:	pkgconfig
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel >= 0.9}
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
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
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
%setup -q -n %{name}

echo "--prefix=%{_prefix}" >>mplayer_options
echo "--enable-runtime-cpudetection" >>mplayer_options

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
