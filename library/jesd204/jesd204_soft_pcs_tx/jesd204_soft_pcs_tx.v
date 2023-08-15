// ***************************************************************************
// ***************************************************************************
// Copyright (C) 2023 Analog Devices, Inc. All rights reserved.
//
// In this HDL repository, there are many different and unique modules, consisting
// of various HDL (Verilog or VHDL) components. The individual modules are
// developed independently, and may be accompanied by separate and unique license
// terms.
//
// The user should read each of these license terms, and understand the
// freedoms and responsibilities that he or she has by using this source/core.
//
// This core is distributed in the hope that it will be useful, but WITHOUT ANY
// WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
// A PARTICULAR PURPOSE.
//
// Redistribution and use of source or resulting binaries, with or without modification
// of this file, are permitted under one of the following two license terms:
//
//   1. The GNU General Public License version 2 as published by the
//      Free Software Foundation, which can be found in the top level directory
//      of this repository (LICENSE_GPL2), and also online at:
//      <https://www.gnu.org/licenses/old-licenses/gpl-2.0.html>
//
// OR
//
//   2. An ADI specific BSD license, which can be found in the top level directory
//      of this repository (LICENSE_ADIBSD), and also on-line at:
//      https://github.com/analogdevicesinc/hdl/blob/master/LICENSE_ADIBSD
//      This will allow to generate bit files and not release the source code,
//      as long as it attaches to an ADI device.
//
// ***************************************************************************
// ***************************************************************************

`timescale 1ns/100ps

module jesd204_soft_pcs_tx #(
  parameter NUM_LANES = 1,
  parameter DATA_PATH_WIDTH = 4,
  parameter INVERT_OUTPUTS = 0,
  parameter IFC_TYPE = 0
) (
  input clk,
  input reset,

  input [NUM_LANES*DATA_PATH_WIDTH*8-1:0] char,
  input [NUM_LANES*DATA_PATH_WIDTH-1:0] charisk,

  output reg [NUM_LANES*(DATA_PATH_WIDTH*10 + IFC_TYPE*40)-1:0] data
);

  reg [NUM_LANES-1:0] disparity = 'h00;

  wire [DATA_PATH_WIDTH:0] disparity_chain[0:NUM_LANES-1];
  wire [NUM_LANES*DATA_PATH_WIDTH*10-1:0] data_s;
  wire [NUM_LANES*DATA_PATH_WIDTH*10-1:0] data_inv_s;

  assign data_inv_s = INVERT_OUTPUTS ? ~data_s : data_s;

  always @(posedge clk) begin
    data <= IFC_TYPE == 0 ? data_inv_s : { // F-Tile padding
                            /* 79-60 */ 20'b0,
                            /* 59-40 */ data_inv_s[39:20],
                            /*    39 */ 1'b0,
                            /*    38 */ 1'b1,
                            /* 37-20 */ 18'b0,
                            /* 19-00 */ data_inv_s[19:0]};
  end

  generate
  genvar lane;
  genvar i;
  for (lane = 0; lane < NUM_LANES; lane = lane + 1) begin: gen_lane
    assign disparity_chain[lane][0] = disparity[lane];

    always @(posedge clk) begin
      if (reset == 1'b1) begin
        disparity[lane] <= 1'b0;
      end else begin
        disparity[lane] <= disparity_chain[lane][DATA_PATH_WIDTH];
      end
    end

    for (i = 0; i < DATA_PATH_WIDTH; i = i + 1) begin: gen_dpw
      localparam j = DATA_PATH_WIDTH * lane + i;

      jesd204_8b10b_encoder i_enc (
        .in_char(char[j*8+:8]),
        .in_charisk(charisk[j]),
        .out_char(data_s[j*10+:10]),

        .in_disparity(disparity_chain[lane][i]),
        .out_disparity(disparity_chain[lane][i+1]));
    end
  end
  endgenerate

endmodule
