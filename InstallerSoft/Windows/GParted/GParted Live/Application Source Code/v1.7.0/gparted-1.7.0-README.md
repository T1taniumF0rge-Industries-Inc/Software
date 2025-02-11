GParted 1.7.0   (2025-01-30)
============================

Release Notes
-------------
  This release of GParted includes enhancements, bug fixes and
  language translation updates.

### Key changes include:

  * Recognise NBDs (Network Block Devices)
  * Add support for Bcachefs (experimental), single device file systems only
  * Prevent GParted probe starting LVM Volume Groups
  * Increase minimum required version of libparted to 3.2 (!131)

Bug Fixes
---------
  * Recognise NBDs (Network Block Devices) (#247, !122)
  * Update CI jobs for Ubuntu 24.04 LTS and use Rocky Linux 8 (!124)
  * Read exFAT file system usage from exfatprogs >= 1.2.3 (#261, !125)
  * Fix serial number for my USB key showing binary data (#263, !126)
  * Add support for Bcachefs, single device file systems only (#234, !123)
  * Prevent GParted probe starting LVM Volume Groups (#259, !127)
  * Fix hang searching partitions when btrfs-progs not installed (#271, !130)
  * Increase minimum required version of libparted to 3.2 (!131)

Code Credits
------------
  Code enhancements are courtesy of Mike Fleetwood.

Translations (new/updated)
--------------------------
  be(Yuras Shumovich, Vasil Pupkin), cs(Daniel Rusek),
  da(Alan Mortensen), de(Jürgen Benvenuti), he(Yaron Shahrabani),
  hi(Scrambled 777), hu(Balázs Úr), ka(Ekaterine Papava),
  lt(Aurimas Černius), lv(Rūdolfs Mazurs), pl(Piotr Drąg),
  pt(Hugo Carvalho), pt_BR(Rafael Fontenelle), ro(Daniel Șerbănescu),
  ru(Sergej A.), sl(Martin Srebotnjak), sr(Мирослав Николић),
  sv(Anders Jonsson), uk(Yuri Chornoivan), zh_CN(Luming Zh)

Dependencies (new/updated)
--------------------------
  * n/a

Checksums
---------
### MD5SUM
    97305db7509dd1bf2456a1331d2380f3  gparted-1.7.0.tar.gz

### SHA1SUM:
    7e548c742b1516c4bb0328df0db4eac521b699cf  gparted-1.7.0.tar.gz
