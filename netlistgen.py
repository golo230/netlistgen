import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring
import xml.dom.minidom

input_size = 4
output_size = 2
temp_connectivity = [[(3, [0, 2, 3]), (2, [1, 2, 3])],
 [(1, [0, 1, 3]), (0, [0, 1, 2])]]

# input_size = 140
# output_size = 40
# temp_connectivity = [[(3, [0, 2, 3]),
#   (2, [1, 2, 3]),
#   (1, [0, 1, 3]),
#   (0, [0, 1, 2])]]

connectivity = []

for clbT in temp_connectivity:
    temp1 = []
    for bleT in clbT:
        temp1.append((bleT[0] + 1, [x + 1 for x in bleT[1]]))
    connectivity.append(temp1)

# print(connectivity)

outgoing = []
for clbO in connectivity:
    temp2 = [bleO[0] for bleO in clbO]
    outgoing.append(temp2)

outgoing2 = []
for q1 in range(len(outgoing)):
    temp3 = []
    detect = False
    for element in outgoing[q1]:
        for clbG in connectivity:
            for bleG in clbG:
                if bleG[0] not in outgoing[q1] and element in bleG[1]:
                    temp3.append(element)
                    break

    outgoing2.append(temp3)

# print(outgoing2)

"""
[[(4, [1, 3, 4]), (3, [2, 3, 4])],
 [(2, [1, 2, 4]), (1, [1, 2, 3])]]
"""

