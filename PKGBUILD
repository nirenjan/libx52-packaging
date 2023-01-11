# Maintainer: Nirenjan Krishnan <nirenjan@gmail.com>

pkgname=libx52
pkgver=0.3.0
pkgrel=3
pkgdesc="Application to control the MFD and LEDs of a Saitek X52/X52Pro HOTAS"
arch=('amd64')
url="https://github.com/nirenjan/libx52"
license=('GPL2')
depends=('libusb-1.0-0' 'libhidapi-hidraw0' 'libevdev2')
makedepends=('autoconf' 'automake' 'libtool' 'pkg-config' 'python3'
         'gettext' 'autopoint' 'libusb-1.0-0-dev' 'libhidapi-dev'
         'libevdev-dev' 'doxygen' 'libcmocka-dev')
source=("https://github.com/nirenjan/libx52/releases/download/v${pkgver}/${pkgname}_${pkgver}.orig.tar.gz")
sha256sums=('80a6141c64c94387d5593c8b4a9b5de5c22db16a0fa9cacaf1a2a80e8a3cd96e')
backup=('/etc/x52d/x52d.conf')
postinst=libx52.post.sh
postrm=libx52.post.sh

build() {
  cd ${srcdir}/${pkgname}-${pkgver}
  mkdir -p build
  cd build
  ../configure --prefix=/usr --localstatedir=/var --sysconfdir=/etc \
    --disable-silent-rules --disable-maintainer-mode
  make
}

package() {
  cd ${srcdir}/${pkgname}-${pkgver}/build

  make install DESTDIR="$pkgdir"
}
