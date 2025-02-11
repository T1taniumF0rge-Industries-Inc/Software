This is GParted live 1.6.0-10
=============================

Release Notes
-------------
  * The underlying GNU/Linux operating system was upgraded. 
    This release is based on the Debian Sid repository (as of 2024/Sep/28).
  * Linux kernel was updated to 6.10.11-1.
  * Package pm-utils is included now. Thanks to Nono for this suggestion.
  * Removed package cpufrequtils from lists of live system.
    It's not in the Debian repo anymore.
  * Force to use zenity as the dialog in GParted live's program gl-screenshot.
    No more using gdialog or Xdialog since they are not available in Debian
    repo.
    Ref: https://gitlab.gnome.org/GNOME/gparted/-/issues/256


### MD5SUMS:
93e369a86a992e19fe55b9bd23d1981d  gparted-live-1.6.0-10-amd64.iso
47539eb4c5316cff9003a2d944a599a6  gparted-live-1.6.0-10-i686.iso
ba3d2b2cdf97ea1b8634711869728d64  gparted-live-1.6.0-10-i686-pae.iso
8d77ba5dac3b0af87d2d5d435ca69165  gparted-live-1.6.0-10-amd64.zip
18261905b1f437aeeca7bd00698cdcc2  gparted-live-1.6.0-10-i686-pae.zip
b87ae5498bcbcc38ca02dcad7a1e6501  gparted-live-1.6.0-10-i686.zip

### SHA1SUMS:
5096694ef1c4165fc6d64aa48661b1c618be04e9  gparted-live-1.6.0-10-amd64.iso
6f9c7c296d9fce69cea3a7c41b2cb7300123bf87  gparted-live-1.6.0-10-i686.iso
710e7bc46df1d83686682a6460253350127cd3f7  gparted-live-1.6.0-10-i686-pae.iso
91b8ef761239ed9776b93eccbf2aba7c757b79e5  gparted-live-1.6.0-10-amd64.zip
3822d1424d779b9e4d13d55ec1edd74657196476  gparted-live-1.6.0-10-i686-pae.zip
8edc06fdbaaf3a10ab17a9bbd87a30c168bfa8f8  gparted-live-1.6.0-10-i686.zip

### SHA256SUMS:
f2cb819cffa1b7d0f72852785566aee3d76146950a5c70b78a34b45e29e66be9  gparted-live-1.6.0-10-amd64.iso
f1ba563b917ac8f5ac1cfa90cd3fe1bd1d9b3a91ab8e9c8ef6af20f3eab88950  gparted-live-1.6.0-10-i686.iso
b73874adecc8f2729a658ddf312a491c0ab62a8ab0f764e784642ca669fc7afe  gparted-live-1.6.0-10-i686-pae.iso
3d375a2184fd8a5458de1455576b30cabb30f9994a8911f94c59e46171d3b464  gparted-live-1.6.0-10-amd64.zip
19d934429c3b7fc824f34d31b144630646107d4bbcf4784cad1556239f67e521  gparted-live-1.6.0-10-i686-pae.zip
0d1f8c27775a4a658c716acd3c5a5a020136ffb92d05b782518bd7400258ec0b  gparted-live-1.6.0-10-i686.zip

### SHA512SUMS:
8e1dec46c83715c60c0ffd0d936e5a6618f9e69f497da7b26ec4b6e022a9b2e6ac54fcc2b29d273f338c4db697c6b876daf17e11661ddb1f54929e613598c331  gparted-live-1.6.0-10-amd64.iso
60c5b0bb1672eb519478e772c8278a2491dce2ab6f335999837cedbd26fbe8433366af6c836917a038f576e4a79b6fe85b59761e6ad083b59a2fd86e071c254a  gparted-live-1.6.0-10-i686.iso
81253f4ed372f647a341b8c2df8c33eded0500e3a19be5727923a6cb0bbc98a67616640e0f7f2482b5f4b661b440229be93fa1af84c5c7979f574372e0bed2a6  gparted-live-1.6.0-10-i686-pae.iso
50984df91d2398d7a748f1f6fb2b62e3adbda574436c9ccebe51044d9a3e7f6159ac84f47627f7d689215f6e2fdf43499db09bfa11cc4c5182d64ad08186de8b  gparted-live-1.6.0-10-amd64.zip
46da68c0318515462f77e96f0715c795b211ece268a279ec1e999e472bd8ac814a55ba75dd984f21bf9949e2eb4abec2554052dbc521ca4e2581ac19a9c191ba  gparted-live-1.6.0-10-i686-pae.zip
8ffa4b430ade2d235170da7a784a11a650f9c21874c0b97df02aac12cdcbf453d71c1d9e1395b4df2cba93c7c433fedf031a844b80501c03d05b341c53609ace  gparted-live-1.6.0-10-i686.zip

### B2SUMS:
76fd79c6f19274ecb35f4137949ed25f15fd9d1a7f029645f576466282d829cbf7a3b28dd5629ba9185a99b960973ded9926d8933474f20cbe5c12546b4719da  gparted-live-1.6.0-10-amd64.iso
0ade9fe00f128a37c1b1831aa5457263de1f6315b48e587e139f95c4a8492c3254d989a4836c7553d64fb2eba8b93254c0f1c2d7f3e5a65f42d3430b7b4adb8c  gparted-live-1.6.0-10-i686.iso
f4e5968ee9fd573eae55c8861c40aa88924a5fe95d4de53c116a814eca5a1b79d49350b67ce5e1ad66d48781d14a1536cd3c8a0e3f8faeaed594984cca1f303a  gparted-live-1.6.0-10-i686-pae.iso
72fcca9c3600a6918e1deaf6fb7eccc988aa7869f9925fec59cc408f0d2ba44b2289e1292ad04632ab69099ca03dfad007903f39fb1204e26aefdf3759861540  gparted-live-1.6.0-10-amd64.zip
0f0bfd25a7a61a249fefcddf8981930f0bae9d7e18dd602e1da9deb9fd5e3393f1d1b653e5379210d2986d79898c88c7a83171a795973e40f43ff261c137047e  gparted-live-1.6.0-10-i686-pae.zip
d4dcad5624e419297778f2e3ae616287e20faaf7a9b065876cfd90f27686329dc79a5db6f3e6773f51b089bb0f927461c13fc3842a86f38af7235b3582c7c4f4  gparted-live-1.6.0-10-i686.zip
