[Digital System Design Repository GHDL Folder](https://github.com/kevinwlu/dsd/tree/master/ghdl)

# Lab 1

- [GHDL 0.37-mingw64-llvm](https://github.com/ghdl/ghdl/releases/tag/v0.37) for compiling.
- [GTKWave 3.3.100-bin-win64](https://sourceforge.net/projects/gtkwave/files/gtkwave-3.3.100-bin-win64) for waveform veiwing

## Half Adder Example:

Commnands run in git bash:
```
$ ghdl -a ha.vhdl
$ ghdl -a ha_tb.vhdl
$ ghdl -e ha_tb
$ ghdl -r ha_tb --vcd=ha.vcd
ha_tb.vhdl:47:5:@5ns:(assertion error): Reached end of test
$ gtkwave ha.vcd
```
