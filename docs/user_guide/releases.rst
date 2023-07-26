.. _releases:

Releases
===============================================================================



The HDL repository is released as git branches bi-annually. 
The release branches are created first and then tested before being made official.
That is, the existence of a branch does not mean it is a fully tested release. 
Also, the release branch is tested ONLY on certain versions of the tools and 
may NOT work with other versions of the tools. The projects that are tested and
supported in a release branch are listed here along with the ADI library cores 
that are used. The branch may contain other projects that are in development, 
one must assume these are NOT tested and therefore NOT supported by this release.


Porting a release branch to another Tool version
-------------------------------------------------------------------------------

It is possible to port a release branch to another tool version, though not recommended. The ADI libraries should work across different versions of the tools, but the projects may not. The issues are most likely with the Intel and Xilinx cores. If you must still do this, note the following:

First, disable the version check of the scripts.

The ADI build scripts are making sure that the releases are being run on the validated tool version. It will promptly notify the user if he or she trying to use an unsupported version of tools. You need to disable this check by setting the environment variable ``ADI_IGNORE_VERSION_CHECK``.

Second, make Intel and Xilinx IP cores version changes.

The Intel projects should automatically be changed by Quartus. The Xilinx projects are a bit tricky. The GUI automatically updates the cores, but the TCL flow does NOT. So it may be easier to create the project file with the supported version first, then opening it with the new version. After which, update the TCL scripts accordingly.

The versions are specified in the following format.

.. code-block:: tcl
   :linenos: 

   add_instance sys_cpu altera_nios2_gen2 16.0 
   set sys_mb [create_bd_cell -type ip -vlnv xilinx.com:ip:microblaze:9.5 sys_mb] 

