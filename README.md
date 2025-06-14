![image](https://github.com/user-attachments/assets/c1291e83-c6da-4d8b-9ff6-c4e30bbe39e7)

# MARMalade CPU & Assembler

A simple 8-bit custom CPU and its accompanying assembler, designed and implemented using Logisim Evolution and Python. The CPU, named **MARMalade**, supports a minimal instruction set architecture (ISA) with basic arithmetic and memory load operations. It is powered by a Python-based assembler (**M-ARM**) that translates human-readable instructions into machine code.

## Project Overview

This project was developed concurrently with a computer architecture course to demonstrate a complete assembly to execution workflow:

- **MARMalade**: A custom-built 8-bit CPU architecture simulated in Logisim.
- **M-ARM Assembler**: A Python program that converts high-level assembly into machine-readable hex format.

## Repository Structure

```
├── MarmAssembler.py       # Python-based assembler
├── Instructions.txt       # Output hex image from the assembler
├── MARMalade.circ         # Logisim circuit file (CPU)
└── README.md              # Project documentation
```

## Features

- 8-bit instruction format: `2 bits opcode | 2 bits destination | 2x 2 bits parameters`
- Supports up to **16 instructions**
- Manual entry assembler interface with real-time validation
- Custom data memory layout (hardcoded in Logisim)
- Exported hex machine code compatible with Logisim's instruction memory

## Getting Started

### Step 1: Assembling a Program

Run the assembler:

```bash
python MarmAssembler.py
```

Follow the prompt to enter up to 16 instructions. Use the following syntax:

- `LDR Md Imm 00`  
  (Loads data from memory address `Imm` into register `Md`)
- `ADD Md Ma Mb`  
  (Adds `Ma` + `Mb`, stores in `Md`)
- `SUB Md Ma Mb`  
  (Subtracts `Mb` from `Ma`, stores in `Md`)

Example session:

```
Enter Instruction 1:
LDR M0 0 00
Add another instruction? (y/n): y
Enter Instruction 2:
LDR M1 1 00
...
```

The assembler generates a file called `Instructions.txt`, which includes a hex-formatted program memory image.

### Step 2: Running the Program in Logisim

1. Open `MARMalade.circ` in Logisim.
2. Load `Instructions.txt` into the **Instruction Memory** module (Right-click → Load Image).
3. Manually set data memory values (hardcoded via input pins or memory editor).
4. Clock the circuit and observe the state of registers and output.

## Example Program

```asm
LDR M0 0 00
LDR M1 1 00
SUB M2 M1 M0
```

This loads values from memory address 0 and 1 into registers `M0` and `M1`, subtracts `M0` from `M1`, and stores the result in `M2`.

## Instruction Set

| Instruction | Format             | Description                               |
|------------:|--------------------|-------------------------------------------|
| `LDR`       | `LDR Md Imm 00`    | Load value from memory address `Imm` into `Md` |
| `ADD`       | `ADD Md Ma Mb`     | `Md = Ma + Mb`                            |
| `SUB`       | `SUB Md Ma Mb`     | `Md = Ma - Mb`                            |

## Documentation

See `MARMalade_CPU_Specs.pdf` or the inline docstrings and comments in `MarmAssembler.py` for a detailed breakdown of:

- Instruction encoding
- Register layout
- Circuit components
- Example usage

## Limitations

- Only 4 registers: `M0` to `M3`
- Max 4 hardcoded data memory values (address 0–3)
- No conditional branches or jumps (no control flow yet)
- Instruction entry via prompt only; no input file parsing

---
