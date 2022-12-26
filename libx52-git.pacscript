# Maintainer: Nirenjan Krishnan <nirenjan@gmail.com>

name=libx52-git
pkgname=libx52
url="https://github.com/nirenjan/${pkgname}.git"
description="Application to control the MFD and LEDs of a Saitek X52/X52Pro HOTAS"
maintainer="Nirenjan Krishnan <nirenjan@gmail.com>"
breaks=libx52
depends="libusb-1.0-0 libhidapi-hidraw0 libevdev2"
build_depends="autoconf automake libtool pkg-config python3 gettext autopoint libusb-1.0-0-dev libhidapi-dev libevdev-dev doxygen libcmocka-dev git"

pkgver() {
    git ls-remote "$url" master | cut -f1
}

prepare() {
    ./autogen.sh
}

build() {
    ./configure
    make -j$(nproc) V=0
}

install() {
    sudo make install DESTDIR="${STOWDIR}/${name}" SKIP_UDEV=true
}

postinst() {
    if command -v udevadm >/dev/null
    then
        sudo udevadm control --reload-rules
        sudo udevadm trigger --subsystem-match=usb --attr-match=idVendor=06a3 --action=add
    fi
}
