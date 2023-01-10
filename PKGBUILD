# Maintainer: Nirenjan Krishnan <nirenjan@gmail.com>

pkgname=libx52-git
_gitname=libx52
pkgver=0.3.0.3.gd3973a0
pkgrel=git
pkgdesc="Application to control the MFD and LEDs of a Saitek X52/X52Pro HOTAS"
arch=('amd64')
url="https://github.com/nirenjan/libx52"
license=('GPL2')
depends=('libusb-1.0-0' 'libhidapi-hidraw0' 'libevdev2')
makedepends=('autoconf' 'automake' 'libtool' 'pkg-config' 'python3'
         'gettext' 'autopoint' 'libusb-1.0-0-dev' 'libhidapi-dev'
         'libevdev-dev' 'doxygen' 'libcmocka-dev' 'git')
postinst=libx52.post.sh
postrm=libx52.post.sh
provides=('libx52')
conflicts=('libx52')

prepare() {
    cd ${srcdir}
    if [ ! -d "${_gitname}" ]; then
        git clone "${url}.git" -b master
    else
        git -C "${_gitname}" pull
        rm -rf ${srcdir}/${_gitname}/build
    fi
}

pkgver() {
    cd ${srcdir}/${_gitname}
    git describe 2>/dev/null | sed -e 's/^v//' -e 's/-/./g'
}

build() {
  cd ${srcdir}/${_gitname}
  ./autogen.sh
  ./configure --prefix=/usr --localstatedir=/var --sysconfdir=/etc \
    --disable-silent-rules --disable-maintainer-mode
  make
}

package() {
  cd ${srcdir}/${_gitname} #/build

  make install DESTDIR="$pkgdir"
}
