import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring
import xml.dom.minidom
from numpy import array

input_size = 140
output_size = 40
temp_connectivity = [[(6, [108, 109, 110, 111, 132, 133, 134, 135, 156, 157, 158, 159, 180,
       181, 182, 183]), (5, [ 68,  69,  70,  71,  80,  81,  82,  83,  92,  93,  94,  95, 104,
       105, 106, 107]), (4, [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), (48, [216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227]), (46, [208, 209, 210, 211, 220, 221, 222, 223, 224, 225, 226, 227]), (43, [196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207]), (40, [184, 185, 186, 187, 200, 201, 202, 203, 204, 205, 206, 207]), (39, [180, 181, 182, 183, 212, 213, 214, 215, 216, 217, 218, 219]), (38, [176, 177, 178, 179, 212, 213, 214, 215, 216, 217, 218, 219]), (37, [172, 173, 174, 175, 192, 193, 194, 195, 196, 197, 198, 199]), (35, [164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175]), (33, [156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167]), (32, [152, 153, 154, 155, 192, 193, 194, 195, 196, 197, 198, 199]), (31, [148, 149, 150, 151, 184, 185, 186, 187, 188, 189, 190, 191]), (29, [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]), (27, [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]), (26, [128, 129, 130, 131, 184, 185, 186, 187, 188, 189, 190, 191]), (20, [104, 105, 106, 107, 160, 161, 162, 163, 164, 165, 166, 167]), (19, [100, 101, 102, 103, 136, 137, 138, 139, 140, 141, 142, 143]), (3, [ 64,  65,  66,  67, 104, 105, 106, 107, 180, 181, 182, 183]), (2, [ 60,  61,  62,  63,  92,  93,  94,  95, 156, 157, 158, 159]), (1, [ 56,  57,  58,  59,  80,  81,  82,  83, 132, 133, 134, 135]), (0, [ 52,  53,  54,  55,  68,  69,  70,  71, 108, 109, 110, 111]), (44, [200, 201, 202, 203, 208, 209, 210, 211]), (42, [192, 193, 194, 195, 208, 209, 210, 211]), (36, [168, 169, 170, 171, 176, 177, 178, 179]), (34, [160, 161, 162, 163, 176, 177, 178, 179]), (30, [144, 145, 146, 147, 152, 153, 154, 155]), (28, [136, 137, 138, 139, 152, 153, 154, 155]), (50, [224, 225, 226, 227]), (45, [204, 205, 206, 207]), (41, [188, 189, 190, 191]), (7, [52, 53, 54, 55])], [(23, [116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]), (21, [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), (18, [ 96,  97,  98,  99, 168, 169, 170, 171, 172, 173, 174, 175]), (17, [ 92,  93,  94,  95,  96,  97,  98,  99, 100, 101, 102, 103]), (16, [ 88,  89,  90,  91, 112, 113, 114, 115, 116, 117, 118, 119]), (15, [ 84,  85,  86,  87, 144, 145, 146, 147, 148, 149, 150, 151]), (14, [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]), (12, [ 72,  73,  74,  75, 120, 121, 122, 123, 124, 125, 126, 127]), (11, [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), (10, [ 64,  65,  66,  67,  96,  97,  98,  99, 100, 101, 102, 103]), (9, [60, 61, 62, 63, 84, 85, 86, 87, 88, 89, 90, 91]), (8, [56, 57, 58, 59, 72, 73, 74, 75, 76, 77, 78, 79]), (49, [220, 221, 222, 223, 228, 229, 230, 231]), (47, [212, 213, 214, 215, 228, 229, 230, 231]), (24, [120, 121, 122, 123, 128, 129, 130, 131]), (22, [112, 113, 114, 115, 128, 129, 130, 131]), (51, [228, 229, 230, 231]), (25, [124, 125, 126, 127]), (13, [76, 77, 78, 79]), (231, [47, 49, 51]), (230, [47, 49, 51]), (229, [47, 49, 51]), (228, [47, 49, 51]), (227, [46, 48, 50]), (226, [46, 48, 50]), (225, [46, 48, 50]), (224, [46, 48, 50]), (223, [46, 48, 49]), (222, [46, 48, 49]), (221, [46, 48, 49]), (220, [46, 48, 49]), (219, [38, 39, 48]), (218, [38, 39, 48]), (217, [38, 39, 48]), (216, [38, 39, 48]), (215, [38, 39, 47]), (214, [38, 39, 47]), (213, [38, 39, 47]), (212, [38, 39, 47]), (211, [42, 44, 46])], [(210, [42, 44, 46]), (209, [42, 44, 46]), (208, [42, 44, 46]), (207, [40, 43, 45]), (206, [40, 43, 45]), (205, [40, 43, 45]), (204, [40, 43, 45]), (203, [40, 43, 44]), (202, [40, 43, 44]), (201, [40, 43, 44]), (200, [40, 43, 44]), (199, [32, 37, 43]), (198, [32, 37, 43]), (197, [32, 37, 43]), (196, [32, 37, 43]), (195, [32, 37, 42]), (194, [32, 37, 42]), (193, [32, 37, 42]), (192, [32, 37, 42]), (191, [26, 31, 41]), (190, [26, 31, 41]), (189, [26, 31, 41]), (188, [26, 31, 41]), (187, [26, 31, 40]), (186, [26, 31, 40]), (185, [26, 31, 40]), (184, [26, 31, 40]), (183, [ 3,  6, 39]), (182, [ 3,  6, 39]), (181, [ 3,  6, 39]), (180, [ 3,  6, 39]), (179, [34, 36, 38]), (178, [34, 36, 38]), (177, [34, 36, 38]), (176, [34, 36, 38]), (175, [18, 35, 37]), (174, [18, 35, 37]), (173, [18, 35, 37]), (172, [18, 35, 37]), (171, [18, 35, 36])], [(170, [18, 35, 36]), (169, [18, 35, 36]), (168, [18, 35, 36]), (167, [20, 33, 35]), (166, [20, 33, 35]), (165, [20, 33, 35]), (164, [20, 33, 35]), (163, [20, 33, 34]), (162, [20, 33, 34]), (161, [20, 33, 34]), (160, [20, 33, 34]), (159, [ 2,  6, 33]), (158, [ 2,  6, 33]), (157, [ 2,  6, 33]), (156, [ 2,  6, 33]), (155, [28, 30, 32]), (154, [28, 30, 32]), (153, [28, 30, 32]), (152, [28, 30, 32]), (151, [15, 29, 31]), (150, [15, 29, 31]), (149, [15, 29, 31]), (148, [15, 29, 31]), (147, [15, 29, 30]), (146, [15, 29, 30]), (145, [15, 29, 30]), (144, [15, 29, 30]), (143, [19, 27, 29]), (142, [19, 27, 29]), (141, [19, 27, 29]), (140, [19, 27, 29]), (139, [19, 27, 28]), (138, [19, 27, 28]), (137, [19, 27, 28]), (136, [19, 27, 28]), (135, [ 1,  6, 27]), (134, [ 1,  6, 27]), (133, [ 1,  6, 27]), (132, [ 1,  6, 27]), (131, [22, 24, 26])], [(130, [22, 24, 26]), (129, [22, 24, 26]), (128, [22, 24, 26]), (127, [12, 23, 25]), (126, [12, 23, 25]), (125, [12, 23, 25]), (124, [12, 23, 25]), (123, [12, 23, 24]), (122, [12, 23, 24]), (121, [12, 23, 24]), (120, [12, 23, 24]), (119, [16, 21, 23]), (118, [16, 21, 23]), (117, [16, 21, 23]), (116, [16, 21, 23]), (115, [16, 21, 22]), (114, [16, 21, 22]), (113, [16, 21, 22]), (112, [16, 21, 22]), (111, [ 0,  6, 21]), (110, [ 0,  6, 21]), (109, [ 0,  6, 21]), (108, [ 0,  6, 21]), (107, [ 3,  5, 20]), (106, [ 3,  5, 20]), (105, [ 3,  5, 20]), (104, [ 3,  5, 20]), (103, [10, 17, 19]), (102, [10, 17, 19]), (101, [10, 17, 19]), (100, [10, 17, 19]), (99, [10, 17, 18]), (98, [10, 17, 18]), (97, [10, 17, 18]), (96, [10, 17, 18]), (95, [ 2,  5, 17]), (94, [ 2,  5, 17]), (93, [ 2,  5, 17]), (92, [ 2,  5, 17]), (91, [ 9, 14, 16])], [(90, [ 9, 14, 16]), (89, [ 9, 14, 16]), (88, [ 9, 14, 16]), (87, [ 9, 14, 15]), (86, [ 9, 14, 15]), (85, [ 9, 14, 15]), (84, [ 9, 14, 15]), (83, [ 1,  5, 14]), (82, [ 1,  5, 14]), (81, [ 1,  5, 14]), (80, [ 1,  5, 14]), (79, [ 8, 11, 13]), (78, [ 8, 11, 13]), (77, [ 8, 11, 13]), (76, [ 8, 11, 13]), (75, [ 8, 11, 12]), (74, [ 8, 11, 12]), (73, [ 8, 11, 12]), (72, [ 8, 11, 12]), (71, [ 0,  5, 11]), (70, [ 0,  5, 11]), (69, [ 0,  5, 11]), (68, [ 0,  5, 11]), (67, [ 3,  4, 10]), (66, [ 3,  4, 10]), (65, [ 3,  4, 10]), (64, [ 3,  4, 10]), (63, [2, 4, 9]), (62, [2, 4, 9]), (61, [2, 4, 9]), (60, [2, 4, 9]), (59, [1, 4, 8]), (58, [1, 4, 8]), (57, [1, 4, 8]), (56, [1, 4, 8]), (55, [0, 4, 7]), (54, [0, 4, 7]), (53, [0, 4, 7]), (52, [0, 4, 7])]]

# input_size = 140
# output_size = 40
# temp_connectivity = [[(3, [0, 2, 3]),
#   (2, [1, 2, 3]),
#   (1, [0, 1, 3]),
#   (0, [0, 1, 2])]]

# input_size = 4
# output_size = 2
# temp_connectivity = [[(3, [0, 2, 3]), (2, [1, 2, 3])],
#  [(1, [0, 1, 3])]]
    
# print(outgoing)
# print(outgoing2)

"""
[[(4, [1, 3, 4]), (3, [2, 3, 4])],
 [(2, [1, 2, 4]), (1, [1, 2, 3])]]
"""

def write_packing_results_to_xml(temp_connectivity, input_size, output_size):
    connectivity = []

    for clbT in temp_connectivity: # change from 0-index to 1-index
        temp1 = []
        for bleT in clbT:
            temp1.append((bleT[0] + 1, [x + 1 for x in bleT[1]]))
        connectivity.append(temp1)

    outgoing = []
    for clbO in connectivity: # gets all indices/names of BLEs
        temp2 = [bleO[0] for bleO in clbO]
        outgoing.append(temp2)

    outgoing2 = []
    for q1 in range(len(outgoing)): # get all indices/names that are actually called by other CLBs
        temp3 = []
        detect = False
        for element in outgoing[q1]:
            for clbG in connectivity:
                for bleG in clbG:
                    if bleG[0] not in outgoing[q1] and element in bleG[1]:
                        temp3.append(element)
                        detect = True
                        break
                if detect:
                    detect = False
                    break

        outgoing2.append(temp3)

    root = ET.Element("block")                          # top block
    root.set("name", "TODO.net")
    root.set("instance", "FPGA_packed_netlist[0]")
    root.set("architecture_id", "SHA256:TODO")
    root.set("atom_netlist_id", "SHA256:TODO")

    topInputs = ET.Element("inputs")
    topInputs.text = "pclk"
    root.append(topInputs)

    topOutputs = ET.Element("outputs")
    topOutputs.text = "out:_x1"
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
            for m in range(len(bleInputList)):
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

        while output_size - bleCount > 0:
            openBlock = ET.Element("block")
            openBlock.set("name", "open")
            openBlock.set("instance", f"ble[{bleCount}]")
            clbBlock.append(openBlock)
            bleCount += 1

        root.append(clbBlock)
        clbNumber += 1

    outpadBlock = ET.Element("block")
    outpadBlock.set("name", "out:_x1")
    outpadBlock.set("instance", f"io[{clbNumber}]")
    outpadBlock.set("mode", "outpad")

    outpadBlockInputs = ET.Element("inputs")
    outpadBlockInputsPort = ET.Element("port")
    outpadBlockInputsPort.set("name", "outpad")
    outpadBlockInputsPort.text = "_x1"
    outpadBlockInputs.append(outpadBlockInputsPort)
    outpadBlockOutputs = ET.Element("outputs")
    outpadBlockOutputsPort = ET.Element("port")
    outpadBlockOutputsPort.set("name", "inpad")
    outpadBlockOutputsPort.text = "open"
    outpadBlockOutputs.append(outpadBlockOutputsPort)
    outpadBlockClocks = ET.Element("clocks")
    outpadBlockClocksPort = ET.Element("port")
    outpadBlockClocksPort.set("name", "clock")
    outpadBlockClocksPort.text = "open"
    outpadBlockClocks.append(outpadBlockClocksPort)

    subOutpadBlock = ET.Element("block")
    subOutpadBlock.set("name", "out:_x1")
    subOutpadBlock.set("instance", "outpad[0]")
    subOutpadBlockAttributes = ET.Element("attributes")
    subOutpadBlockParameters = ET.Element("parameters")
    subOutpadBlockInputs = ET.Element("inputs")
    subOutpadBlockInputsPort = ET.Element("port")
    subOutpadBlockInputsPort.set("name", "outpad")
    subOutpadBlockInputsPort.text = "io.outpad[0]->outpad"
    subOutpadBlockOutputs = ET.Element("outputs")
    subOutpadBlockClocks = ET.Element("clocks")

    subOutpadBlockInputs.append(subOutpadBlockInputsPort)
    subOutpadBlock.append(subOutpadBlockAttributes)
    subOutpadBlock.append(subOutpadBlockParameters)
    subOutpadBlock.append(subOutpadBlockInputs)
    subOutpadBlock.append(subOutpadBlockOutputs)
    subOutpadBlock.append(subOutpadBlockClocks)
    outpadBlock.append(outpadBlockInputs)
    outpadBlock.append(outpadBlockOutputs)
    outpadBlock.append(outpadBlockClocks)
    outpadBlock.append(subOutpadBlock)

    root.append(outpadBlock)

    inpadBlock = ET.Element("block")
    inpadBlock.set("name", "pclk")
    inpadBlock.set("instance", f"io[{clbNumber + 1}]")
    inpadBlock.set("mode", "inpad")

    inpadBlockInputs = ET.Element("inputs")
    inpadBlockInputsPort = ET.Element("port")
    inpadBlockInputsPort.set("name", "outpad")
    inpadBlockInputsPort.text = "open"
    inpadBlockInputs.append(inpadBlockInputsPort)
    inpadBlockOutputs = ET.Element("outputs")
    inpadBlockOutputsPort = ET.Element("port")
    inpadBlockOutputsPort.set("name", "inpad")
    inpadBlockOutputsPort.text = "inpad[0].inpad[0]->inpad"
    inpadBlockOutputs.append(inpadBlockOutputsPort)
    inpadBlockClocks = ET.Element("clocks")
    inpadBlockClocksPort = ET.Element("port")
    inpadBlockClocksPort.set("name", "clock")
    inpadBlockClocksPort.text = "open"
    inpadBlockClocks.append(inpadBlockClocksPort)

    subInpadBlock = ET.Element("block")
    subInpadBlock.set("name", "pclk")
    subInpadBlock.set("instance", "inpad[0]")
    subInpadBlockAttributes = ET.Element("attributes")
    subInpadBlockParameters = ET.Element("parameters")
    subInpadBlockInputs = ET.Element("inputs")
    subInpadBlockOutputs = ET.Element("outputs")
    subInpadBlockOutputsPort = ET.Element("port")
    subInpadBlockOutputsPort.set("name", "inpad")
    subInpadBlockOutputsPort.text = "pclk"
    subInpadBlockClocks = ET.Element("clocks")

    subInpadBlockOutputs.append(subInpadBlockOutputsPort)
    subInpadBlock.append(subInpadBlockAttributes)
    subInpadBlock.append(subInpadBlockParameters)
    subInpadBlock.append(subInpadBlockInputs)
    subInpadBlock.append(subInpadBlockOutputs)
    subInpadBlock.append(subInpadBlockClocks)
    inpadBlock.append(inpadBlockInputs)
    inpadBlock.append(inpadBlockOutputs)
    inpadBlock.append(inpadBlockClocks)
    inpadBlock.append(subInpadBlock)

    root.append(inpadBlock)

    tree = ET.ElementTree(root) 
      
    with open ("netlist.xml", "w") as files:
        xml_p = xml.dom.minidom.parseString(tostring(root))
        pretty_xml = xml_p.toprettyxml()                                      # writes to netlist.xml
        files.write(pretty_xml)

if __name__ == "__main__":          # adjust as needed
    write_packing_results_to_xml(temp_connectivity, input_size, output_size)         
