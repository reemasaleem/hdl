.. _introduction:

Introduction
===============================================================================

.. toctree::
   :hidden:

   AMD Xilinx<xilinx_ref_designs>
   Intel<intel_ref_designs>

ADI provides FPGA reference designs for selected hardware featuring some of our
products interfacing to publicly available FPGA evaluation boards.
This wiki documentation details the HDL resources of these reference designs.

A list of supported hardware can be found here:

About this guide
-------------------------------------------------------------------------------
The main purpose of this user guide is to help you understand and use (modify
or otherwise) the HDL resources provided by Analog Devices and to provide
advice and instructions for using these resources. After reading this guide,
the user should be able to build a specific project from the HDL repository and
be able to modify (if so desire) the digital data path implemented in the FPGA.
Furthermore all ADI developed and supported IP is presented in detail.

At the same time, this user guide does not intend to be a guide for any third
party tool. To understand and use the HDL framework efficiently the user needs
to have a solid understanding how an FPGA works and needs to be familiar with
all the design tools and flows. FPGA's and SoC's are highly complex systems,
we do not have the time and place to cover every feature and aspect of it.

If somebody does not have this knowledge we highly recommend to make some
general research and go through some basic tutorials with her targeted
development platform. There can be found a lot of information and documentation
at vendor's support pages:

* `AMD Xilinx support`_
* `Intel support`_

Location of the sources
-------------------------------------------------------------------------------
All the HDL sources can be found at Analog Devices Inc. `GitHub repository`_.
Later in this guide, the structure of this repository will be presented.


.. _AMD Xilinx support: https://www.xilinx.com/support.html

.. _Intel support: https://www.intel.com/content/www/us/en/programmable/support/support-resources.html

.. _GitHub repository: https://github.com/analogdevicesinc
