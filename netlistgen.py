import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring
import xml.dom.minidom

# LINELENGTH = 1024
# TAB_LENGTH = 4

# The function write_packing_results_to_xml prints a skeleton of a netlist given a list of inputs and outputs
# It creates a top block, then a block for each input and output
# Two libraries are used:
# 1. xml.etree.ElementTree, which provides the ability to create and modify XML files with Python
# 2. xml.dom.minidom, which is used for indenting said XML file

# When running the program, it prints out an XML netlist based on the example from https://docs.verilogtorouting.org/en/latest/vpr/file_formats/#packed-netlist-format-net
# given inputs pa, pb, pc, and outputs pd, pe, pf, and pg, a netlist is generated

# there's a file titled netlist.xml that is created, but it is without indents
# to account for this, the terminal also prints the indented version of the netlist
# more work is needed, but this is a functional start!

# NOTE: I assumed the output ports had the same structure as the input ports, but I am unsure if this is correct
# NOTE: the TODOs represent values that I believe are reliant on the initial clustering, so I will need to fix those too

def write_packing_results_to_xml(inputs, outputs):
    root = ET.Element("block")                          # top block
    root.set("name", "b1.net")
    root.set("instance", "FPGA_packed_netlist[0]")

    topInputs = ET.Element("inputs")
    topInputs.text = "pclk"
    root.append(topInputs)

    topOutputs = ET.Element("outputs")
    topOutputs.text = ' '.join(outputs)
    root.append(topOutputs)

    topClocks = ET.Element("clocks")
    topClocks.text = "pclk"
    root.append(topClocks)   

    for i in inputs:                                    # input blocks
        instanceBlock = ET.Element("block")             # start of main input block
        instanceBlock.set("name", i)
        instanceBlock.set("instance", "TODO")
        instanceBlock.set("mode", "TODO")

        instanceInput = ET.Element("inputs")
        inputPort = ET.Element("port")
        inputPort.set("name", "TODO")
        instanceInput.append(inputPort)
        instanceBlock.append(instanceInput)

        instanceOutput = ET.Element("outputs")
        outputPort = ET.Element("port")
        outputPort.set("name", "TODO")
        instanceOutput.append(outputPort)
        instanceBlock.append(instanceOutput)

        instanceClocks = ET.Element("clocks")
        blockPort = ET.Element("port")
        blockPort.set("name", "TODO")
        instanceBlock.append(instanceClocks)

        subBlock = ET.Element("block")                  # start of sub input block within the hierarchy
        subBlock.set("name", i)
        subBlock.set("instance", "TODO")

        subInput = ET.Element("inputs")
        subOutput = ET.Element("outputs")
        subPortO = ET.Element("port")
        subPortO.set("name", "TODO")
        subOutput.append(subPortO)
        subClocks = ET.Element("clocks")

        subAttribute = ET.Element("attribute")
        attribute = ET.Element("attribute")
        attribute.set("name", "TODO")
        subAttribute.append(attribute)

        subParameter = ET.Element("parameters")
        parameter = ET.Element("parameter")
        parameter.set("name", "TODO")
        subParameter.append(parameter)

        subBlock.append(subInput)
        subBlock.append(subOutput)
        subBlock.append(subClocks)
        subBlock.append(subAttribute)
        subBlock.append(subParameter)

        instanceBlock.append(subBlock)

        root.append(instanceBlock)

    for j in outputs:                                   # output blocks
        instanceBlock = ET.Element("block")             # start of main output block
        instanceBlock.set("name", j)
        instanceBlock.set("instance", "TODO")
        instanceBlock.set("mode", "TODO")

        instanceInput = ET.Element("inputs")
        inputPort = ET.Element("port")
        inputPort.set("name", "TODO")
        instanceInput.append(inputPort)
        instanceBlock.append(instanceInput)

        instanceOutput = ET.Element("outputs")
        outputPort = ET.Element("port")
        outputPort.set("name", "TODO")
        instanceOutput.append(outputPort)
        instanceBlock.append(instanceOutput)

        instanceClocks = ET.Element("clocks")
        blockPort = ET.Element("port")
        blockPort.set("name", "TODO")
        instanceBlock.append(instanceClocks)

        subBlock = ET.Element("block")                  # start of sub output block within the hierarchy
        subBlock.set("name", j)
        subBlock.set("instance", "TODO")

        subInput = ET.Element("inputs")
        subOutput = ET.Element("outputs")
        subPortO = ET.Element("port")
        subPortO.set("name", "TODO")
        subOutput.append(subPortO)
        subClocks = ET.Element("clocks")

        subAttribute = ET.Element("attribute")
        attribute = ET.Element("attribute")
        attribute.set("name", "TODO")
        subAttribute.append(attribute)

        subParameter = ET.Element("parameters")
        parameter = ET.Element("parameter")
        parameter.set("name", "TODO")
        subParameter.append(parameter)

        subBlock.append(subInput)
        subBlock.append(subOutput)
        subBlock.append(subClocks)
        subBlock.append(subAttribute)
        subBlock.append(subParameter)

        instanceBlock.append(subBlock)

        root.append(instanceBlock)

    tree = ET.ElementTree(root) 
      
    with open ("netlist.xml", "wb") as files:              # writes to netlist.xml
        tree.write(files)

if __name__ == "__main__":  
    inp = ["pa", "pb", "pc"]                                # adjust as needed
    outp = ["out:pd", "out:pe", "out:pf", "out:pg"]         # adjust as needed
    write_packing_results_to_xml(inp, outp)         
    tree = ET.parse('netlist.xml')
    root = tree.getroot()

    xml_p = xml.dom.minidom.parseString(tostring(root))
    pretty_xml = xml_p.toprettyxml()                        # indent to make it look nice
    print(pretty_xml)

    f = open("external.txt", "w")
    for test in pretty_xml:
        f.write(test)
    f.close()