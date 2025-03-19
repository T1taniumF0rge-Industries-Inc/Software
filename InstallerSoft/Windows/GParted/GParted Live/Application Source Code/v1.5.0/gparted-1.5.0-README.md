GParted 1.5.0   (2023-02-21)
============================

Release Notes
-------------
  This release of GParted includes enhancements, bug fixes and
  language translation updates.

### Key changes include:

  * Fix path used to resize btrfs needs to be a directory
  * Fix crash when copying NTFS to starting beyond 2 TiB
  * Enable repair when checking exfat file systems

Bug Fixes
---------
  * Fix undeclared identifier 'basename' build failure with musl libc (!99)
  * Fix NULL == 0 assumption in call to ped_partition_flag_next() (!100)
  * Fix path used to resize btrfs needs to be a directory (#193, !102)
  * Fix make distcheck failure found in GitLab CI job unbuntu_test (!103)
  * Add Alpine Linux CI jobs and resolve FAT16/32 label and UUID issues (!104)
  * Update used btrfs file system commands, btrfs-progs 4.5 required (!105)
  * Update AC_PROG_LIBTOOL to LT_INIT in configure.ac (!106)
  * Migrate from intltool to gettext translation (!107)
  * Fix crash when copying NTFS to starting beyond 2 TiB (#164, !108)
  * Enable repair when checking exfat file systems (!109)
  * Increase minimum XFS size to 300 MiB (#217, !110)
  * Erase all Promise FastTrack RAID signatures (#220, !111)

Code Credits
------------
  Code enhancements are courtesy of Markus Volk, Dominika Liberda and
  Mike Fleetwood.

Translations (new/updated)
--------------------------
  ca(Jordi Mas), da(Alan Mortensen), de(Jürgen Benvenuti),
  fr(Irénée Thirion), he(Yaron Shahrabani, Yosef Or Boczko),
  hr(Goran Vidović), hu(Balázs Úr), id(Andika Triwidada, Kukuh Syafaat),
  ka(Temuri Doghonadze, Zurab Kargareteli), ko(Seong-ho Cho),
  nl(Nathan Follens), pl(Piotr Drąg), pt(Hugo Carvalho),
  pt_BR(Rafael Fontenelle, Enrico Nicoletto), ru(Aleksandr Melman, Sergej A),
  sk(Dušan Kazik), sl(Matej Urbančič), sr(Мирослав Николић),
  sv(Anders Jonsson, Luna Jernberg), tr(Sabri Ünal, Muhammet Kara),
  uk(Yuri Chornoivan)

Dependencies (new/updated)
--------------------------
  * btrfs-progs >= 4.5 package is required for btrfs file system support.

Checksums
---------
### MD5SUM
    9adbd4b1cbcb7a7c76dcc0e9ffed9a7c  gparted-1.5.0.tar.gz

### SHA1SUM:
    e5f841eef14d005d8e4c30aa453a11a04d49d26d  gparted-1.5.0.tar.gz
