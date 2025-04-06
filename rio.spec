Name:           rio
Version:        0.2.12
Release:        1
URL:            https://github.com/raphamorim/rio
Source0:        https://github.com/raphamorim/rio/archive/refs/tags/v%{version}.tar.gz
Summary:        A hardware-accelerated GPU terminal emulator powered by WebGPU
License:        MIT
BuildRequires:  rustc
BuildRequires:  pkg-config
BuildRequires:  libxcb-dev
BuildRequires:  freetype-dev
BuildRequires:  xclip
BuildRequires:  fontconfig-dev
BuildRequires:  mesa-dev
BuildRequires:  libxkbcommon-dev
BuildRequires:  ncurses-dev
BuildRequires:  expat-dev
BuildRequires:  python3

 
%description
A hardware-accelerated GPU terminal emulator powered by WebGPU.

%prep
%setup -q -n rio-%{version}

%build
unset http_proxy https_proxy no_proxy
export RUSTFLAGS="$RUSTFLAGS -C target-cpu=westmere -C target-feature=+avx -C opt-level=3 -C codegen-units=1 -C panic=abort -Clink-arg=-Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code "
cargo build --release --all-features


%install
install -D -m755 target/release/rio %{buildroot}/usr/bin/rio
install -m644 misc/rio.desktop -pD %{buildroot}/usr/share/applications/rio.desktop
install -m644 docs/static/assets/rio-logo.svg -pD %{buildroot}/usr/share/icons/hicolor/scalable/apps/rio.svg
strip %{buildroot}/usr/bin/rio

%files
%defattr(-,root,root,-)
/usr/bin/rio
/usr/share/applications/rio.desktop
/usr/share/icons/hicolor/scalable/apps/rio.svg