def write_packing_results_to_xml():
    root = ET.Element("block")                          # top block
    root.set("name", "b1.net")
    root.set("instance", "FPGA_packed_netlist[0]")
    root.set("architecture_id", "SHA256:TODO")
    root.set("atom_netlist_id", "SHA256:TODO")

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
        clbBlock.set("name", "_l" + str(clb[-1][0]))
        clbBlock.set("instance", f"clb[{clbNumber}]")
        clbBlock.set("mode", "default")

        clbBlockInputs = ET.Element("inputs")
        clbBlockInputsPort = ET.Element("port")
        clbBlockInputsPort.set("name", "I")

        clbinputs = []
        internalclbinputs = []
        for bleS in clb:
            clbinputs = clbinputs + bleS[1]
            internalclbinputs.append(bleS[0])

        clbinputs.sort()
        finalclbinputs = list(set(clbinputs))
        finalclbtext = ""

        for i in finalclbinputs:
            if i not in internalclbinputs:
                finalclbtext = finalclbtext + "_x" + str(i) + " "
        
        finalclbtextlist = finalclbtext.split()
        finalclbtextlist = [x[2:] for x in finalclbtextlist]

        if len(finalclbtextlist) == input_size:
            finalclbtext = finalclbtext[:-1]
        elif len(finalclbtextlist) < input_size:
            finalclbtext = finalclbtext + " ".join(["open"] * (input_size - len(finalclbtextlist)))

        clbBlockInputsPort.text = finalclbtext

        clbBlockInputs.append(clbBlockInputsPort)
        clbBlock.append(clbBlockInputs)

        clbBlockOutputs = ET.Element("outputs")
        clbBlockOutputsPort = ET.Element("port")
        clbBlockOutputsPort.set("name", "O")

        clbBlockOutputsPortText = ""
        for f in outgoing2[clbNumber]:
            clbBlockOutputsPortText += f"ble[{outgoing[clbNumber].index(f)}].out[0]->clbouts1 "

        if len(outgoing2[clbNumber]) == output_size:
            clbBlockOutputsPortText = clbBlockOutputsPortText[:-1]
        elif len(outgoing2[clbNumber]) < output_size:
            clbBlockOutputsPortText = clbBlockOutputsPortText + " ".join(["open"] * (output_size - len(outgoing2[clbNumber])))

        clbBlockOutputsPort.text = clbBlockOutputsPortText
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
            bleBlock.set("name", "_l" + str(ble[0]))
            bleBlock.set("instance", f"ble[{bleCount}]")
            bleBlock.set("mode", "default")

            bleBlockInputs = ET.Element("inputs")
            bleBlockInputsPort = ET.Element("port")
            bleBlockInputsPort.set("name", "in")

            bleInputList = ble[1]
            bleInputText = ""

            for j in bleInputList:
                if j in internalclbinputs:
                    bleInputText += f"ble[{internalclbinputs.index(j)}].out[0]->crossbar "
                else:
                    bleInputText += f"clb.I[{finalclbtextlist.index(str(j))}]->crossbar "

            if len(bleInputList) == input_size:
                bleInputText = bleInputText[:-1]
            elif len(bleInputList) < input_size:
                bleInputText = bleInputText + " ".join(["open"] * (input_size - len(bleInputList)))
            
            bleBlockInputsPort.text = bleInputText

            bleBlockInputs.append(bleBlockInputsPort)
            bleBlock.append(bleBlockInputs)

            bleBlockOutputs = ET.Element("outputs")
            bleBlockOutputsPort = ET.Element("port")
            bleBlockOutputsPort.set("name", "out")
            bleBlockOutputsPort.text = "ff[0].Q[0]->direct4"
            bleBlockOutputs.append(bleBlockOutputsPort)
            bleBlock.append(bleBlockOutputs)

            bleBlockClocks = ET.Element("clocks")
            bleBlockClocksPort = ET.Element("port")
            bleBlockClocksPort.set("name", "clk")
            bleBlockClocksPort.text = "clb.clk[0]->clks"
            bleBlockClocks.append(bleBlockClocksPort)
            bleBlock.append(bleBlockClocks)

            lutBlock = ET.Element("block")
            lutBlock.set("name", "_l" + str(ble[0]))
            lutBlock.set("instance", f"lut_{input_size}[0]")
            lutBlock.set("mode", f"lut_{input_size}")
            lutBlockInputs = ET.Element("inputs")
            lutBlockInputsPort = ET.Element("port")
            lutBlockInputsPort.set("name", "in")
            
            lutBlockText = ""
            for k in range(len(bleInputList)):
                lutBlockText += f"ble.in[{k}]->direct1 "
            
            if len(bleInputList) == input_size:
                lutBlockText = lutBlockText[:-1]
            elif len(bleInputList) < input_size:
                lutBlockText = lutBlockText + " ".join(["open"] * (input_size - len(bleInputList)))

            lutBlockInputsPort.text = lutBlockText
            
            lutBlockInputs.append(lutBlockInputsPort)
            lutBlock.append(lutBlockInputs)

            lutBlockOutputs = ET.Element("outputs")
            lutBlockOutputsPort = ET.Element("port")
            lutBlockOutputsPort.set("name", "out")
            lutBlockOutputsPort.text = f"lut[0].out[0]->direct:lut_{input_size}"
            lutBlockOutputs.append(lutBlockOutputsPort)
            lutBlock.append(lutBlockOutputs)

            lutBlockClocks = ET.Element("clocks")
            lutBlock.append(lutBlockClocks)

            subLutBlock = ET.Element("block")
            subLutBlock.set("name", "_l" + str(ble[0]))
            subLutBlock.set("instance", "lut[0]")
            subLutBlockAttributes = ET.Element("attributes")
            subLutBlockParameters = ET.Element("parameters")
            subLutBlock.append(subLutBlockAttributes)
            subLutBlock.append(subLutBlockParameters)

            subLutBlockInputs = ET.Element("inputs")
            subLutBlockInputsPort = ET.Element("port")
            subLutBlockInputsPort.set("name", "in")

            subLutBlockText = ""
            for l in range(len(bleInputList)):
                subLutBlockText += f"lut_{input_size}.in[{l}]->direct:lut_{input_size} "
            
            if len(bleInputList) == input_size:
                subLutBlockText = subLutBlockText[:-1]
            elif len(bleInputList) < input_size:
                subLutBlockText = subLutBlockText + " ".join(["open"] * (input_size - len(bleInputList)))

            subLutBlockInputsPort.text = subLutBlockText

            subLutBlockInputsPortRotation = ET.Element("port_rotation_map")
            subLutBlockInputsPortRotation.set("name", "in")

            subLutBlockText2 = ""
            for m in reversed(range(len(bleInputList))):
                subLutBlockText2 +=  str(m) + " "
            
            if len(bleInputList) == input_size:
                subLutBlockText2 = subLutBlockText2[:-1]
            elif len(bleInputList) < input_size:
                subLutBlockText2 = subLutBlockText2 + " ".join(["open"] * (input_size - len(bleInputList)))

            subLutBlockInputsPortRotation.text = subLutBlockText2

            subLutBlockInputs.append(subLutBlockInputsPort)
            subLutBlockInputs.append(subLutBlockInputsPortRotation)
            subLutBlock.append(subLutBlockInputs)

            subLutBlockOutputs = ET.Element("outputs")
            subLutBlockOutputsPort = ET.Element("port")
            subLutBlockOutputsPort.set("name", "out")
            subLutBlockOutputsPort.text = "_l" + str(ble[0])
            subLutBlockOutputs.append(subLutBlockOutputsPort)
            subLutBlock.append(subLutBlockOutputs)

            subLutBlockClocks = ET.Element("clocks")
            subLutBlock.append(subLutBlockClocks)

            ffBlock = ET.Element("block")
            ffBlock.set("name", "_x" + str(ble[0]))
            ffBlock.set("instance", "ff[0]")
            ffBlockAttributes = ET.Element("attributes")
            ffBlockParameters = ET.Element("parameters")
            ffBlock.append(ffBlockAttributes)
            ffBlock.append(ffBlockParameters)

            ffBlockInputs = ET.Element("inputs")
            ffBlockInputsPort = ET.Element("port")
            ffBlockInputsPort.set("name", "D")
            ffBlockInputsPort.text = f"lut_{input_size}[0].out[0]->direct2"
            ffBlockInputs.append(ffBlockInputsPort)
            ffBlock.append(ffBlockInputs)

            ffBlockOutputs = ET.Element("outputs")
            ffBlockOutputsPort = ET.Element("port")
            ffBlockOutputsPort.set("name", "Q")
            ffBlockOutputsPort.text = "_x" + str(ble[0])
            ffBlockOutputs.append(ffBlockOutputsPort)
            ffBlock.append(ffBlockOutputs)

            ffBlockClocks = ET.Element("clocks")
            ffBlockClocksPort = ET.Element("port")
            ffBlockClocksPort.set("name", "clk")
            ffBlockClocksPort.text = "ble.clk[0]->direct3"
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
      
    with open ("netlist.xml", "w") as files:
        xml_p = xml.dom.minidom.parseString(tostring(root))
        pretty_xml = xml_p.toprettyxml()                                      # writes to netlist.xml
        files.write(pretty_xml)

if __name__ == "__main__":          # adjust as needed
    write_packing_results_to_xml()         