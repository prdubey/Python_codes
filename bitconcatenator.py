#Generates WrEn logic and VCCAON AIP instantiation

#!/usr/intel/bin/python3
'''
@author: prdubey
__copyright__ = "Copyright (c) 2020 Intel Corporation, Intel Proprietary and Top Secret Information"
'''
import xml.etree.ElementTree as ET

tree = ET.parse('C:\\Users\\prdubey\\Downloads\\ddrphy_top_crif.xml')
root = tree.getroot()

f1 = open('C:\\Users\\prdubey\\Downloads\\tmp.sv',"w+")


new_data = ''
signal = ''

for reg in root.findall('registerFile'):
    if (reg.find('RalFile').text) == "ddrccc_msg0":
        for child in reg.findall('register'):
            reg_name = child.findtext("name")
            new_data = "{"
            log_sig = []
            for grandchild in child.findall('field'):
                field_name = grandchild.findtext("name")
                bit_width =  grandchild.findtext("bitWidth")
                bit_offset = grandchild.findtext("bitOffset")
                if ((int(bit_width) + int(bit_offset) - 1 )>= 31):
                    new_data += "registers." + reg_name + '.' + field_name
                else:
                    new_data += "registers." + reg_name + '.' + field_name + ','
                    
            new_data += "}"
            typedef = reg_name + "_t"
            reg_def  = typedef + " " + reg_name + "_AIP_OUT;"
            #print(reg_def)
            #print("\n")
            new_name = reg_name.split("_")
            #print(new_name)
            for name in new_name:
                #print(name)
                new_sig = "%s%s" % (name[0], name[1:].lower())
                log_sig.append(new_sig)
            new_log_sig = '_'.join(log_sig)
            #print(new_log_sig)
            #print("\n")
            signal = new_log_sig
            output_sig = signal + "ShadowSnnnH"
            for grandchild in child.findall('field'):
                field_name = grandchild.findtext("name")
                bit_width =  grandchild.findtext("bitWidth")
                bit_offset = grandchild.findtext("bitOffset")
                typedef_out = output_sig + "[" + str(int(bit_offset) + int(bit_width) - 1) + ":" + bit_offset  + "]"
                out_reg_def = "assign "  + reg_name + "_AIP_OUT." + field_name + " = " + typedef_out
                #print(out_reg_def)
                #print("\n")
            f1.write("logic " + signal + "WrEnSnnnH;")
            f1.write("\n")
            f1.write("logic [31:0] " + signal + "SnnnH;")
            f1.write("\n")
            f1.write("logic [31:0] " + signal + "ShadowSnnnH;")
            f1.write("\n")
            wr_en = "assign " + signal + "WrEnSnnnH =  "  + "DdrCrWrValidSnnnH  && (GDMsgWriteAddrSnnnH == " + reg_name + "_CR_ADDR[8:2]);"
            f1.write(wr_en)
            f1.write("\n")
            assignment = "assign " +  signal + "SnnnH" + " = " + new_data + " ;"
            f1.write(assignment)
            f1.write("\n")
            f1.write("`DDRPHY_SBCLKCR_VCCAONAIP_SHADOW(" + signal + "ShadowSnnnH, " + signal + "ValidSnnnH, "  + signal + "SnnnH," + " ClkCriSH, " + "DdrSAPwrGoodOnDD2_HV, DdrVDD2PwrGoodLocalOn1p8, " + reg_name + "_RESET, " + signal + "WrEnSnnnH)")
            f1.write("\n")
            f1.write("\n")

f1.close
        