import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring
import xml.dom.minidom

# LINELENGTH = 1024
# TAB_LENGTH = 4

input_size = 4
output_size = 2
connectivity = [[(3, [0, 2, 3]), (2, [1, 2, 3])],
 [(1, [0, 1, 3]), (0, [0, 1, 2])]]

def write_packing_results_to_xml():
    root = ET.Element("block")                          # top block
    root.set("name", "b1.net")
    root.set("instance", "FPGA_packed_netlist[0]")
    root.set("architecture_id", "TODO")
    root.set("atom_netlist_id", "TODO")

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
        clbBlock.set("name", "TODO")
        clbBlock.set("instance", f"clb[{clbNumber}]")
        clbBlock.set("mode", "default")

        clbBlockInputs = ET.Element("inputs")
        clbBlockInputsPort = ET.Element("port")
        clbBlockInputsPort.set("name", "I")
        # clbBlockInputsPort.text = "open " * (input_size - 1) + "open"

        clbBlockInputsPortText = []
        for blei in clb:
            clbBlockInputsPortText = clbBlockInputsPortText + blei[1]
            clbBlockInputsPortText.sort()
            tempSet = set(clbBlockInputsPortText)
            finalList = list(tempSet)

        finalCLBText = ""

        for i in range(input_size - 1):
            if i < len(finalList) - 1:
                finalCLBText = finalCLBText + "_x" + str(finalList[i]) + " "
            else:
                finalCLBText = finalCLBText + "open "
        if len(finalList) == input_size:
            finalCLBText = finalCLBText + "_x" + str(finalList[input_size - 1])
        else:
            finalCLBText = finalCLBText + "open"

        clbBlockInputsPort.text = finalCLBText

        clbBlockInputs.append(clbBlockInputsPort)
        clbBlock.append(clbBlockInputs)

        clbBlockOutputs = ET.Element("outputs")
        clbBlockOutputsPort = ET.Element("port")
        clbBlockOutputsPort.set("name", "O")
        clbBlockOutputsPort.text = "open " * (output_size - 1) + "open"
        clbBlockOutputs.append(clbBlockOutputsPort)
        clbBlock.append(clbBlockOutputs)
        
        clbBlockClocks = ET.Element("clocks")
        clbBlockClocksPort = ET.Element("port")
        clbBlockClocksPort.set("name", "clk")
        clbBlockClocksPort.text = "pclk"
        clbBlockClocks.append(clbBlockClocksPort)
        clbBlock.append(clbBlockClocks)

        bleCount = 0

        for ble in clb:
            bleBlock = ET.Element("block")
            bleBlock.set("name", "TODO")
            bleBlock.set("instance", f"ble[{bleCount}]")
            bleBlock.set("mode", "default")

            bleBlockInputs = ET.Element("inputs")
            bleBlockInputsPort = ET.Element("port")
            bleBlockInputsPort.set("name", "in")
            # bleBlockInputsPort.text = "open " * (input_size - 1) + "open"

            bleInputList = ble[1]
            bleInputText = ""

            for i in bleInputList:
                for j in range(len(finalList)):
                    if finalList[j] == i:
                        bleInputText = bleInputText + f"clb.I[{j}]-&gt;crossbar "
                        break

            while len(bleInputList) < input_size - 1:
                bleInputText = bleInputText + "open "

            bleInputText = bleInputText + "open"
            bleBlockInputsPort.text = bleInputText

            bleBlockInputs.append(bleBlockInputsPort)
            bleBlock.append(bleBlockInputs)

            bleBlockOutputs = ET.Element("outputs")
            bleBlockOutputsPort = ET.Element("port")
            bleBlockOutputsPort.set("name", "out")
            bleBlockOutputsPort.text = "ff[0].Q[0]-&gt;direct4"
            bleBlockOutputs.append(bleBlockOutputsPort)
            bleBlock.append(bleBlockOutputs)

            bleBlockClocks = ET.Element("clocks")
            bleBlockClocksPort = ET.Element("port")
            bleBlockClocksPort.set("name", "clk")
            bleBlockClocksPort.text = "clb.clk[0]-&gt;clks"
            bleBlockClocks.append(bleBlockClocksPort)
            bleBlock.append(bleBlockClocks)

            lutBlock = ET.Element("block")
            lutBlock.set("name", f"lut_{input_size}[0]")
            lutBlock.set("instance", f"lut_{input_size}[0]")
            lutBlock.set("mode", f"lut_{input_size}")
            lutBlockInputs = ET.Element("inputs")
            lutBlockInputsPort = ET.Element("port")
            lutBlockInputsPort.set("name", "in")
            # lutBlockInputsPort.text = "open " * (input_size - 1) + "open"
            
            lutBlockText = ""
            tempList2 = bleInputText.split()

            for i in range(len(tempList2) - 1):
                if tempList2[i] != "open":
                    lutBlockText = lutBlockText + f"ble.in[{i}]-&gt;direct1 "
                else:
                    lutBlockText = "open "

            while len(tempList2) < input_size - 1:
                lutBlockText = lutBlockText + "open "

            lutBlockText = lutBlockText + "open"

            lutBlockInputsPort.text = lutBlockText
            
            lutBlockInputs.append(lutBlockInputsPort)
            lutBlock.append(lutBlockInputs)

            lutBlockOutputs = ET.Element("outputs")
            lutBlockOutputsPort = ET.Element("port")
            lutBlockOutputsPort.set("name", "out")
            lutBlockOutputsPort.text = f"lut[0].out[0]-&gt;direct:lut_{input_size}"
            lutBlockOutputs.append(lutBlockOutputsPort)
            lutBlock.append(lutBlockOutputs)

            lutBlockClocks = ET.Element("clocks")
            lutBlock.append(lutBlockClocks)

            subLutBlock = ET.Element("block")
            subLutBlock.set("name", "TODO")
            subLutBlock.set("instance", "lut[0]")
            subLutBlockAttributes = ET.Element("attributes")
            subLutBlockParameters = ET.Element("parameters")
            subLutBlock.append(subLutBlockAttributes)
            subLutBlock.append(subLutBlockParameters)

            subLutBlockInputs = ET.Element("inputs")
            subLutBlockInputsPort = ET.Element("port")
            subLutBlockInputsPort.set("name", "in")
            # subLutBlockInputsPort.text = "open " * (input_size - 1) + "open"

            subLutBlockText = ""
            tempList3 = lutBlockText.split()

            for i in range(len(tempList3) - 1):
                if tempList3[i] != "open":
                    subLutBlockText = subLutBlockText + f"lut_{input_size}.in[{i}]-&gt;lut_{input_size} "
                else:
                    subLutBlockText = "open "

            while len(tempList3) < input_size - 1:
                subLutBlockText = subLutBlockText + "open "

            subLutBlockText = subLutBlockText + "open"

            subLutBlockInputsPort.text = subLutBlockText

            subLutBlockInputsPortRotation = ET.Element("port_rotation_map")
            subLutBlockInputsPortRotation.set("name", "in")

            subLutBlockText2 = ""
            tempList4 = lutBlockText.split()
            count = 2

            for i in range(len(tempList4) - 1):
                if tempList4[i] != "open":
                    subLutBlockText2 = subLutBlockText2 + f"{count} "
                    count = count - 1
                else:
                    subLutBlockText2 = "open "

                if count < 0:
                    break

            while len(tempList3) < input_size - 1:
                subLutBlockText2 = subLutBlockText2 + "open "

            subLutBlockText2 = subLutBlockText2 + "open"

            subLutBlockInputsPortRotation.text = subLutBlockText2

            # subLutBlockInputsPortRotation.text = "open " * (input_size - 1) + "open"
            subLutBlockInputs.append(subLutBlockInputsPort)
            subLutBlockInputs.append(subLutBlockInputsPortRotation)
            subLutBlock.append(subLutBlockInputs)

            subLutBlockOutputs = ET.Element("outputs")
            subLutBlockOutputsPort = ET.Element("port")
            subLutBlockOutputsPort.set("name", "out")
            subLutBlockOutputs.append(subLutBlockOutputsPort)
            subLutBlock.append(subLutBlockOutputs)

            subLutBlockClocks = ET.Element("clocks")
            subLutBlock.append(subLutBlockClocks)

            ffBlock = ET.Element("block")
            ffBlock.set("name", "TODO")
            ffBlock.set("instance", "ff[0]")
            ffBlockAttributes = ET.Element("attributes")
            ffBlockParameters = ET.Element("parameters")
            ffBlock.append(ffBlockAttributes)
            ffBlock.append(ffBlockParameters)

            ffBlockInputs = ET.Element("inputs")
            ffBlockInputsPort = ET.Element("port")
            ffBlockInputsPort.set("name", "D")
            ffBlockInputsPort.text = f"lut_{input_size}[0].out[0]-&gt;direct2"
            ffBlockInputs.append(ffBlockInputsPort)
            ffBlock.append(ffBlockInputs)

            ffBlockOutputs = ET.Element("outputs")
            ffBlockOutputsPort = ET.Element("port")
            ffBlockOutputsPort.set("name", "Q")
            ffBlockOutputs.append(ffBlockOutputsPort)
            ffBlock.append(ffBlockOutputs)

            ffBlockClocks = ET.Element("clocks")
            ffBlockClocksPort = ET.Element("port")
            ffBlockClocksPort.set("name", "clk")
            ffBlockClocksPort.text = "ble.clk[0]-&gt;direct3"
            ffBlockClocks.append(ffBlockClocksPort)
            ffBlock.append(ffBlockClocks)

            lutBlock.append(subLutBlock)
            bleBlock.append(lutBlock)
            bleBlock.append(ffBlock)

            clbBlock.append(bleBlock)

            bleCount += 1

        root.append(clbBlock)
        clbNumber += 1

    tree = ET.ElementTree(root) 
      
    with open ("netlist.xml", "wb") as files:              # writes to netlist.xml
        tree.write(files)

if __name__ == "__main__":          # adjust as neededl
    write_packing_results_to_xml()         
    tree = ET.parse('netlist.xml')
    root = tree.getroot()

    xml_p = xml.dom.minidom.parseString(tostring(root))
    pretty_xml = xml_p.toprettyxml()                        # indent to make it look nice
    print(pretty_xml)

    f = open("netlist.txt", "w")
    for test in pretty_xml:
        f.write(test)
    f.close()