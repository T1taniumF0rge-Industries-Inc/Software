GParted 1.6.0   (2024-02-26)
============================

Release Notes
-------------
  This release of GParted includes enhancements, bug fixes and
  language translation updates.

### Key changes include:

  * Stop forcing 1 MiB gap when moving partition boundary right
  * Fix crash when dealing with 0000-0000 exfat UUID
  * Remove Attempt Data Rescue and use of gpart

Bug Fixes
---------
  * Stop forcing 1 MiB gap when moving partition boundary right (#227, !112)
  * Fix GitLab CI test jobs failures on BlockSpecial unit tests (!113)
  * Fix Missing progress bar text reset when applying operation (#230, !114)
  * Fix crash when dealing with 0000-0000 exfat UUID (!115)
  * Update systemd mount masking and udev rule location (!116)
  * Require C++11 compilation (!117)
  * Remove Attempt Data Rescue and use of gpart (!118)
  * Tidy-ups for file system interface classes (!119)
  * Move appstream metadata out of legacy path (#241, !120)
  * Document future Debian/Ubuntu build time dependency in README (!121)

Code Credits
------------
  Code enhancements are courtesy of Marcin Zepp and Mike Fleetwood.

Translations (new/updated)
--------------------------
  cs(Daniel Rusek), da(Alan Mortensen), de(Jürgen Benvenuti),
  es(Daniel Mustieles), eu(Asier Sarasua Garmendia), fa(Danial Behzadi),
  fur(Fabio Tomat), ga(katerine Papava), gl(Fran Dieguez),
  he(Yosef Or Boczko), hu(Balázs Úr), id(Kukuh Syafaat),
  ie(Olga Smirnova), ka(Ekaterine Papava), kk(Baurzhan Muftakhidinov),
  lt(Aurimas Černius), pl(Piotr Drąg), pt(Hugo Carvalho),
  pt_BR(marcelocripe, Juliano de Souza Camargo), ro(Florentina Mușat),
  ru(Sergej A), sk(Dušan Kazik), sv(Anders Jonsson),
  tr(Sabri Ünal, Emin Tufan), uk(Yuri Chornoivan),
  zh_CN(Luming Zh, Boyuan Yang), zh_TW(Woodman Tuen, Cheng-Chia Tseng)

Dependencies (new/updated)
--------------------------
  * gpart is no longer needed because the "Attempt Data Rescue"
    feature has been removed.

Checksums
---------
### MD5SUM
    b2006a0a3f35853e7d7dc34c87db11f2  gparted-1.6.0.tar.gz

### SHA1SUM:
    e6e740357bcaedcf8f1b69010440328b63c35e6c  gparted-1.6.0.tar.gz
