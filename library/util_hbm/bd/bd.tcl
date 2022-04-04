proc init {cellpath otherInfo} {
  set ip [get_bd_cells $cellpath]
}

# Executed when you close the config window
proc post_config_ip {cellpath otherinfo} {
  set ip [get_bd_cells $cellpath]

  # Update AXI interface properties according to configuration
  set axi_protocol [get_property "CONFIG.AXI_PROTOCOL" $ip]
  set data_width [get_property "CONFIG.AXI_DATA_WIDTH" $ip]

  # <TODO>: Make this depend on FIFO_SIZE parameter
  set fifo_size 8

  if {$axi_protocol == 0} {
    set axi_protocol_str "AXI4"
    set max_beats_per_burst 256
  } else {
    set axi_protocol_str "AXI3"
    set max_beats_per_burst 16
  }

  set num_m [get_property "CONFIG.NUM_M" $ip]
  for {set idx 0} {$idx < $num_m} {incr idx} {

    set intf [get_bd_intf_pins [format "%s/MAXI_%d" $cellpath $idx]]

    set_property CONFIG.PROTOCOL $axi_protocol_str $intf
    set_property CONFIG.MAX_BURST_LENGTH $max_beats_per_burst $intf

    set_property CONFIG.NUM_WRITE_OUTSTANDING $fifo_size $intf
    set_property CONFIG.NUM_READ_OUTSTANDING  $fifo_size $intf

  }

  # For multi master configurations (e.g.HBM) the AXIS data widths must match
  if { $num_m > 1} {
    set src_width [get_property "CONFIG.SRC_DATA_WIDTH" $ip]
    set dst_width [get_property "CONFIG.DST_DATA_WIDTH" $ip]
    if {$src_width != $dst_width} {
      bd::send_msg -of $cellpath -type ERROR -msg_id 1 -text ": For multi AXI master configuration the Source AXIS interface width ($src_width) must match the Destination AXIS interface width ($dst_width)  ."
    }
  }

}

# Executed when the block design is validated
proc propagate {cellpath otherinfo} {
  set ip [get_bd_cells $cellpath]

}
