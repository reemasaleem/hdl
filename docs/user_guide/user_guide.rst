HDL User Guide
===============================================================================

Analog Devices provides FPGA reference designs for selected hardware featuring 
some of our products interfacing to publicly available FPGA evaluation boards. 
This wiki page details the HDL resources of these reference designs.

A list of supported hardware can be found at:
- Intel (intel_reference_designs)
- Xilinx (xilinx_reference_designs)

Projects list
--------------------------------------------------------------------------------

By carrier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :header-rows: 1

   * - Carrier
     - Add-on board
     - Source
     - Project doc
     - HDL doc
     - Linux device driver
   * - a10soc
     - ad9081_fmca_ebz
     - TBD
   * - Xilinx Artix 7
     - TBD
     - TBD
   * - Xilinx Kintex 7
     - TBD
     - TBD
   * - Xilinx Virtex 7
     - TBD
     - TBD


Sizing of the internal store-and-forward data buffer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AXI-Streaming slave
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
- Supports multiple interface types

  -  AXI3/4 memory mapped
  -  AXI4 Streaming
  -  ADI FIFO interface

- Zero-latency transfer switch-over architecture

  -  Allows **continuous** high-speed streaming

- Cyclic transfers
- 2D transfers

