GParted 1.4.0   (2022-03-28)
============================

Release Notes
-------------
  This release of GParted includes enhancements, bug fixes and
  language translation updates.

### Key changes include:

  * Add labelling of mounted btrfs, ext2/3/4 and xfs file systems
  * Fix detection of mount points for encrypted file systems
  * Fix crash scrolling quickly in the drive selection combobox
  * Add bcache detection
  * Add JBD external EXT3/4 journal detection

Bug Fixes
---------
  * Add labelling of mounted btrfs, ext2/3/4 and xfs file systems (#163, !87)
  * Fix detection of mount points for encrypted file systems (#162, !88)
  * Fix unmount error when unmounting below a bind mount point (!89)
  * Fix crash scrolling quickly in the drive selection combobox (#165, !91)
  * Add initial Indonesian translation of help (!90)
  * Add accessibility relations for screen readers like Orca (!92)
  * Fix partition creation at sector 2048 if partition before it (#172, !93)
  * Make more getter methods use return-by-constant-reference (!94)
  * Check copy destination instead of source (!95)
  * Add bcache detection (#183, !96)
  * Add JBD external EXT3/4 journal detection (#89, !97)
  * Fix translation of DocBook markup tag of the GParted Manual (!98)

Code Credits
------------
  Code enhancements are courtesy of Movie Ma, Pascal Engélibert, and
  Mike Fleetwood.

Translations (new/updated)
--------------------------
  cs(Marek Černocký), da(Alan Mortensen), eu(Asier Sarasua Garmendia),
  fur(Fabio Tomat), he(Yaron Shahrabani), hr(Goran Vidović),
  hu(Balázs Úr), id(Andika Triwidada), it(Milo Casagrande),
  ko(Seong-ho Cho), lt(Aurimas Černius), lv(Rūdolfs Mazurs),
  nb(Kjell Cato Heskjestad), nl(Nathan Follens), pa(A S Alam),
  pt(Hugo Carvalho), ru(Aleksandr Melman, Sergej A), sk(Dušan Kazik),
  sl(Matej Urbančič), sr(Мирослав Николић), zh_CN(Luming Zh)

Dependencies (new/updated)
--------------------------
  * n/a

Checksums
---------
### MD5SUM
    4561261a5f6fbd0c2f071953f94af670  gparted-1.4.0.tar.gz

### SHA1SUM:
    23e69c65b902a0995a892b667ea6122bf1adcee6  gparted-1.4.0.tar.gz
