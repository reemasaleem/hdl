.. _template_framework module:

Template Module
================================================================================

.. symbolator:: ../../../library/spi_engine/spi_engine_execution/spi_engine_execution.v
   :caption: spi_engine_execution

The {module name} is responsible for {brief description}.

Files
-------------------------------------------------------------------------------

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Name
     - Description
   * - :git-hdl:`master:library/spi_engine/spi_engine_execution/spi_engine_execution.v`
     - Verilog source for the peripheral.
   * - :git-hdl:`master:library/spi_engine/spi_engine_execution/spi_engine_execution_ip.tcl`
     - TCL script to generate the Vivado IP-integrator project for the peripheral.

Configuration Parameters
--------------------------------------------------------------------------------

.. list-table::
   :widths: 15 80 5
   :header-rows: 1

   * - Name
     - Description
     - Default
   * - ``DATA_WIDTH``
     - Data width of the parallel data stream. Supported values: 8/16/24/32
     - 8

Signal and Interface Pins
--------------------------------------------------------------------------------

.. list-table::
   :widths: 10 25 65
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``clk``
     - Clock
     - All other signals are synchronous to this clock.
   * - ``resetn``
     - Synchronous active-low reset
     - Resets the internal state machine of the core.
   * - ``ctrl``
     - :ref:`template_framework interface` master
     - {brief description}.

Theory of Operation
--------------------------------------------------------------------------------

The {module name}  module implements {brief description}.

.. image:: ../spi_engine/spi_engine.svg
