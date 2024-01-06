# Outline

Netlist Structure:
```
<block> MAIN NETLIST
    <inputs>
    <outputs>
    <clocks>
    <block> CLB
        <inputs>
            <port>
        </inputs>
        <outputs>
            <port>
        </outputs>
        <clocks>
            <port>
        </clocks>
        <block> BLE
            <block instance="lut[0]"> LUT_144
                <block lut> LUT0
            <block ff>
        </block> BLE, REPEAT
    </block> CLB, REPEAT
</block>
```

**Alg Input:** 
input size (integer)  
output size (integer)  

results of packing alg (nested nested list)
```
[ NETLIST
    [ CLB
        [BLE], [BLE], [BLE]
    ],
    [ CLB
        [BLE], [BLE], [BLE]
    ],
]
```

### Very Basic Pseudocode
```
1. Create top netlist block
2. Loop through to create CLBs
3. For each CLB, create the BLEs
4. For each BLE, create the top LUT (and sub LUT) and flip-flop 
```

Input/Output Logic:  
Inputs: CLB inputs are all the inputs taken in by the BLEs
Outputs: CLB outputs are... TODO
