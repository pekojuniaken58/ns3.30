APPNAME = 'ns'
AR = ['/usr/bin/ar']
ARFLAGS = ['rcs']
BINDIR = '/usr/local/bin'
BOOST_VERSION = '1_65_1'
BUILD_PROFILE = 'debug'
BUILD_SUFFIX = '-debug'
CC = ['/usr/bin/gcc']
CCDEFINES = ['_DEBUG']
CCFLAGS = ['-O0', '-ggdb', '-g3', '-Wall', '-Werror', '-O0', '-ggdb', '-g3', '-Wall', '-Werror', '-std=c++11', '-frounding-math', '-fstrict-aliasing', '-Wstrict-aliasing']
CCFLAGS_PTHREAD = '-pthread'
CCFLAGS_PYEXT = ['-fvisibility=hidden']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('7', '5', '0')
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_PYEMBED = ['-g', '-fdebug-prefix-map=/build/python3.6-XokORh/python3.6-3.6.9=.', '-fstack-protector', '-g', '-fwrapv', '-O3']
CFLAGS_PYEXT = ['-g', '-fdebug-prefix-map=/build/python3.6-XokORh/python3.6-3.6.9=.', '-fstack-protector', '-g', '-fwrapv', '-O3']
CFLAGS_cshlib = ['-fPIC']
COMPILER_CC = 'gcc'
COMPILER_CXX = 'g++'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/g++']
CXXDEFINES = ['_DEBUG']
CXXFLAGS = ['-O0', '-ggdb', '-g3', '-Wall', '-Werror', '-std=c++11', '-frounding-math', '-fstrict-aliasing', '-Wstrict-aliasing']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_PTHREAD = '-pthread'
CXXFLAGS_PYEMBED = ['-g', '-fdebug-prefix-map=/build/python3.6-XokORh/python3.6-3.6.9=.', '-fstack-protector', '-g', '-fwrapv', '-O3']
CXXFLAGS_PYEXT = ['-g', '-fdebug-prefix-map=/build/python3.6-XokORh/python3.6-3.6.9=.', '-fstack-protector', '-g', '-fwrapv', '-O3', '-fvisibility=hidden', '-Wno-array-bounds']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DATADIR = '/usr/local/share'
DATAROOTDIR = '/usr/local/share'
DEFINES = ['NS3_BUILD_PROFILE_DEBUG', 'NS3_ASSERT_ENABLE', 'NS3_LOG_ENABLE', 'HAVE_SYS_IOCTL_H=1', 'HAVE_IF_NETS_H=1', 'HAVE_NET_ETHERNET_H=1', 'HAVE_PACKET_H=1', 'HAVE_SQLITE3=1', 'HAVE_IF_TUN_H=1', 'HAVE_GSL=1']
DEFINES_PYEMBED = ['NDEBUG']
DEFINES_PYEXT = ['NDEBUG']
DEFINES_ST = '-D%s'
DEFINE_COMMENTS = {'PYTHONDIR': '', 'PYTHONARCHDIR': '', 'HAVE_PYEMBED': '', 'HAVE_PYEXT': '', 'HAVE_PYTHON_H': '', 'HAVE_LIBXML2': '', 'HAVE_UINT128_T': '', 'HAVE___UINT128_T': '', 'INT64X64_USE_128': '', 'HAVE_STDINT_H': '', 'HAVE_INTTYPES_H': '', 'HAVE_SYS_INT_TYPES_H': '', 'HAVE_SYS_TYPES_H': '', 'HAVE_SYS_STAT_H': '', 'HAVE_DIRENT_H': '', 'HAVE_STDLIB_H': '', 'HAVE_GETENV': '', 'HAVE_SIGNAL_H': '', 'HAVE_PTHREAD_H': '', 'HAVE_RT': '', 'HAVE_SYS_IOCTL_H': '', 'HAVE_IF_NETS_H': '', 'HAVE_NET_ETHERNET_H': '', 'HAVE_IF_TUN_H': '', 'HAVE_PACKET_H': '', 'HAVE_SQLITE3': '', 'HAVE_GSL': ''}
DEST_BINFMT = 'elf'
DEST_CPU = 'x86_64'
DEST_OS = 'linux'
DOCDIR = '/usr/local/share/doc/ns'
DOXYGEN = ['/usr/bin/doxygen']
DVIDIR = '/usr/local/share/doc/ns'
ENABLE_BRITE = False
ENABLE_EMU = True
ENABLE_EXAMPLES = False
ENABLE_FDNETDEV = True
ENABLE_GSL = '-lgsl -lgslcblas -lm\n'
ENABLE_GTK = None
ENABLE_LIBXML2 = '-I/usr/include/libxml2 -lxml2\n'
ENABLE_NSC = False
ENABLE_PYTHON_BINDINGS = True
ENABLE_PYVIZ = True
ENABLE_REAL_TIME = True
ENABLE_STATIC_NS3 = False
ENABLE_SUDO = False
ENABLE_TAP = True
ENABLE_TESTS = False
ENABLE_THREADING = True
EXAMPLE_DIRECTORIES = ['traffic-control', 'tutorial', 'realtime', 'routing', 'udp', 'matrix-topology', 'stats', 'ipv6', 'udp-client-server', 'tcp', 'naming', 'socket', 'wireless', 'error-model', 'energy']
EXEC_PREFIX = '/usr/local'
GCC_RTTI_ABI_COMPLETE = 'True'
HAVE_DIRENT_H = 1
HAVE_GSL = 1
HAVE_INTTYPES_H = 1
HAVE_LIBXML2 = 1
HAVE_LINUX_IF_TUN_H = 1
HAVE_NETPACKET_PACKET_H = 1
HAVE_NET_ETHERNET_H = 1
HAVE_NET_IF_H = 1
HAVE_PTHREAD_H = 1
HAVE_PYEMBED = 1
HAVE_PYEXT = 1
HAVE_PYTHON_H = 1
HAVE_RT = 1
HAVE_SIGNAL_H = 1
HAVE_SQLITE3 = 1
HAVE_STDINT_H = 1
HAVE_STDLIB_H = 1
HAVE_SYS_IOCTL_H = 1
HAVE_SYS_STAT_H = 1
HAVE_SYS_TYPES_H = 1
HAVE___UINT128_T = 1
HTMLDIR = '/usr/local/share/doc/ns'
INCLUDEDIR = '/usr/local/include'
INCLUDES_BOOST = '/usr/include'
INCLUDES_LIBXML2 = ['/usr/include/libxml2']
INCLUDES_PYEMBED = ['/usr/include/python3.6m']
INCLUDES_PYEXT = ['/usr/include/python3.6m']
INFODIR = '/usr/local/share/info'
INT64X64_USE_128 = 1
LIB = ['CGAL', 'CGAL_Core', 'gmp', 'mpfr', 'boost_thread']
LIBDIR = '/usr/local/lib'
LIBEXECDIR = '/usr/local/libexec'
LIBPATH_BOOST = ['/usr/lib/x86_64-linux-gnu']
LIBPATH_PYEMBED = ['/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu', '/usr/lib']
LIBPATH_PYEXT = ['/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu', '/usr/lib']
LIBPATH_ST = '-L%s'
LIB_BOOST = ['boost_system', 'boost_signals', 'boost_filesystem']
LIB_GSL = ['gsl', 'gslcblas', 'm']
LIB_LIBXML2 = ['xml2']
LIB_PYEMBED = ['python3.6m', 'pthread', 'dl', 'util', 'm', 'python3.6m', 'pthread', 'dl', 'util', 'm']
LIB_PYEXT = ['python3.6m', 'pthread', 'dl', 'util', 'm', 'python3.6m', 'pthread', 'dl', 'util', 'm']
LIB_RT = ['rt']
LIB_SQLITE3 = ['sqlite3']
LIB_ST = '-l%s'
LINKFLAGS = ['-L/usr/lib', '-L/usr/lib/x86_64-linux-gnu']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_PTHREAD = '-pthread'
LINKFLAGS_PYEMBED = ['-Xlinker', '-export-dynamic', '-Wl,-O1', '-Wl,-Bsymbolic-functions']
LINKFLAGS_PYEXT = ['-Xlinker', '-export-dynamic', '-Wl,-O1', '-Wl,-Bsymbolic-functions']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINKFLAGS_cxxshlib = ['-shared']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CC = ['/usr/bin/gcc']
LINK_CXX = ['/usr/bin/g++']
LOCALEDIR = '/usr/local/share/locale'
LOCALSTATEDIR = '/usr/local/var'
MANDIR = '/usr/local/share/man'
MODULES_NOT_BUILT = ['brite', 'click', 'openflow']
NS3_CONTRIBUTED_MODULES = []
NS3_ENABLED_CONTRIBUTED_MODULES = []
NS3_ENABLED_MODULES = ['ns3-antenna', 'ns3-aodv', 'ns3-applications', 'ns3-bridge', 'ns3-buildings', 'ns3-config-store', 'ns3-core', 'ns3-csma', 'ns3-csma-layout', 'ns3-dsdv', 'ns3-dsr', 'ns3-energy', 'ns3-fd-net-device', 'ns3-flow-monitor', 'ns3-hirai', 'ns3-internet', 'ns3-internet-apps', 'ns3-jbr', 'ns3-lively', 'ns3-lowbattery', 'ns3-lr-wpan', 'ns3-lsgo', 'ns3-lte', 'ns3-mesh', 'ns3-mobility', 'ns3-mpi', 'ns3-nearest', 'ns3-netanim', 'ns3-network', 'ns3-nix-vector-routing', 'ns3-obstacle', 'ns3-olsr', 'ns3-point-to-point', 'ns3-point-to-point-layout', 'ns3-propagation', 'ns3-sample', 'ns3-shutoushu', 'ns3-sigo', 'ns3-sixlowpan', 'ns3-spectrum', 'ns3-stats', 'ns3-tap-bridge', 'ns3-test', 'ns3-topology-read', 'ns3-traffic-control', 'ns3-uan', 'ns3-virtual-net-device', 'ns3-visualizer', 'ns3-wave', 'ns3-wifi', 'ns3-wimax']
NS3_EXECUTABLE_PATH = ['/home/nsl-ubu/ns-3-allinone/ns3.30/build/src/fd-net-device', '/home/nsl-ubu/ns-3-allinone/ns3.30/build/src/tap-bridge']
NS3_MODULES = ['ns3-antenna', 'ns3-aodv', 'ns3-applications', 'ns3-bridge', 'ns3-buildings', 'ns3-config-store', 'ns3-core', 'ns3-csma', 'ns3-csma-layout', 'ns3-dsdv', 'ns3-dsr', 'ns3-energy', 'ns3-fd-net-device', 'ns3-flow-monitor', 'ns3-hirai', 'ns3-internet', 'ns3-internet-apps', 'ns3-jbr', 'ns3-lively', 'ns3-lowbattery', 'ns3-lr-wpan', 'ns3-lsgo', 'ns3-lte', 'ns3-mesh', 'ns3-mobility', 'ns3-mpi', 'ns3-nearest', 'ns3-netanim', 'ns3-network', 'ns3-nix-vector-routing', 'ns3-obstacle', 'ns3-olsr', 'ns3-point-to-point', 'ns3-point-to-point-layout', 'ns3-propagation', 'ns3-sample', 'ns3-shutoushu', 'ns3-sigo', 'ns3-sixlowpan', 'ns3-spectrum', 'ns3-stats', 'ns3-tap-bridge', 'ns3-test', 'ns3-topology-read', 'ns3-traffic-control', 'ns3-uan', 'ns3-virtual-net-device', 'ns3-visualizer', 'ns3-wave', 'ns3-wifi', 'ns3-wimax']
NS3_MODULE_PATH = ['/usr/lib/gcc/x86_64-linux-gnu/7', '/home/nsl-ubu/ns-3-allinone/ns3.30/build/lib']
NS3_OPTIONAL_FEATURES = [('python', 'Python Bindings', True, None), ('castxml', 'Python API Scanning Support', False, "Missing 'pygccxml' Python module"), ('brite', 'BRITE Integration', False, 'BRITE not enabled (see option --with-brite)'), ('nsclick', 'NS-3 Click Integration', False, 'nsclick not enabled (see option --with-nsclick)'), ('GtkConfigStore', 'GtkConfigStore', [], "library 'gtk+-3.0 >= 3.0' not found"), ('XmlIo', 'XmlIo', '-I/usr/include/libxml2 -lxml2\n', "library 'libxml-2.0 >= 2.7' not found"), ('Threading', 'Threading Primitives', True, '<pthread.h> include not detected'), ('RealTime', 'Real Time Simulator', True, 'threading not enabled'), ('FdNetDevice', 'File descriptor NetDevice', True, 'FdNetDevice module enabled'), ('TapFdNetDevice', 'Tap FdNetDevice', True, 'Tap support enabled'), ('EmuFdNetDevice', 'Emulation FdNetDevice', True, 'Emulation support enabled'), ('PlanetLabFdNetDevice', 'PlanetLab FdNetDevice', False, 'PlanetLab operating system not detected (see option --force-planetlab)'), ('nsc', 'Network Simulation Cradle', False, 'NSC not found (see option --with-nsc)'), ('mpi', 'MPI Support', False, 'option --enable-mpi not selected'), ('openflow', 'NS-3 OpenFlow Integration', False, 'OpenFlow not enabled (see option --with-openflow)'), ('SqliteDataOutput', 'SQlite stats data output', '-lsqlite3\n', "library 'sqlite3' not found"), ('TapBridge', 'Tap Bridge', True, '<linux/if_tun.h> include not detected'), ('PyViz', 'PyViz visualizer', True, None), ('ENABLE_SUDO', 'Use sudo to set suid bit', False, 'option --enable-sudo not selected'), ('ENABLE_TESTS', 'Tests', False, 'defaults to disabled'), ('ENABLE_EXAMPLES', 'Examples', False, 'defaults to disabled'), ('GSL', 'GNU Scientific Library (GSL)', '-lgsl -lgslcblas -lm\n', 'GSL not found'), ('libgcrypt', 'Gcrypt library', [], 'libgcrypt not found: you can use libgcrypt-config to find its location.'), ('DES Metrics', 'DES Metrics event collection', [], 'defaults to disabled')]
OLDINCLUDEDIR = '/usr/include'
PACKAGE = 'ns'
PDFDIR = '/usr/local/share/doc/ns'
PKGCONFIG = ['/usr/bin/pkg-config']
PLATFORM = 'linux'
PREFIX = '/usr/local'
PRINT_BUILT_MODULES_AT_END = False
PSDIR = '/usr/local/share/doc/ns'
PYC = 1
PYFLAGS = ''
PYFLAGS_OPT = '-O'
PYO = 1
PYTAG = 'cpython-36'
PYTHON = ['/usr/bin/python3']
PYTHONARCHDIR = '/usr/local/lib/python3/dist-packages'
PYTHONDIR = '/usr/local/lib/python3/dist-packages'
PYTHON_BINDINGS_APIDEFS = 'gcc-LP64'
PYTHON_CONFIG = ['/usr/bin/python3-config']
PYTHON_VERSION = '3.6'
REQUIRED_BOOST_LIBS = ['system', 'signals', 'filesystem']
RPATH_ST = '-Wl,-rpath,%s'
SBINDIR = '/usr/local/sbin'
SHAREDSTATEDIR = '/usr/local/com'
SHLIB_MARKER = '-Wl,-Bdynamic'
SONAME_ST = '-Wl,-h,%s'
SQLITE_STATS = '-lsqlite3\n'
STLIBPATH_BOOST = ['/usr/lib/x86_64-linux-gnu']
STLIBPATH_ST = '-L%s'
STLIB_BOOST = []
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
SUDO = ['/usr/bin/sudo']
SYSCONFDIR = '/usr/local/etc'
VALGRIND_FOUND = False
VERSION = '3-dev'
WITH_PYBINDGEN = '/home/nsl-ubu/ns-3-allinone/pybindgen'
WL_SONAME_SUPPORTED = True
cfg_files = ['/home/nsl-ubu/ns-3-allinone/ns3.30/build/ns3/config-store-config.h', '/home/nsl-ubu/ns-3-allinone/ns3.30/build/ns3/core-config.h']
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.so'
cxxstlib_PATTERN = 'lib%s.a'
define_key = ['HAVE_SYS_IOCTL_H', 'HAVE_IF_NETS_H', 'HAVE_NET_ETHERNET_H', 'HAVE_IF_TUN_H', 'HAVE_PACKET_H', 'HAVE_SQLITE3', 'HAVE_GSL']
macbundle_PATTERN = '%s.bundle'
pyext_PATTERN = '%s.cpython-36m-x86_64-linux-gnu.so'
