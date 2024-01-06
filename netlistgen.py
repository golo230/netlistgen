import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring
import xml.dom.minidom

# LINELENGTH = 1024
# TAB_LENGTH = 4

input_size = 144
output_size = 44
connectivity = [[1,2,3],
                [4,5,6],
                [7,8,9]
                ]

def write_packing_results_to_xml():
    root = ET.Element("block")                          # top block
    root.set("name", "b1.net")
    root.set("instance", "FPGA_packed_netlist[0]")
    root.set("architecture_id", "TODO")

    topInputs = ET.Element("inputs")
    topInputs.text = "pclk"
    root.append(topInputs)

    topOutputs = ET.Element("outputs")
    root.append(topOutputs)

    topClocks = ET.Element("clocks")
    topClocks.text = "pclk"
    root.append(topClocks)

    clbNumber = 0

    for clb in connectivity:
        clbBlock = ET.Element("block")
        clbBlock.set("name", "temp")
        clbBlock.set("instance", f"clb[{clbNumber}]")
        clbBlock.set("mode", "default")

        clbBlockInputs = ET.Element("inputs")
        clbBlockInputsPort = ET.Element("port")
        clbBlockInputsPort.set("name", "I")

        clbBlockInputs.append(clbBlockInputsPort)


        clbBlockOutputs = ET.Element("outputs")
        clbBlockOutputsPort = ET.Element("port")
        clbBlockOutputsPort.set("name", "O")

        clbBlockOutputs.append(clbBlockInputsPort)
        
        clbBlockClocks = ET.Element("clocks")
        clbBlockClocksPort = ET.Element("port")
        clbBlockClocksPort.set("name", "clk")
        clbBlockClocksPort.text = "pclk"
        clbBlockClocks.append(clbBlockClocksPort)

        bleCount = 0

        for ble in clb:
            bleBlock = ET.Element("block")
            bleBlock.set("name", "")
            bleBlock.set("instance", "ble[{bleCount}]")
            bleBlock.set("mode", "default")

            bleBlockInputs = ET.Element("inputs")
            bleBlockInputsPort = ET.Element("port")
            bleBlockInputsPort.set("name", "in")
            bleBlockInputs.append(bleBlockInputsPort)

            bleBlockOutputs = ET.Element("outputs")
            bleBlockOutputsPort = ET.Element("port")
            bleBlockOutputsPort.set("name", "out")
            bleBlockOutputsPort.text = "ff[0].Q[0]-&gt;direct4"
            bleBlockOutputs.append(bleBlockOutputsPort)

            bleBlockClocks = ET.Element("clocks")
            bleBlockClocksPort = ET.Element("port")
            bleBlockClocksPort.set("name", "clk")
            bleBlockClocksPort.text = "clb.clk[0]-&gt;clks"
            bleBlockClocks.append(bleBlockClocksPort)

            lutBlock = ET.Element("block")

            subLutBlock = ET.Element("block")

            ffBlock = ET.Element("block")

            bleCount += 1


        root.append(clbBlock)
        clbNumber += 1

    tree = ET.ElementTree(root) 
      
    with open ("netlist.xml", "wb") as files:              # writes to netlist.xml
        tree.write(files)

if __name__ == "__main__":          # adjust as needed
    write_packing_results_to_xml()         
    tree = ET.parse('netlist.xml')
    root = tree.getroot()

    xml_p = xml.dom.minidom.parseString(tostring(root))
    pretty_xml = xml_p.toprettyxml()                        # indent to make it look nice
    print(pretty_xml)

    f = open("external.txt", "w")
    for test in pretty_xml:
        f.write(test)
    f.close()