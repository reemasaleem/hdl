# Create only the RX path
set INTF_CFG RX

# Dummy parameters for TX
set ad_project_params(TX_LANE_RATE) 0
set ad_project_params(TX_JESD_M) 1
set ad_project_params(TX_JESD_L) 1
set ad_project_params(TX_JESD_S) 1
set ad_project_params(TX_JESD_NP) 12
set ad_project_params(TX_NUM_LINKS) 1
set ad_project_params(TX_KS_PER_CHANNEL) 1

source $ad_hdl_dir/projects/ad9081_fmca_ebz/vck190/system_bd.tcl

#system ID
ad_ip_parameter axi_sysid_0 CONFIG.ROM_ADDR_BITS 9
ad_ip_parameter rom_sys_0 CONFIG.PATH_TO_FILE "[pwd]/mem_init_sys.txt"
ad_ip_parameter rom_sys_0 CONFIG.ROM_ADDR_BITS 9
set sys_cstring "sys rom custom string placeholder"
sysid_gen_sys_init_file $sys_cstring
